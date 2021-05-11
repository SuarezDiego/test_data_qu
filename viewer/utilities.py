from django.template.loader import get_template
from django.core.mail import EmailMessage
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import calendar

def sendMail(**kwargs):

    """
        html: boolean
        to_email:
        cc_email
        subject
        attach
        email_message
        data
    """

    status = True
    message = None

    try:

        html = True if 'html' in kwargs else False
        to_email = kwargs['to_email']
        cc_email = kwargs['cc_email'] if 'cc_email' in kwargs else []
        subject = kwargs['subject']
        attach = kwargs['attach'] if 'attach' in kwargs else False
        email_message = kwargs['message'] if 'message' in kwargs else ''
        data = kwargs['data'] if 'data' in kwargs else {}

        if html:
            email_message = get_template(email_message).render(data)

        email = EmailMessage(subject, email_message, settings.EMAIL_HOST_USER, to_email, cc=cc_email)

        if attach:
            email.attach_file(attach)

        if html:
            email.content_subtype = 'html'

        email.send()

    except Exception as error:

        status = False
        message = str(error)

    return {
        'status': status,
        'message': message
    }


def last_day(data):
    return date(data.year, data.month, calendar.monthrange(data.year, data.month)[1])

def add_days(date, days):
    return date + relativedelta(days=days)

def add_months(data, months):

    month = data.month - 1 + months
    year = int(data.year + month / 12 )
    month = month % 12 + 1
    day = min(data.day, calendar.monthrange(year,month)[1])

    return date(year, month, day)

def days_bettewn_dates(date_start, date_end):

    data = list()
    day = date_start
    while day <= date_end:
        data.append({
            'start': day,
            'end': day,
            })
        day = day + relativedelta(days=1)

    return data

def weeks_bettewn_dates(first_day, last_day):

    data = list()
    first_day_week = first_day - timedelta(days=first_day.weekday() % 7)
    last_day_week = first_day_week

    while last_day_week < last_day:

        last_day_week = first_day_week + timedelta(days=6)

        data.append({
            'start': first_day_week,
            'end': last_day_week,
            })

        first_day_week = last_day_week + relativedelta(days=1)

    return data

def months_bettewn_dates(date_start, date_end):

    data = list()

    while date_start <= date_end:

        data.append({
            'start': date(date_start.year, date_start.month, 1),
            'end': last_day(date_start),
            })

        date_start = add_months(date_start, 1)
        date_start = date(date_start.year, date_start.month, 1)

    return data
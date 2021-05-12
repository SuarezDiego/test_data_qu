from django.core.management.base import BaseCommand
from car_rental.models import Statistics, Client, Company, Rent, client


"""
Command to execute the test functions and store them in the database.
"""

def getClientIds():
    clients = Client.objects.all()
    return list(clients.values_list("id",flat=True))

def getClientSortByRut():
    clients = Client.objects.all().order_by("rut")
    return list(clients.values_list("id",flat=True))

def getClientSortByRentExpenses():
    clients = Client.objects.all()
    rents = Rent.objects.all()
    clients_expenses = []
    for client in clients:
        rents = Rent.objects.filter(client=client)
        client_expenses = [client.id,0]
        for rent in rents:
            client_expenses[1] += rent.daily_cost * rent.days
        clients_expenses.append(client_expenses)
    clients_sorted_expenses = sorted(
        clients_expenses,
        key=lambda client: client[1],
        reverse=True
    )
    return [Client.objects.get(id=client[0]).name for client in clients_sorted_expenses]

def getCompanyClientsSortByNames():
    dict_company = {}
    companies = Company.objects.all()
    for company in companies:
        rents = Rent.objects.filter(company=company)
        clients_ids = rents.values_list("client_id", flat=True)
        clients_ids = list(set(clients_ids))
        clients = Client.objects.filter(id__in=clients_ids).order_by("name")
        ruts = list(clients.values_list("rut",flat=True))
        dict_company[company.name] = ruts
    return dict_company

def getExpensesSortByAmount():
    company = Company.objects.get(name="RENT A CAR S.A")
    clients = Client.objects.all()
    expenses = []
    for client in clients:
        rents = Rent.objects.filter(company=company, client=client)
        aux_sum = 0
        for rent in rents:
            aux_sum += rent.daily_cost * rent.days
        expenses.append(aux_sum)
    expenses.sort(reverse=True)
    return [expense for expense in expenses if expense > 40000]

def getCompaniesSortByProfits():
    companies = Company.objects.all()
    companies_list = []
    for company in companies:
        rents = Rent.objects.filter(company=company)
        aux_sum = 0
        for rent in rents:
            aux_sum += rent.daily_cost * rent.days
        companies_list.append([company.id,aux_sum])
    sorted_companies = sorted(
        companies_list,
        key=lambda company: company[1],
        reverse=False
    )
    return [company[0] for company in sorted_companies]

def getCompanyClientsNumber():
    companies_dict = {}
    companies = Company.objects.all()
    for company in companies:
        rents = Rent.objects.filter(company=company)
        clients_ids = rents.values_list("client_id", flat=True)
        clients_ids = list(set(clients_ids))
        companies_dict[company.name]=len(clients_ids)
    return companies_dict

def getClientsWithLessExpense():
    companies = Company.objects.all()
    companies_dict = {}
    for company in companies:
        clients_expense = []
        clients_ids = Rent.objects.filter(company=company).values_list("client_id",flat=True)
        clients = Client.objects.filter(id__in=clients_ids)
        for client in clients:
            rents = Rent.objects.filter(company=company, client=client)
            aux_sum = 0
            for rent in rents:
                aux_sum += rent.daily_cost * rent.days
            clients_expense.append([client.id, aux_sum])
        less_expense = min(clients_expense, key= lambda client: client[1])
        companies_dict[company.name] = less_expense[0]
    return companies_dict

def newClientRanking():
    Client(name="Nuevo",rut="12.345.678-9").save()
    new_client = Client.objects.get(name="Nuevo",rut="12.345.678-9")
    Rent(
        client_id=new_client.id,
        company_id= 2,
        daily_cost=20000,
        days=30
    ).save()
    new_rent = Rent.objects.get(
        client_id=new_client.id,
        company_id= 2,
        daily_cost=20000,
        days=30
    )
    ranking = getClientSortByRentExpenses()
    new_client.delete()
    new_rent.delete()
    return ranking

class Command(BaseCommand):
    def handle(self, *args, **options):
        data = {}
        data["getClientIds"] = getClientIds()
        data["getClientSortByRut"] = getClientSortByRut()
        data["getClientSortByRentExpenses"] = getClientSortByRentExpenses()
        data["getCompanyClientsSortByNames"] = getCompanyClientsSortByNames()
        data["getExpensesSortByAmount"] = getExpensesSortByAmount()
        data["getCompaniesSortByProfits"] = getCompaniesSortByProfits()
        data["getCompanyClientsNumber"] = getCompanyClientsNumber()
        data["getClientsWithLessExpense"] = getClientsWithLessExpense()
        data["newClientRanking"] = newClientRanking()
        Statistics(data=data).save()

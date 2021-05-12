from django.db import models


class Statistics(models.Model):
    """
    Attributes:
        data: JSON
            The results of the test functions.
        date: datetime
            The date and time the data was written.
    """
    data = models.JSONField(null=False)
    date = models.DateTimeField(auto_now_add=True, null=False)
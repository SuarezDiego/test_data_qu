from django.db import models
from .client import Client
from .company import Company


class Rent(models.Model):
    """
    Attributes:
        client: Client
            The customer who rented.
        company: Company
            The company that rents.
        daily_cost: Integer
            The daily cost of the rental in pesos.
        days:
            The days it was rented.
    """
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    daily_cost = models.IntegerField(null=False)
    days = models.IntegerField(null=False)

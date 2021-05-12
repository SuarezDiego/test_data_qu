from django.db import models
from .client import Client
from .company import Company


class Rent(models.Model):
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    daily_cost = models.IntegerField(null=False)
    days = models.IntegerField(null=False)

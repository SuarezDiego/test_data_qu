from django.db import models


class Client(models.Model):
    rut = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

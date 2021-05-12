from django.db import models


class Client(models.Model):
    """
    Attributes:
        rut: String
            National identification number of the client.
        name: String
            Name of the client.
    """
    rut = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

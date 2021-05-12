from django.db import models

class Statistics(models.Model):
    data = models.JSONField(null=False)
    date = models.DateTimeField(auto_now_add=True, null=False)
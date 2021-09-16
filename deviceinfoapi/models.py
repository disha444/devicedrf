from django.db import models

class Devicinfo(models.Model):
    device_name = models.CharField(max_length = 100)
    device_price = models.BigIntegerField()
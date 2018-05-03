from django.db import models

# Create your models here.
class zakaz(models.Model):
    data_time = models.DateTimeField()
    status = models.TextField()


class adres(models.Model):
    region = models.TextField()
    siti   = models.TextField()
    punkt  = models.TextField()
    strid  = models.TextField()
    dom = models.TextField()
    korp = models.TextField()
    kv =models.TextField()
    adres =models.ForeignKey(zakaz, on_delete=models.CASCADE)
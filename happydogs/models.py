from django.urls import reverse
from django.db import models

class PeriodModel(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()

class DogModel(models.Model):
    id = models.IntegerField(primary_key=True)
    start = models.DateField()
    end = models.DateField()
    date_id = models.ForeignKey(PeriodModel, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
from django.db import models
from datetime import date
today = date.today()
today = today.strftime("%Y-%m-%d")

class CriminalSightingsAPI(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    date = models.DateField()
    time = models.TimeField()
    location = models.TextField()
    description = models.TextField()

class Meta:
    ordering = ['date']
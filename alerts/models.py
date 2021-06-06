from django.db import models
from datetime import date
today = date.today()
today = today.strftime("%Y-%m-%d")

class AlertAPI(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    date = models.DateField()
    time = models.TimeField()
    subject = models.TextField()
    link = models.URLField()


class Meta:
    ordering = ['date']
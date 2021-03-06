from django.db import models
from datetime import timedelta
from six import python_2_unicode_compatible
from multiselectfield import MultiSelectField


class CriminalDataAPI(models.Model):
    name = models.CharField(max_length=100, default='')
    dob = models.DateField()
    known_crimes = models.TextField()
    REGISTER_CHOICES = (('Y', 'Yes'), ('N', 'No'),)
    registered = models.CharField(max_length=1, choices=REGISTER_CHOICES)
    registered_at = models.CharField(max_length=100, default='')
    CUSTODY_CHOICES = (('Y', 'Yes'), ('N', 'No'),)
    custody = models.CharField(max_length=1, choices=CUSTODY_CHOICES)
    latest_sightings_time = models.TimeField()
    latest_sightings_date = models.DateField()
    latest_sightings_place = models.CharField(max_length=100)

# class Meta:
#     ordering = ['appointment_date']

from django.conf.urls import url
from criminal_sightings import views
from django.urls import path

urlpatterns = [
    url(r'^criminal_sightings/$', views.criminal_sightings),
    path('criminal_sightings/<str:name>/', views.criminal_sightings_name),
    path('criminal_sightings/<str:location>/', views.criminal_sightings_location)
]
from django.conf.urls import url
from criminal_data import views
from django.urls import path

urlpatterns = [
    url(r'^criminal_data/$', views.criminal_data),
    path('criminal_data/<str:name>/', views.criminal_name)
]
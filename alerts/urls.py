from django.conf.urls import url
from alerts import views
from django.urls import path

urlpatterns = [
    url(r'^alerts/$', views.alerts),
    path('alerts/<str:name>/', views.alert_name),
    path('alerts/<str:subject>/', views.alert_subject)
]
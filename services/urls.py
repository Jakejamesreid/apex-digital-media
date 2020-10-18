from django.urls import path
from . import views


urlpatterns = [
    path('', views.services, name='services'),
    path('request-service', views.request_service, name='request-service'),
]

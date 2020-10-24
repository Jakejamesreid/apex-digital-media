from django.urls import path
from . import views


urlpatterns = [
    path('', views.services, name='services'),
    path('request-service/<int:service_id>/<str:service_name>', 
         views.request_service, name='request-service'),
    path('decrement-service/<int:service_id>/<str:service_name>',
         views.decrement_service,
         name='decrement_service'),
]

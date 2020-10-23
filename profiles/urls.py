from django.urls import path
from . import views


app_name = 'profiles'
urlpatterns = [
    path('', views.profile, name='profile'),
    path('decrement-service/<int:service_id>/<str:service_name>',
         views.decrement_service,
         name='decrement_service'),
]

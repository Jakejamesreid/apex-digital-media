from django.urls import path
from . import views


urlpatterns = [
    path('', views.website_details, name='website_details'),
]

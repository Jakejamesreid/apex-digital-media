from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('<int:package_id>', views.checkout, name='checkout'),
]

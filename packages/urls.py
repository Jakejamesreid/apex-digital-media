from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_packages, name='packages'),
    path('<int:package_id>/', views.package_detail, name='package_detail'),
]

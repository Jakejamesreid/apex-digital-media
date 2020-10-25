from django.urls import path
from . import views


urlpatterns = [
    path('', views.website_details, name='website_details'),
    path('<int:website_id>', views.website_details, name='website_details'),
    path('submit-website-details', views.submit_website_details,
         name='submit_website_details'),
]

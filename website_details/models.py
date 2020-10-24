from django.db import models
from profiles.models import UserProfile


class Website(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=1, blank=True, related_name='websites')
    company_name = models.CharField(max_length=50)
    company_description = models.TextField()
    current_url = models.CharField(max_length=100, blank=True, null=True)
    new_site_description = models.TextField()

    def __str__(self):
        return self.company_name

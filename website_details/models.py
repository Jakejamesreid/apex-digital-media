from django.db import models
from profiles.models import UserProfile
from services.models import Services


class Website(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                     null=1, blank=True)
    services = models.OneToOneField(Services, null=True,
                                    on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    company_description = models.TextField()
    current_url = models.CharField(max_length=100, blank=True, null=True)
    new_site_description = models.TextField()

    def __str__(self):
        return self.company_name

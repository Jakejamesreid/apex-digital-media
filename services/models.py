from django.db import models
from packages.models import Package
from profiles.models import UserProfile


class Services(models.Model):
    class Meta:
        verbose_name_plural = 'Services'

    profile = models.ForeignKey(UserProfile, null=False, blank=False,
                                on_delete=models.CASCADE)
    package = models.ForeignKey(Package, null=False, blank=False,
                                on_delete=models.CASCADE)

    remaining_pages = models.PositiveSmallIntegerField(null=True, default=0)
    remaining_email_addresses = models.PositiveSmallIntegerField(
        null=True, default=0)
    remaining_seo_updates = models.PositiveSmallIntegerField(
        null=True, default=0)
    remaining_website_updates = models.PositiveSmallIntegerField(
        null=True, default=0)

    def __str__(self):
        return f'{self.package}'

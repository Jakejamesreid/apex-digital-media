from django.db import models


class Services(models.Model):
    pages = models.PositiveSmallIntegerField(null=True)
    email_addresses = models.PositiveSmallIntegerField(null=True)
    seo_updates = models.PositiveSmallIntegerField(null=True)
    website_updates = models.PositiveSmallIntegerField(null=True)

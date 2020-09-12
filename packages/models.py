from django.db import models


class Package(models.Model):

    name = models.CharField(max_length=254)
    description = models.TextField()
    features = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    currency = models.CharField(max_length=254)

    def __str__(self):
        return self.name

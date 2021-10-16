from django.db import models

# Create your models here.


class ProductModel(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False)

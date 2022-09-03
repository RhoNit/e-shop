from django.db import models
from .categories import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='upload/products/')
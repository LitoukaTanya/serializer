from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Rating(models.Model):
    score = models.FloatField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField()






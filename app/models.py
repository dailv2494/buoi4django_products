from django.db import models

class Product(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()

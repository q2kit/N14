from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=100)


class Product(models.Model):
    productName = models.CharField(max_length=100)
    unitPrice = models.IntegerField()
    category = models.CharField(max_length=100)
    quantityInStock = models.IntegerField()
    showcasedImg = models.ImageField(null=True)


class Product_img(models.Model):
    productID = models.IntegerField()
    image = models.ImageField(null=True)

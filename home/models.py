from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=10, primary_key=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantityInStock = models.IntegerField()
    showcasedImg = models.ImageField(null=True)
    id = models.CharField(max_length=32, primary_key=True)

    def __str__(self):
        return self.id


class Product_img(models.Model):
    productID = models.IntegerField()
    image = models.ImageField(null=True)


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.CharField(max_length=10)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name


class Product_review(models.Model):
    productId = models.CharField(max_length=32)
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=10)
    content = models.CharField(max_length=40)

    def __str__(self):
        return self.content

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
        return self.name


class Product_img(models.Model):
    id = models.AutoField(primary_key=True)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    image = models.ImageField(null=True)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    stt = (
        ('incart','Trong giỏ hàng'),
        ('processing', 'Đang xử lý'),
        ('done', 'Đã hoàn thành'),
    )
    status = models.CharField(max_length=20,choices=stt,default='inCart')

    def __str__(self):
        return str(self.id)

from django.db import models


# Create your models here.

class Tinh(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name
class Huyen(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    tinh = models.ForeignKey(Tinh, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Xa(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    huyen = models.ForeignKey(Huyen, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=10, primary_key=True)
    password = models.CharField(max_length=100)
    tinh = models.ForeignKey(Tinh, on_delete=models.SET_NULL, null=True)
    huyen = models.ForeignKey(Huyen, on_delete=models.SET_NULL, null=True)
    xa = models.ForeignKey(Xa, on_delete=models.SET_NULL, null=True)

    def add(self):
        return self.xa.name + ' ' + self.huyen.name + ' ' + self.tinh.name
    
    def numCart(self):
        return len(Order.objects.filter(customer=self, status="incart"))

    def __str__(self):
        return self.name



class Product(models.Model):
    type = models.CharField(max_length=100, choices=[('iphone', 'iphone'), ('ipad', 'ipad'), ('mac', 'mac'), ('watch', 'watch'),], default='iphone')
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


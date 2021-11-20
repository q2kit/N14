from django.contrib import admin
from .models import *


# Register your models here.


class CustomerController(admin.ModelAdmin):
    list_display = ['phone', 'name', 'password']


class ProductController(admin.ModelAdmin):
    list_display = ['id', 'name', 'price',
                    'showcasedImg', 'quantityInStock', 'type']
    list_filter = ['type']


class OrderController(admin.ModelAdmin):
    list_display = ['id', 'product', 'customer', 'quantity', 'status']
    list_filter = ['status', 'customer', 'product', ]


class TinhController(admin.ModelAdmin):
    list_display = ['id', 'name']

class HuyenController(admin.ModelAdmin):
    list_display = ['id', 'name', 'tinh']
    list_filter = ['tinh']

class XaController(admin.ModelAdmin):
    list_display = ['id', 'name', 'huyen']
    list_filter = ['huyen']

admin.site.register(Customer, CustomerController)
admin.site.register(Product, ProductController)
admin.site.register(Product_img)
admin.site.register(Order, OrderController)
admin.site.register(Tinh, TinhController)
admin.site.register(Huyen, HuyenController)
admin.site.register(Xa, XaController)

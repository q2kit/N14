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


admin.site.register(Customer, CustomerController)
admin.site.register(Product, ProductController)
admin.site.register(Product_img)
admin.site.register(Order, OrderController)

from django.contrib import admin
from .models import *


# Register your models here.


class CustomerController(admin.ModelAdmin):
    list_display = ['phone', 'name', 'password']


class ProductController(admin.ModelAdmin):
    list_display = ['id', 'name', 'price',
                    'showcasedImg', 'quantityInStock', 'type']


admin.site.register(Customer, CustomerController)
admin.site.register(Product, ProductController)
admin.site.register(Product_img)

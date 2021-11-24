from django.contrib import admin
from .models import *


# Register your models here.


class CustomerController(admin.ModelAdmin):
    list_display = ['phone', 'name', 'password']
    search_fields = ['phone', 'name']

class ProductController(admin.ModelAdmin):
    list_display = ['id', 'name', 'price',
                    'showcasedImg', 'quantityInStock', 'type']
    list_filter = ['type']
    search_fields = ['name']


class OrderController(admin.ModelAdmin):
    list_display = ['id', 'product', 'customer', 'quantity', 'status']
    list_filter = ['status', 'customer', 'product', ]
    search_fields = ['id', 'customer', 'product']

class CityController(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

class DistrictController(admin.ModelAdmin):
    list_display = ['id', 'name', 'city']
    list_filter = ['city']
    search_fields = ['name']

class WardController(admin.ModelAdmin):
    list_display = ['id', 'name', 'district']
    list_filter = ['district']
    search_fields = ['name']

admin.site.register(Customer, CustomerController)
admin.site.register(Product, ProductController)
admin.site.register(Product_img)
admin.site.register(Order, OrderController)
admin.site.register(City, CityController)
admin.site.register(District, DistrictController)
admin.site.register(Ward, WardController)

from django.contrib import admin
from .models import *


# Register your models here.


class CustomerController(admin.ModelAdmin):
    list_display = ['phone', 'name', 'password']
    search_fields = ['phone', 'name']


class ProductController(admin.ModelAdmin):
    list_display = ['id', 'name', 'price',
                    'showcasedImg', 'quantityInStock', 'type', 'sale']
    list_filter = ['type']
    search_fields = ['name']


class OrderController(admin.ModelAdmin):
    list_display = ['id', 'product', 'productImg',
                    'productCapacity', 'customer', 'quantity', 'status']
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


# class Product_ColorController(admin.ModelAdmin):
#     list_display = ['id', 'productID', 'color']
#     list_filter = ['productID']
#     search_fields = ['productID']


class Product_Img_ColorController(admin.ModelAdmin):
    list_display = ['id', 'productID', 'img', 'color']
    list_filter = ['productID']
    search_fields = ['productID']


class Product_CapacityController(admin.ModelAdmin):
    list_display = ['id', 'productID', 'capacity']
    list_filter = ['productID']
    search_fields = ['productID']


admin.site.register(Customer, CustomerController)
admin.site.register(Product, ProductController)
admin.site.register(Order, OrderController)
admin.site.register(City, CityController)
admin.site.register(District, DistrictController)
admin.site.register(Ward, WardController)
admin.site.register(Product_img_color, Product_Img_ColorController)
admin.site.register(Product_Capacity, Product_CapacityController)

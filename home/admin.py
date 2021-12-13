from django.contrib import admin
from .models import *


# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['phone', 'name', 'password', 'is_staff']
    search_fields = ['phone', 'name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price',
                    'showcasedImg', 'quantityInStock', 'type', 'sale']
    list_filter = ['type']
    search_fields = ['name', 'id']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'productImg',
                    'productCapacity', 'customer', 'quantity', 'status']
    list_filter = ['status', 'customer', 'product', ]
    search_fields = ['id', 'customer', 'product']


class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city']
    list_filter = ['city']
    search_fields = ['name']


class WardAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'district']
    list_filter = ['district']
    search_fields = ['name']


# class Product_ColorAdmin(admin.ModelAdmin):
#     list_display = ['id', 'productID', 'color']
#     list_filter = ['productID']
#     search_fields = ['productID']


class Product_Img_ColorAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'img', 'color']
    list_filter = ['product']
    search_fields = ['product__name']


class Product_CapacityAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'capacity']
    list_filter = ['product']
    search_fields = ['product__name', 'id']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'district', 'ward']
    list_filter = ['city']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Ward, WardAdmin)
admin.site.register(Product_img_color, Product_Img_ColorAdmin)
admin.site.register(Product_Capacity, Product_CapacityAdmin)
admin.site.register(Address, AddressAdmin)
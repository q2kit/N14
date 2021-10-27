from django.contrib import admin
from .models import Customer, Product_img, Product
# Register your models here.

admin.site.register(Customer)


class ProductController(admin.ModelAdmin):
    list_display = ['id', 'productName', 'unitPrice',
                    'showcasedImg', 'quantityInStock', 'category']


admin.site.register(Product, ProductController)
admin.site.register(Product_img)

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "id",
            "type",
            "name",
            "price",
            "quantityInStock",
            "showcasedImg",
            "sale",
        ]
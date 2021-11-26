from django.views.generic import ListView

from home.models import Product


class ProductListView(ListView):
    model = Product

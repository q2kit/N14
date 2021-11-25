from django.views.generic import ListView

from home.models import Product


class ContactListView(ListView):
    paginate_by = 2
    model = Product

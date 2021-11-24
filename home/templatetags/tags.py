from django import template
from home.models import Order, Customer


register = template.Library()


@register.simple_tag
def number_in_cart(request):
    try:
        phone = request.session['customer']
        customer = Customer.objects.get(phone=phone)
        num = len(Order.objects.filter(customer=customer, status='incart'))
    except:
        num = 0
    return num

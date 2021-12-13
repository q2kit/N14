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


@register.simple_tag()
def multiply(sale, unit_price, *args, **kwargs):
    # you would need to do any localization of the result here
    if(sale == None):
        sale = 0
    return int((1-sale)*unit_price)


@register.simple_tag()
def mul(*args, **kwargs):
    # you would need to do any localization of the result here
    try:
        result = 1
        for arg in args:
            result *= arg
        return int(result)
    except:
        return 0


@register.simple_tag()
def total(id):
    try:
        order = Order.objects.get(id=id)
        return int(order.quantity*order.product.price*(1-order.product.sale))
    except:
        return int(order.quantity*order.product.price)

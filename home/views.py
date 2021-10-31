from django.http.response import *
from django.shortcuts import render
from django.shortcuts import redirect
from .models import *


# Create your views here.

def index(request):
    try:
        phone = request.session['customer']
        customer = Customer.objects.get(phone=phone)
    except KeyError:
        customer = None
    Data = {'products': Product.objects.all(), 'customer': customer}
    return render(request, 'index.html', Data)

def productDetail(request, id):
    if id is None:
        return redirect('/')
    Data = {'product': Product.objects.get(id=id)}
    return render(request, 'productDetail.html', Data)


def category(request, category):
    Data = {
        'products': Product.objects.filter(type=category),
        'type': category
    }
    return render(request, 'category.html', Data)


def register(request):
    try:
        phone = request.session['customer']
        return redirect('/')
    except KeyError:
        pass

    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            return render(request, 'register.html',
                          {'result': "Mật khẩu không trùng khớp.", 'name': name, 'phone': phone})
        # if password != password2:
        #     return render(request, 'register.html', {'result': "Mật khẩu không trùng khớp."})
        try:
            Customer.objects.get(phone=phone)
            return render(request, 'register.html', {'result': "Tài khoản đã tồn tại."})
        except Customer.DoesNotExist:
            Customer.objects.create(name=name, phone=phone, password=password)
            return render(request, 'login.html', {'result': 'completeRegistration'})
    return render(request, 'register.html', {'result': ''})


def login(request):
    try:
        phone = request.session['customer']
        return redirect('/')
    except KeyError:
        pass
    if request.method == 'POST':
        phone = request.POST['phone']
        password = request.POST['password']
        try:
            customer = Customer.objects.get(phone=phone, password=password)
            request.session['customer'] = customer.phone
            return redirect('/')
        except Customer.DoesNotExist:
            return render(request, 'login.html', {'result': 'incorrect'})

    return render(request, 'login.html', {'result': None})


def forgot(request):
    try:
        phone = request.session['customer']
        return redirect('/')
    except KeyError:
        pass
    passwordDefault = "5ghfE$Dg"

    if request.method == 'POST':
        phone = request.POST['phone']
        try:
            user = Customer.objects.get(phone=phone)

        except Customer.DoesNotExist:
            return render(request, 'forgot.html', {'result': 'notFound'})

    return render(request, 'forgot.html', {'result': 'getPhone'})


def search(request):
    if request.method == 'GET':
        try:
            q = request.GET['q'].lower().split()
            products = Product.objects.all()
            result = []
            for product in products:
                ok = False
                for text in q:
                    if text in product.name.lower():
                        result.append(product)
                        break

            return render(request, 'search.html', {'result': result})
        except:
            return render(request, 'search.html', {'result': None})

    return render(request, 'search.html', {'result': None})


def account(request):
    try:
        phone = request.session['customer']
        customer = Customer.objects.get(phone=phone)
    except KeyError:
        return redirect('/login')
    return render(request, 'account.html')

def logout(request):
    try:
        del request.session['customer']
    except KeyError:
        pass
    return redirect('/')

def iphone(request):
    products = Product.objects.filter(type='iphone')
    return render(request, 'iphone.html', {'products': products})
    pass

def ipad(request):
    products = Product.objects.filter(type='ipad')
    return render(request, 'ipad.html',{'products': products})
    pass

def mac(request):
    products = Product.objects.filter(type='mac')
    return render(request, 'mac.html', {'products': products})
    pass

def watch(request):
    products = Product.objects.filter(type='watch')
    return render(request, 'watch.html', {'products': products})
    pass

def page_not_found_view(request, exception):
    return redirect('/')
    
def cart(request):
    return HttpResponse('cart')
    pass

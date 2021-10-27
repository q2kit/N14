from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Customer, Product


# Create your views here.

def index(request):
    Data = {'products': Product.objects.all()}
    return render(request, 'index.html', Data)


def register(request):
    if request.method == 'POST':
        ls = request.POST.dict()
        name = ls.get('name')
        phone = ls.get('phone')
        password = ls.get('password')
        password2 = ls.get('password2')

        if password != password2:
            return render(request, 'register.html', {'result': "Mật khẩu không trùng khớp.", 'name': name, 'phone': phone})
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
    if request.method == 'POST':
        phone = request.POST.dict().get('phone')
        password = request.POST.dict().get('password')
        try:
            obj = Customer.objects.get(phone=phone, password=password)
        except Customer.DoesNotExist:
            obj = None

        if obj:
            return redirect('/')
        else:
            return render(request, 'login.html', {'result': 'incorrect'})

    return render(request, 'login.html', {'result': None})


def forgot(request):
    passwordFefault = "5ghfE$Dg"

    if request.method == 'POST':
        phone = request.POST.dict().get('phone')
        try:
            obj = Customer.objects.get(phone=phone)

        except Customer.DoesNotExist:
            return render(request, 'forgot.html', {'result': 'notFound'})

    return render(request, 'forgot.html', {'result': 'getPhone'})

from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Customer


# Create your views here.

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        ls = request.POST.dict()
        name = ls.get('name')
        phone = ls.get('phone')
        password = ls.get('password')
        password2 = ls.get('password2')

        if password != password2:
            return render(request, 'register.html', {'err': "Mật khẩu không trùng khớp."})
        try:
            Customer.objects.get(phone=phone)
            return render(request, 'register.html', {'err': "Tài khoản đã tồn tại."})
        except Customer.DoesNotExist:
            Customer.objects.create(name=name, phone=phone, password=password)
            return render(request, 'login.html', {'code': 'completeRegistration'})
    return render(request, 'register.html', {'err': None})


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
            return render(request, 'login.html', {'code': 'incorrect'})

    return render(request, 'login.html', {'code': None})


def forgot(request):
    passwordFefault = "5ghfE$Dg"

    if request.method == 'POST':
        phone = request.POST.dict().get('phone')
        try:
            obj = Customer.objects.get(phone=phone)

        except Customer.DoesNotExist:
            return render(request, 'forgot.html', {'msg': 'notFound'})

    return render(request, 'forgot.html', {'msg': 'getPhone'})

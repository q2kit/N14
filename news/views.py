from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import NewForm

# Create your views here.

def index(response):
    return render(response,'news.html')

def add(request):
    if request.method == 'POST':
        f = NewForm(request.POST)
        if f.is_valid():
            f.save()
            return render(request,'add.html',{'form':NewForm,'ok':True})
        else: return HttpResponse('<h1>Lỗi</h1>')
    return render(request,'add.html',{'form':NewForm,'ok':False})
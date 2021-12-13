from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from home.models import *
from django.core.files.storage import FileSystemStorage

# Create your views here.


def index(request):
    products = Product.objects.all().order_by('type')
    return render(request, 'staff/index.html', {'products': products})


def addProduct(request):
    try:
        user = Customer.objects.get(phone=request.session['customer'])
        if request.method == 'POST':
            if user.is_staff:
                id = request.POST['id']
                try:
                    Product.objects.get(id=id)
                    return JsonResponse({'status': 'error', 'message': 'Product already exists'})
                except Product.DoesNotExist:
                    pass
                type = request.POST['type']
                name = request.POST['name']
                price = request.POST['price']
                quantityInStock = request.POST['quantity']
                sale = int(request.POST['sale'])/100
                img = request.FILES['img']
                fs = FileSystemStorage()
                if not fs.exists(str(img)):
                    fs.save(img.name, img)
                showcasedImg = img.name
                Product.objects.create(id=id, type=type, name=name, price=price,
                                       quantityInStock=quantityInStock, showcasedImg=showcasedImg, sale=sale)

                return JsonResponse({'status': 'success', 'message': 'Product added successfully'})
            else:
                return JsonResponse({'status': 'error', 'message': 'You are not authorized to add products'})
        else:
            return render(request, 'staff/addProduct.html')
    except KeyError:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def deleteProduct(request, id):
    try:
        user = Customer.objects.get(phone=request.session['customer'])
        if user.is_staff:
            try:
                product = Product.objects.get(id=id)
                if product.showcasedImg:
                    fs = FileSystemStorage()
                    fs.delete(product.showcasedImg.path)
                product.delete()
                return JsonResponse({'status': 'success', 'message': 'Product deleted successfully'})
            except:
                return JsonResponse({'status': 'error', 'message': 'Product not found'})
        else:
            return JsonResponse({'status': 'error', 'message': 'You are not authorized to delete products'})
    except:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def editProduct(request, id):
    try:
        user = Customer.objects.get(phone=request.session['customer'])
        if request.method == 'POST':
            if user.is_staff:
                type = request.POST['type']
                name = request.POST['name']
                price = request.POST['price']
                quantityInStock = request.POST['quantityInStock']
                sale = int(request.POST['sale'])/100
                img = request.FILES['img']
                fs = FileSystemStorage()
                if not fs.exists(str(img)):
                    fs.save(img.name, img)
                showcasedImg = img.name
                product = Product.objects.get(id=id)
                product.type = type
                product.name = name
                product.price = price
                product.quantityInStock = quantityInStock
                product.showcasedImg = showcasedImg
                product.sale = sale
                product.save()
                return JsonResponse({'status': 'success', 'message': 'Product edited successfully'})
            else:
                return JsonResponse({'status': 'error', 'message': 'You are not authorized to edit products'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid request'})
    except KeyError:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def order(request):
    try:
        user = Customer.objects.get(phone=request.session['customer'])
        if user.is_staff:
            orders = Order.objects.all()
            return render(request, 'staff/order.html', {'orders': orders})
        else:
            return JsonResponse({'status': 'error', 'message': 'You are not authorized to view orders'})
    except KeyError:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def shipping(request, id):
    try:
        user = Customer.objects.get(phone=request.session['customer'])
        if user.is_staff:
            try:
                order = Order.objects.get(id=id)
                order.status = 'shipping'
                order.save()
                return JsonResponse({'status': 'success', 'message': 'Order shipped successfully'})
            except Order.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Order not found'})
        else:
            return JsonResponse({'status': 'error', 'message': 'You are not authorized to view orders'})
    except KeyError:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def done(request, id):
    try:
        user = Customer.objects.get(phone=request.session['customer'])
        if user.is_staff:
            try:
                order = Order.objects.get(id=id)
                order.status = 'done'
                order.save()
                return JsonResponse({'status': 'success', 'message': 'Order completed successfully'})
            except Order.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Order not found'})
        else:
            return JsonResponse({'status': 'error', 'message': 'You are not authorized to view orders'})
    except KeyError:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'})
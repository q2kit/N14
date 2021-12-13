from django.http.response import *
from django.http import *
from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import redirect
from .models import *
import hashlib


# Create your views here.
# import copy
# def index(request):
#     xx = Order.objects.all()
#     for x in xx:
#         copy.copy(x).save(using='dj')
#     pass

# def index(request):
#     if Product_Capacity.objects.all().count() > 0:
#         return HttpResponse("<h1>Done</h1>")
#     products = Product.objects.filter(type='iphone')
#     for product in products:
#         Product_Capacity.objects.create(product=product, capacity='64GB')
#         Product_Capacity.objects.create(product=product, capacity='128GB')
#         Product_Capacity.objects.create(product=product, capacity='512GB')
#         Product_Capacity.objects.create(product=product, capacity='1TB')

#     products = Product.objects.filter(type='ipad')
#     for product in products:
#         Product_Capacity.objects.create(product=product, capacity='64GB')
#         Product_Capacity.objects.create(product=product, capacity='128GB')
#         Product_Capacity.objects.create(product=product, capacity='512GB')
#         Product_Capacity.objects.create(product=product, capacity='1TB')

#     products = Product.objects.filter(type='mac')
#     for product in products:
#         Product_Capacity.objects.create(product=product, capacity='RAM 16GB - SSD 256GB')
#         Product_Capacity.objects.create(product=product, capacity='RAM 32GB - SSD 512GB')

#     products = Product.objects.filter(type='watch')
#     for product in products:
#         Product_Capacity.objects.create(product=product, capacity='41mm')
#         Product_Capacity.objects.create(product=product, capacity='45mm')

    # return HttpResponse("<h1>Done</h1>")

# def index(request):
#     f = open('D:/Desktop/f.txt','r',encoding='utf-8')
#     for line in f.readlines():
#         xa,huyen,tinh=line.split('/')
#         xaid,xa=xa.split(',')
#         huyenid,huyen=huyen.split(',')
#         tinhid,tinh=tinh.split(',')
#         xaid=xaid.strip()
#         huyenid=huyenid.strip()
#         tinhid=tinhid.strip()
#         xa=xa.strip()
#         huyen=huyen.strip()
#         tinh=tinh.strip()
#         try:
#             City.objects.get(id=tinhid)
#         except:
#             City.objects.create(id=tinhid,name=tinh)
#         try:
#             District.objects.get(id=huyenid)
#         except:
#             District.objects.create(id=huyenid,name=huyen,city_id=tinhid)
#         try:
#             Ward.objects.get(id=xaid)
#         except:
#             Ward.objects.create(id=xaid,name=xa,district_id=huyenid)
#     f.close()
#     return HttpResponse("<h1>Done</h1>")

def index(request):
    # return JsonResponse({'status': 'success', 'message': 'Đăng nhập thành công','x':True})
    # return JsonResponse(request.COOKIES)
    try:
        phone = request.session['customer']
        customer = Customer.objects.get(phone=phone)
    except KeyError:
        customer = None
    iPhone = Product.objects.filter(type='iphone')
    mac = Product.objects.filter(type='mac')
    watch = Product.objects.filter(type='watch')
    iPad = Product.objects.filter(type='ipad')
    Data = {
        'iPhone': iPhone,
        'mac': mac,
        'watch': watch,
        'iPad': iPad,
        'customer': customer
    }
    return render(request, 'home/index.html', Data)


def addToCart(request, id):
    try:
        phone = request.session['customer']
        customer = Customer.objects.get(phone=phone)
    except KeyError:  # not login
        return redirect('/login')
    try:

        product = Product.objects.get(id=id)

        # lấy danh sách màu của sản phẩm đc chọn
        colors = Product_img_color.objects.all().filter(product=product)
        # lấy giá trị màu mà user chọn
        selectedcolor = request.GET.get('color')
        # mặc định màu là màu đầu tiên
        if selectedcolor == None:
            selectedcolor = list(colors)[0].color
        # lấy link ảnh từ màu đc chọn
        productImg = Product_img_color.objects.get(color=selectedcolor, product=product).img.url
        # lấy danh sách dung lượng của sản phẩm đc chọn
        capacityList = Product_Capacity.objects.all().filter(product=product)
        selectedcapacity = request.GET.get('capacity')
        if selectedcapacity == None:
            selectedcapacity = list(capacityList)[0].capacity

        if(product.quantityInStock == 0):
            return HttpResponse("<h1>Sản phẩm đã hết hàng</h1>")
        product.quantityInStock -= 1
        product.save()
    except:  # error id
        return HttpResponseBadRequest("<h1>Sản phẩm không tồn tại</h1>")

    try:
        order = Order.objects.get(
            customer=customer, product_id=id, productImg=productImg, productCapacity=selectedcapacity, status='incart')
        order.quantity += 1
        order.save()
    except:  # order not found
        Order.objects.create(customer=customer, product_id=id, productImg=productImg, productCapacity=selectedcapacity,
                             quantity=1, status='incart')

    return redirect('/product/'+id+f'?color={selectedcolor}&capacity={selectedcapacity}')


def removeFromCart(request):
    if request.is_ajax() and request.method == 'POST':
        try:
            phone = request.session['customer']
            customer = Customer.objects.get(phone=phone)
        except KeyError:
            return redirect('/')
        
        id = request.POST.get('id')
        try:
            order = Order.objects.get(id=int(id), status='incart')
            product = Product.objects.get(id=order.product_id)
            product.quantityInStock += order.quantity
            product.save()
            order.delete()
            return JsonResponse({
                'status': 'success',
                'message': 'Xóa thành công',
                'numInCart': Order.objects.filter(customer=customer, status='incart').count()
            })
        except:
            return redirect('/')
    return redirect('/')


def add(request):
    try:
        phone = request.session['customer']
        customer = Customer.objects.get(phone=phone)
    except KeyError:  # not login
        return redirect('/login')
    try:
        id = request.POST.get('id')
        order = Order.objects.get(id=int(id))
        product = Product.objects.get(id=order.product_id)
        if(product.quantityInStock == 0):
            return JsonResponse({'status': 'error', 'message': 'Sản phẩm đã hết hàng'})
        else:
            product.quantityInStock -= 1
            product.save()
        order.quantity += 1
        order.save()
        return JsonResponse({'status': 'success', 'message': 'Thêm sản phẩm thành công', 'num': order.quantity})
    except:
        return redirect('/')


def sub(request):
    try:
        phone = request.session['customer']
        customer = Customer.objects.get(phone=phone)
    except KeyError:  # not login
        return redirect('/login')
    try:
        id = request.POST.get('id')
        order = Order.objects.get(id=int(id))
        product = Product.objects.get(id=order.product_id)
        product.quantityInStock += 1
        product.save()
        order.quantity -= 1
        order.save()
        if order.quantity == 0:
            order.delete()
        numInCart = Order.objects.filter(customer=customer, status='incart').count()
        return JsonResponse({
            'status': 'success', 
            'message': 'Bớt sản phẩm thành công', 
            'num': order.quantity,
            'numInCart': numInCart
        })
    except:
        return redirect('/')

def productDetail(request, id):

    if id is None:
        return redirect('/')
    # try:
    product = Product.objects.get(id=id)
    colors = Product_img_color.objects.filter(product=product)
    selectedcolor = request.GET.get('color')
    if selectedcolor == None:
        selectedcolor = list(colors)[0].color
    # try:
    productImg = Product_img_color.objects.get(
        color=selectedcolor, product=product)
    capacityList = Product_Capacity.objects.filter(product=product)
    # for capacity in capacityList:
    #     print(capacity.capacity)
    selectedcapacity = request.GET.get('capacity')
    if selectedcapacity == None:
        selectedcapacity = list(capacityList)[0].capacity
    Data = {
        'product': Product.objects.get(id=id),
        'selectedcolor': selectedcolor,
        'colors': colors,
        'productImg': productImg,
        'capacityList': capacityList,
        "selectedcapacity": selectedcapacity
    }
    # except:
        # return redirect('/')
    return render(request, 'home/productDetail.html', Data)


def category(request, category):
    types = {'iphone': 'iPhone', 'ipad': 'iPad',
             'mac': 'Mac', 'watch': 'Watch'}
    if category not in types:
        return redirect('/')

    paginator = Paginator(Product.objects.filter(type=category), 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    Data = {

        'type': types[category],
        'page_obj': page_obj
    }

    return render(request, 'home/category.html', Data)


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
        if phone[0] != '0' or len(phone) != 10 or not(all([(x <= '9' and x >= '0') for x in phone])):
            return render(request, 'home/register.html', {'result': 'Số điện thoại không hợp lệ!', 'name': name, 'phone': phone})

        if password != password2:
            return render(request, 'home/register.html',
                          {'result': "Mật khẩu không trùng khớp.", 'name': name, 'phone': phone})
        # if password != password2:
        #     return render(request, 'register.html', {'result': "Mật khẩu không trùng khớp."})
        try:
            Customer.objects.get(phone=phone)
            return render(request, 'home/register.html', {'result': "Tài khoản đã tồn tại."})
        except Customer.DoesNotExist:
            password = hashlib.sha256(password.encode()).hexdigest()
            Customer.objects.create(name=name, phone=phone, password=password)
            return render(request, 'home/login.html', {'result': 'completeRegistration'})
    return render(request, 'home/register.html', {'result': ''})


def login(request):
    try:
        phone = request.session['customer']
        return redirect('/')
    except KeyError:
        pass
    if request.method == 'POST':
        phone = request.POST['phone']
        if(phone[0] != '0' and len(phone) != 10):
            phone = '0'+phone
        password = request.POST['password']
        password = hashlib.sha256(password.encode()).hexdigest()
        try:
            customer = Customer.objects.get(phone=phone, password=password)
            request.session['customer'] = customer.phone
            return redirect('/')
        except Customer.DoesNotExist:
            return render(request, 'home/login.html', {'result': 'incorrect', 'phone': phone})

    return render(request, 'home/login.html', {'result': None})


def forgot(request):
    try:
        phone = request.session['customer']
        return redirect('/')
    except KeyError:
        pass
    passwordDefault = "5ghfE$Dg"

    if request.method == 'POST':
        phone = request.POST['phone']
        otp = request.POST['otp']
        try:
            user = Customer.objects.get(phone=phone)
            user.password = hashlib.sha256(
                passwordDefault.encode()).hexdigest()
            user.save()
        except Customer.DoesNotExist:
            return render(request, 'home/forgot.html', {'result': 'notFound'})
        # return HttpResponse("<h1>Đổi mật khẩu thành công</h1><h1>Mật khẩu mới là "+passwordDefault+"</h1>")
        return render(request, 'home/login.html', {'result': 'resetpw', 'newpw': passwordDefault})

    return render(request, 'home/forgot.html', {'result': 'getPhone'})


def search(request):
    print(request.GET)
    if request.method == 'GET':
        try:
            q = request.GET['q'].lower().split()
            if q == []: # q is empty or q don't have any words / characters
                return redirect('/')
            products = Product.objects.all()
            result = dict()
            for product in products:
                for text in q:
                    if text in product.name.lower():
                        if product in result:
                            result[product] += 1
                        else:
                            result[product] = 1

            result = sorted(result.items(), key=lambda x: x[1], reverse=True)
            result = [x[0] for x in result]
            paginator = Paginator(result, 9)

            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'home/search.html', {'result': result, 'page_obj': page_obj})

        except KeyError: # q don't exist in request.GET
            return redirect('/')

    return render(request, 'home/search.html', {'result': None})


def account(request):
    try:
        phone = request.session['customer']
        customer = Customer.objects.get(phone=phone)
    except KeyError:
        return redirect('/login')
    return render(request, 'home/account.html', {'customer': customer})


def edit(request):
    try:
        phone = request.session['customer']
        customer = Customer.objects.get(phone=phone)
    except KeyError:
        return redirect('/')

    data = {
        'list_city': City.objects.all(),
        'list_district': District.objects.all(),
        'list_ward': Ward.objects.all(),
        'customer': customer,
        'result': None
    }

    if request.method == 'POST':
        name = request.POST['name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        city = request.POST['city']
        district = request.POST['district']
        ward = request.POST['ward']
        street = request.POST['street']

        if password1 != password2:
            return render(request, 'home/edit.html', {'result': 'notMatch'})

        customer.name = name
        if password1 != '':
            customer.password = hashlib.sha256(password1.encode()).hexdigest()
        customer.city = City.objects.get(id=city)
        customer.district = District.objects.get(id=district)
        customer.ward = Ward.objects.get(id=ward)
        customer.street = street
        customer.save()
        data['result'] = 'done'
        return render(request, 'home/edit.html', data)

    return render(request, 'home/edit.html', data)


def logout(request):
    try:
        del request.session['customer']
    except KeyError:
        pass
    return redirect('/')


def page_not_found_view(request, exception):
    return redirect('/')


def order(request):
    try:
        phone = request.session['customer']
        customer = Customer.objects.get(phone=phone)
    except KeyError:
        return redirect('/login')

    orders = Order.objects.filter(customer=customer)
    data = {
        'cart': list(filter(lambda x: x.status == 'incart', orders)),
        'totalcart': sum([int((1-x.product.sale if x.product.sale != None else 1)*x.product.price*x.quantity) for x in orders if x.status == 'incart']),
        'done': list(filter(lambda x: x.status == 'done', orders)),
        'totaldone': sum([int((1-x.product.sale if x.product.sale != None else 1)*x.product.price*x.quantity) for x in orders if x.status == 'done']),
        'processing': list(filter(lambda x: x.status == 'processing', orders)),
        'totalprocessing': sum([int((1-x.product.sale if x.product.sale != None else 1)*x.product.price*x.quantity) for x in orders if x.status == 'processing'])
    }

    return render(request, 'home/order.html', data)
    pass


def pay(request):
    try:
        phone = request.session['customer']
        customer = Customer.objects.get(phone=phone)
    except KeyError:
        return redirect('/')

    for order in Order.objects.filter(customer=customer, status='incart'):
        order.status = 'processing'
        order.save()

    return redirect('/order')

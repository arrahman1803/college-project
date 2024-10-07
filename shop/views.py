from itertools import count
from lib2to3.fixes.fix_input import context

from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Count
from django.template.loader import render_to_string

from shop.models import Product, Category, CartOrder, CartOrderItems


# Create your views here.
def index(request):
    products = Product.objects.all().order_by('-date')[:8]
    context = {'product' : products}
    return render(request, "shop/index.html" , context)

def product(request, pid):
    product = Product.objects.get(pid = pid)
    p_image = product.p_images.all()
    p_size = product.p_size.all()
    p_color = product.p_color.all()
    context = {'p' : product, 'p_images': p_image, 'p_size': p_size, 'p_color': p_color}
    return render(request, "shop/product.html" , context)

def category(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, "shop/category.html", context)

def category_products(request,cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(category =category)
    context = {'product': products, 'category' : category}
    return render(request, "shop/category_products.html", context)

def products(request):
    products = Product.objects.all()
    context = {'product': products}
    return render(request, "shop/products.html", context)

def add_to_cart(request):
    cart_product = {}

    cart_product[str(request.GET['id'])] = {
        'title' : request.GET['title'],
        'qty' : request.GET['qty'],
        'size' : request.GET['size'],
        'color' : request.GET['color'],
        'price' : request.GET['price'],
        'image' : request.GET['image'],
        'pid' : request.GET['pid'],
    }
    print(cart_product)
    if 'cart_data_obj' in request.session:
        if str(request.GET['id']) in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]['qty'] = int(cart_product[str(request.GET['id'])]['qty'])
            cart_data.update(cart_data)
            request.session['cart_data_obj'] = cart_data
        else:
            cart_data = request.session['cart_data_obj']
            cart_data.update(cart_product)
            request.session['cart_data_obj'] = cart_data
            print(cart_data)
    else:
        request.session['cart_data_obj'] = cart_product
    return JsonResponse({"data" : request.session['cart_data_obj'], "totalcartitems" : len(request.session['cart_data_obj'])})

def serach(request):
    query = request.GET.get("search-navbar", "").strip()  # Get the search query and strip whitespace
    products = []

    if query:  # Only perform search if query is not empty
        products = Product.objects.filter(
            title__icontains=query
        ).union(
            Product.objects.filter(description__icontains=query)
        ).order_by("-date")
    context = {
        "products" : products,
        "query" : query
    }
    return render(request, "shop/search.html", context)


def cart_view(request):
    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])
        return render(request, "shop/cart.html", {"cart_data" : request.session['cart_data_obj'], "totalcartitems" : len(request.session['cart_data_obj']), 'cart_total_amount' : cart_total_amount})
    else:
        return render(request, "shop/cart.html", {"cart_data" : '', "totalcartitems" : len(request.session['cart_data_obj']), 'cart_total_amount' : cart_total_amount})


def delete_from_cart(request):
    product_id = str(request.GET['id'])
    if 'cart_data_obj' in request.session:
        if product_id in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            del request.session['cart_data_obj'][product_id]
            request.session['cart_data_obj'] = cart_data

    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])

    context = render_to_string("async/cart-list.html",{"cart_data" : request.session['cart_data_obj'], "totalcartitems" : len(request.session['cart_data_obj']), 'cart_total_amount' : cart_total_amount})
    return JsonResponse({"data" : context,"totalcartitems" : len(request.session['cart_data_obj']) })

def checkout(request):
    global order
    cart_total_amount = 0
    total_amount = 0

    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            total_amount += int(item['qty']) * float(item['price'])

            order = CartOrder.objects.create(
                user = request.user,
                price = total_amount
            )

        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])

            cart_order_products = CartOrderItems.objects.create(
                order = order,
                item = item['title'],
                image = item['image'],
                qty = item['qty'],
                price = item['price'],
                total = float(item['qty']) * float(item['price']),
            )
    return render(request, "checkout/checkout.html",{"cart_data" : request.session['cart_data_obj'], "totalcartitems" : len(request.session['cart_data_obj']), 'cart_total_amount' : cart_total_amount})
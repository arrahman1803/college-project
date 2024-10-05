from itertools import count

from django.shortcuts import render
from django.db.models import Count
from shop.models import Product, Category


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

def contact(request):
    return render(request, "shop/index.html")

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

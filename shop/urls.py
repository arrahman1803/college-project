from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('products', views.products, name="products"),
    path('product/<pid>', views.product, name="product_detail"),
    path('category', views.category, name="category"),
    path('category/<cid>', views.category_products, name="category_products"),
    path('search', views.serach, name="search"),
]

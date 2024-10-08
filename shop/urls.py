from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name="home"),
    path('products', views.products, name="products"),
    path('product/<pid>', views.product, name="product_detail"),
    path('category', views.category, name="category"),
    path('category/<cid>', views.category_products, name="category_products"),
    path('search', views.serach, name="search"),
    path('add-to-cart', views.add_to_cart, name="add-to-cart"),
    path('delete-from-cart', views.delete_from_cart, name="delete-from-cart"),
    path('cart', views.cart_view, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('order', views.order, name="order"),
]

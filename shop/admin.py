from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, Category, ProductSizes, ProductColors, ProductImages, CartOrder, CartOrderItems, Address


# Register your models here.

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductSizeAdmin(admin.TabularInline):
    model = ProductSizes

class ProductColorAdmin(admin.TabularInline):
    model = ProductColors

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin, ProductSizeAdmin, ProductColorAdmin]
    list_display = ['title', 'product_image','category','price']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']

class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'price', 'order_date']

class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'item', 'image', 'qty', 'price', 'total']

class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address']

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(CartOrder,CartOrderAdmin)
admin.site.register(CartOrderItems,CartOrderItemsAdmin)
admin.site.register(Address,AddressAdmin)
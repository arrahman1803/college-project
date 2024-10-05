from django.db import models
from django.db.models import SET_NULL
from django.utils.html import mark_safe
from shortuuid.django_fields import ShortUUIDField

from userauths.models import User


# Create your models here.

class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=30, prefix="cat", alphabet="abcdefgh12345")
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category")

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title


class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=30, alphabet="abcdefgh12345")
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category")
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    mrp = models.IntegerField()
    image = models.ImageField(upload_to="images")
    in_stock = models.BooleanField(default=True)
    featured =models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def get_percentage(self):
        new_price = (self.price / self.mrp) * 100
        return new_price

    class Meta:
        verbose_name_plural = "Products"

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

class ProductImages(models.Model):
    images = models.ImageField()
    product = models.ForeignKey(Product,related_name="p_images", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Images"

class ProductSizes(models.Model):
    size = models.CharField(max_length=50)
    product = models.ForeignKey(Product,related_name="p_size", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Sizes"

class ProductColors(models.Model):
    color = models.CharField(max_length=50)
    product = models.ForeignKey(Product,related_name="p_color", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Colors"

class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=99999999999999999, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Cart Order"


class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=99999999999999, decimal_places=2)
    total = models.DecimalField(max_digits=99999999999999, decimal_places=2)

    class Meta:
        verbose_name_plural = "Cart Order Items"

    def order_img(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" /> ' % (self.image))

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    address = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = "Address"
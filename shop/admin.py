from django.contrib import admin

from .models import Category, Customer, Order, Product, Seller

# Register your models here.
admin.site.register(Seller)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Customer)
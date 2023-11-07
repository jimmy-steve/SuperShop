from django.contrib import admin

# Register your models here.
from store.models import Product, Order, Cart

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)
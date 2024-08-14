from django.contrib import admin
from .models import User, Admin, Product, Cart, Order, OrderItem

admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)

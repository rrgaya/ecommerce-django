from django.contrib import admin
from .models import OrderItem, Items, Order


admin.site.register(Items)
admin.site.register(Order)
admin.site.register(OrderItem)

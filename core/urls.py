from django.urls import path
from .views import item_list, checkout, product

app_name="core"

urlpatterns = [
    path('', item_list, name="home"),
    path('checkout/', checkout, name="checkout"),
    path('product/', product, name="product"),
]
from django.urls import path
from .views import HomeList, checkout, ItemDetailView

app_name="core"

urlpatterns = [
    path('', HomeList.as_view(), name="home"),
    path('checkout/', checkout, name="checkout"),
    path('product/<slug>', ItemDetailView.as_view(), name="product"),
]
from django.shortcuts import render
from .models import Items
from django.views.generic import ListView, DetailView

def item_list(request):
    template_name = "home.html"
    context = {
        "items": Items.objects.all()
    }
    return render(request, template_name, context)


def checkout(request):
    return render(request, "checkout.html")


class HomeList(ListView):
    model = Items
    template_name = "home.html"


class ItemDetailView(DetailView):
    model = Items
    template_name = "product.html"


def product(request):
    return render(request, "product.html")
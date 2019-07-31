from django.shortcuts import render
from .models import Items


def item_list(request):
    template_name = "home.html"
    context = {
        "items": Items.objects.all()
    }
    return render(request, template_name, context)


def checkout(request):
    return render(request, "checkout.html")


def product(request):
    return render(request, "product.html")
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Items, Order, OrderItem


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


def add_to_cart(request, slug):
    item = get_object_or_404(Items, slug=slug)
    order_item = OrderItem.objects.create(item=item)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # Check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
    else:
        ordered_data = timezone.now()
        order = Order.objects.create(
            user=request.user,
            ordered_date=ordered_data
        )
        order.items.add(order_item)
    return redirect("core:product", slug=slug)
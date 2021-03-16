from django.shortcuts import render
from blog.models import *

# Create your views here.
from blog.utils import cartData


def dashboard(request):

    shippingOrder = ShippingAddress.objects.all()

    context = {
        'customer':shippingOrder,
    }

    return render(request, 'dashboard/dashboard.html', context)

def customers(request, order):

    orders = OrderItem.objects.all()
    filterOrder = orders.filter(order=order)

    address = ShippingAddress.objects.all()
    filterAddress = address.filter(order=order)

    total = sum([item.get_total for item in filterOrder])

    Items = sum([item.quantity for item in filterOrder])

    context = {
        'filterOrder': filterOrder,
        'filterAddress': filterAddress,
        'total': total,
        'Items': Items,
    }
    return render(request, 'dashboard/orderAndAddress.html', context)
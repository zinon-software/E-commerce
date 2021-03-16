from django.shortcuts import render
from blog.models import *

# Create your views here.

def dashboard(request):
    customer = Customer.objects.all()
    orderTime = Order.objects.all()

    customerCount = customer.count()

    context = {
        'customer':customer,
        'orderTime':orderTime,
        'customerCount': customerCount,
    }

    return render(request, 'dashboard/dashboard.html', context)
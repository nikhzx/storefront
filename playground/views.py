from unicodedata import numeric
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Avg, Min, Max, Sum
from store.models import Order, Product, OrderItem, Customer


# Create your views here.

def say_hello(request):
    # queryset = Product.objects.values_list('title', 'orderitem__product_id').order_by('title').distinct()
    # queryset = Product.objects.filter(inventory = F("unit_price"))
    # queryset = Product.objects.filter(inventory = F("collection__id"))
    # product = Product.objects.filter(unit_price__gte=20)
    # return render(request, 'hello.html', {'name': "Nikhil", "products":list(product), "queryset": list(queryset)})
    # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # queryset = Product.objects.prefetch_related('promotions').all()
    # result = Product.objects.aggregate(count= Count('id'), min_price = Min('unit_price'))
    # queryset = Customer.objects.annotate(orders_count = Count('order'))
    disc_price = ExpressionWrapper(F('unit_price')*0.8, output_field=DecimalField())
    queryset = Product.objects.annotate(discounted_price =disc_price)
    return render(request, 'hello.html', {'name': "Nikhil", "queryset": queryset})
    # return render(request, 'hello.html', {'name': "Nikhil", "result": result})
    # return HttpResponse("Hello World")
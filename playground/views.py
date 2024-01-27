from gc import collect
from typing import Collection
from unicodedata import numeric
from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction
from django.db.models import Q, F, Value, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Avg, Min, Max, Sum
from django.contrib.contenttypes.models import ContentType
from store.models import Order, Product, OrderItem, Customer, Collection
from tags.models import TaggedItem

# @transaction.atomic()
def say_hello(request):
    queryset = Customer.objects.raw("SELECT * FROM store_customer")
    # order = Order()
    # order.customer_id = 1
    # order.save()

    # item = OrderItem()
    # item.order = order
    # item.product_id = -1
    # item.quantity = 1
    # item.unit_price = 10
    # item.save()
    return render(request, 'hello.html', {'result':list(queryset)})

# Create your views here.
# def say_hello(request):
#     collection = Collection.objects.get(pk=14)
#     collection.featured_product = Product(pk=7)
#     collection.save()

#     # object = Collection()
#     # object.title = "Games"
#     # object.featured_product = Product(pk=2)
#     # object.save()
#     # print(object.id)

#     # queryset = TaggedItem.objects.get_tags_for(Product, 1)
#     # result = Product.objects.filter(collection_id=3).aggregate(count = Count('id'), min_price = Min('unit_price'))
#     # print(result)
#     return render(request, 'hello.html', {'name': "Nikhil",})# "result":list(queryset)})

# def say_hello(request):
    # queryset = Product.objects.values_list('title', 'orderitem__product_id').order_by('title').distinct()
    # queryset = Product.objects.filter(inventory = F("unit_price"))
    # queryset = Product.objects.filter(inventory = F("collection__id"))
    # product = Product.objects.filter(unit_price__gte=20)
    # return render(request, 'hello.html', {'name': "Nikhil", "products":list(product), "queryset": list(queryset)})
    # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # queryset = Product.objects.prefetch_related('promotions').all()
    # result = Product.objects.aggregate(count= Count('id'), min_price = Min('unit_price'))
    # queryset = Customer.objects.annotate(orders_count = Count('order'))
    # disc_price = ExpressionWrapper(F('unit_price')*0.8, output_field=DecimalField())
    # queryset = Product.objects.annotate(discounted_price =disc_price)
    # return render(request, 'hello.html', {'name': "Nikhil", "queryset": queryset})
    # return render(request, 'hello.html', {'name': "Nikhil", "result": result})
    # return HttpResponse("Hello World")
from django.contrib import admin

from store.models import *

admin.site.site_header = "Storefront Admin"
admin.site.index_title = "Admin"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price']
    list_editable = ['unit_price']
    list_per_page = 10

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership',]
    ordering = ['first_name', 'last_name']
    list_per_page = 10

# Register your models here.
admin.site.register(Collection)
# admin.site.register(Product, ProductAdmin)

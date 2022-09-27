from django.contrib import admin
from .models.products import Product
from .models.categories import Category
from .models.customers import Customer
#from .models.orders import Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer)
#admin.site.register(Order)
from store.models.category import Category
from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'discount',
        'category'
    ]
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'fname',
        'sname',
        'phone',
        'email',
        'password',
        'confirmpassword'
    ]
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer, CustomerAdmin)

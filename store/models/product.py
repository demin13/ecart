from store.models import category
from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.files import ImageField
from .category import Category


class Product(models.Model):
    name = CharField(max_length=50)
    price = IntegerField(default=0)
    discount = IntegerField(default=0, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=2)
    description = CharField(max_length=200, default='', null=True, blank=True)
    images = ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_all_products():
        queryset = Product.objects.all()
        return queryset

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.objects.all()
from django.db import models
from django.db.models.query import QuerySet

class Category(models.Model):
    name = models.CharField(max_length=100)

    @staticmethod
    def get_all_category():
        queryset = Category.objects.all()
        return queryset

    def __str__(self) -> str:
        return self.name
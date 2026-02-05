from django.contrib import admin
from .models import Status, Product, Category

admin.site.register(Product)
admin.site.register(Status)
admin.site.register(Category)

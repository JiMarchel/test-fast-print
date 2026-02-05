from django.shortcuts import render
from .models import Product


def index(req):
    context = {"products": Product.objects.filter(status__name="bisa dijual")}

    return render(req, "index.html", context)

from functools import wraps

from django.http import HttpResponseForbidden, HttpResponseNotAllowed
from django.shortcuts import render

from .models import Product


def get_sellable_products():
    return Product.objects.filter(status__name="bisa dijual")


def render_partial(request, template, context=None):
    return render(request, template, context or {}).content.decode()


def htmx_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.headers.get("HX-Request"):
            return HttpResponseForbidden("HTMX request required")
        return view_func(request, *args, **kwargs)

    return wrapper


def require_POST(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.method != "POST":
            return HttpResponseNotAllowed(["POST"])
        return view_func(request, *args, **kwargs)

    return wrapper


def require_DELETE(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.method != "DELETE":
            return HttpResponseNotAllowed(["DELETE"])
        return view_func(request, *args, **kwargs)

    return wrapper

from django.http import HttpResponse
from django.shortcuts import render

from .forms import ProductForm
from .models import Product
from .helper import (
    get_sellable_products,
    require_POST,
    require_DELETE,
    render_partial,
    htmx_required,
)


def index(request):
    return render(request, "index.html", {"products": get_sellable_products()})


@htmx_required
def product_form(request):
    return render(request, "partials/product_form.html", {"form": ProductForm()})


@htmx_required
@require_POST
def product_create(request):
    form = ProductForm(request.POST)

    if not form.is_valid():
        return render(request, "partials/product_form.html", {"form": form})

    form.save()

    response_html = "".join(
        [
            render_partial(
                request, "partials/product_form.html", {"form": ProductForm()}
            ),
            render_partial(request, "partials/product_toast.html"),
            render_partial(
                request,
                "partials/product_table.html",
                {"products": get_sellable_products()},
            ),
        ]
    )

    return HttpResponse(response_html)


@htmx_required
def product_delete_confirm(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, "partials/product_delete_confirm.html", {"product": product})


@htmx_required
@require_DELETE
def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()

    response_html = "".join(
        [
            render_partial(
                request,
                "partials/product_table.html",
                {"products": get_sellable_products()},
            ),
            render_partial(request, "partials/product_delete_toast.html"),
        ]
    )

    return HttpResponse(response_html)


@htmx_required
def product_edit_form(request, pk):
    product = Product.objects.get(pk=pk)
    form = ProductForm(instance=product)
    return render(
        request, "partials/product_edit_form.html", {"form": form, "product": product}
    )


@htmx_required
@require_POST
def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    form = ProductForm(request.POST, instance=product)

    if not form.is_valid():
        return render(
            request,
            "partials/product_edit_form.html",
            {"form": form, "product": product},
        )

    form.save()

    response_html = "".join(
        [
            render_partial(
                request,
                "partials/product_table.html",
                {"products": get_sellable_products()},
            ),
            render_partial(request, "partials/product_update_toast.html"),
        ]
    )

    return HttpResponse(response_html)

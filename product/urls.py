from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("product/form/", views.product_form, name="product_form"),
    path("product/create/", views.product_create, name="product_create"),
    path(
        "product/<int:pk>/delete/confirm/",
        views.product_delete_confirm,
        name="product_delete_confirm",
    ),
    path("product/<int:pk>/delete/", views.product_delete, name="product_delete"),
    path("product/<int:pk>/edit/", views.product_edit_form, name="product_edit_form"),
    path("product/<int:pk>/update/", views.product_update, name="product_update"),
]

from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "category", "status"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full",
                    "placeholder": "Nama Produk",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "input input-bordered w-full",
                    "placeholder": "0",
                    "step": "1",
                }
            ),
            "category": forms.Select(attrs={"class": "select select-bordered w-full"}),
            "status": forms.Select(attrs={"class": "select select-bordered w-full"}),
        }
        labels = {
            "name": "Nama Produk",
            "price": "Harga",
            "category": "Kategori",
            "status": "Status",
        }

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is not None and price < 1:
            raise forms.ValidationError("Harga harus lebih dari 0")
        return price

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name and len(name) < 3:
            raise forms.ValidationError("Nama produk minimal 3 karakter")
        return name

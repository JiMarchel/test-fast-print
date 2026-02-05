import requests
from datetime import datetime
import hashlib
from django.core.management.base import BaseCommand
from product.models import Product, Category, Status
from zoneinfo import ZoneInfo


class Command(BaseCommand):
    help = "Ambil data dari API dan simpan ke database"

    def handle(self, *args, **kwargs):
        self.stdout.write("Sedang mengambil data...")

        now = datetime.now(ZoneInfo("Asia/Jakarta"))

        username = f"tesprogrammer{now.strftime('%d%m%y')}C{now.hour}"
        password = f"bisacoding-{now.strftime('%d-%m-%y')}"
        md5_hash = hashlib.md5(password.encode()).hexdigest()

        print(f"Username:{username}\nPassword:{md5_hash}")

        response = requests.post(
            "https://recruitment.fastprint.co.id/tes/api_tes_programmer",
            data={"username": username, "password": md5_hash},
        )

        data_api = response.json()

        if "data" not in data_api:
            self.stdout.write(
                self.style.ERROR(f"Gagal mengambil data. Response: {data_api}")
            )
            return

        for item in data_api["data"]:
            cat_obj, _ = Category.objects.get_or_create(name=item["kategori"])

            stat_obj, _ = Status.objects.get_or_create(name=item["status"])

            Product.objects.update_or_create(
                name=item["nama_produk"],
                defaults={
                    "price": item["harga"],
                    "category": cat_obj,
                    "status": stat_obj,
                },
            )

        self.stdout.write(self.style.SUCCESS("Berhasil mengimpor semua data!"))

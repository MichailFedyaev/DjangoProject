from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Добавление данных из фикстур"

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Добавляем данные из фикстур
        call_command("loaddata", "categories_fixture.json", format="json")
        self.stdout.write(self.style.SUCCESS("Категории загружены из фикстур успешно"))
        call_command("loaddata", "products_fixture.json", format="json")
        self.stdout.write(self.style.SUCCESS("Продукты загружены из фикстур успешно"))

from django.core.management import call_command
from django.core.management.base import BaseCommand

from blog.models import Blog


class Command(BaseCommand):
    help = "Добавление данных из фикстур"

    def handle(self, *args, **kwargs):
        Blog.objects.all().delete()

        # Добавляем данные из фикстур
        call_command("loaddata", "blog_fixture.json", format="json")
        self.stdout.write(self.style.SUCCESS("Продукты загружены из фикстур успешно"))
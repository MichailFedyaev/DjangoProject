from django.http import HttpResponse
from .models import Product, Category
from django.views.generic import ListView, DetailView, TemplateView
from .models import Product


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(DetailView):
    model = Product


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    @staticmethod
    def post(request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(
            f"{name}, указанные Вами телефон и сообщение получены<br>Телефон: {phone}<br>Сообщение: {message}"
        )

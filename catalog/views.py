from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category


def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "home.html", context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f'Спасибо, {name}! Мы получили ваш номер телефона и сообщение.')
    return render(request, 'contacts.html')


def product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}

    return render(request, "product.html", context)

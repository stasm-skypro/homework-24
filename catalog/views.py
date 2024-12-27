"""
Контроллеры, определённые внутри приложения catalog.
"""

from django.shortcuts import render
from catalog.models import Product
from catalog.forms import ContactForm


def home_page(request):
    """
    Определяет отображение страницы home.html.
    """
    recent_products = Product.objects.filter(category__name="Продукты")
    for product in recent_products:
        print("Последние %s товаров:" % len(recent_products))
        print(product)

    return render(request, "home.html", context={"data": recent_products})


def contacts_page(request):
    """
    Определяет отображение страницы contacts.html.
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем данные в таблицу catalog_contacts
            return render(request, "success.html")
    else:
        form = ContactForm()
    return render(request, "contacts.html", {"form": form})


def product_details_controller(request, product_id: int = 1):
    """
    Определяет отображение детализации (характеристик) продукта.
    """
    product = Product.objects.get(id=product_id)
    return render(request, "product_details.html", context={"product": product})

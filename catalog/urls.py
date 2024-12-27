"""
URL configuration for app catalog configuring.
"""

from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home_page, contacts_page, product_details_controller


app_name = CatalogConfig.name

urlpatterns = [
    path("", home_page, name="home.html"),
    path("contacts/", contacts_page, name="contacts.html"),
    path("product_details/<int:product_id>", product_details_controller, name="product_details.html")
]

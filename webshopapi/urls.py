from django.urls import path

from webshopapi.views.products_list_view import ProductsListView

urlpatterns = [
    path(r'products', ProductsListView.as_view(), name='products_list_view'),
]

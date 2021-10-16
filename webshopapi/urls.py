from django.urls import path

from webshopapi.views.product_view import ProductCreateView
from webshopapi.views.products_list_view import ProductsListView

urlpatterns = [
    path(r'products', ProductsListView.as_view(), name='products_list_view'),
    path(r'product', ProductCreateView.as_view(), name='product_create_view'),
]

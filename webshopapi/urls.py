from django.urls import path

from webshopapi.views.product_view import ProductCreateView, ProductView
from webshopapi.views.products_list_view import ProductsListView

urlpatterns = [
    path(r'products', ProductsListView.as_view(), name='products_list_view'),
    path(r'product', ProductCreateView.as_view(), name='product_create_view'),
    path(r'product/<int:pk>', ProductView.as_view(), name='product_get_delete_put_view'),
]

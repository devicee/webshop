from typing import List

from django.http import Http404

from webshopapi.constants import NAME, PRICE
from webshopapi.models import ProductModel


class ProductService:
    @staticmethod
    def list_products() -> List[ProductModel]:
        products = ProductModel.objects.all()
        return products

    @staticmethod
    def post(request: dict) -> ProductModel:
        return ProductModel.objects.create(name=request.get(NAME), price=request.get(PRICE))

    @staticmethod
    def get(pk: int):
        product = ProductModel.objects.filter(pk=pk).first()
        if product:
            return product

        raise Http404
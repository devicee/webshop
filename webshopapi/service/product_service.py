from typing import List

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

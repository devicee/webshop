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

    @staticmethod
    def put(pk: int, request: dict):
        product = ProductModel.objects.filter(pk=pk).first()
        if product:
            for data in request:
                if data:
                    setattr(product, data, request.get(data))
                product.save()

            return product

        raise Http404

    @staticmethod
    def delete(pk: int):
        product = ProductModel.objects.filter(pk=pk).exists()
        if product:
            return ProductModel.objects.filter(pk=pk).delete()

        raise Http404

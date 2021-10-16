from typing import List

from webshopapi.models import ProductModel


class ProductService:
    def list(self) -> List[ProductModel]:
        products = ProductModel.objects.all()
        return products

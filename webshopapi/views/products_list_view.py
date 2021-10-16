from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from webshopapi.serializers.product_serializer import ProductSerializer
from webshopapi.service.product_service import ProductService


class ProductsListView(ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get',]

    def get_queryset(self):
        return None

    def get(self, request, *args, **kwargs):
        products = ProductService().list()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

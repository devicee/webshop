from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from webshopapi.constants import PK
from webshopapi.serializers.product_serializer import ProductSerializer, ProductSerializerPost
from webshopapi.service.product_service import ProductService


class ProductCreateView(ListCreateAPIView):
    serializer_class = ProductSerializerPost
    permission_classes = [AllowAny]
    http_method_names = ['post', ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid() is False:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        product = ProductService.post(request=serializer.validated_data)
        serializer = self.serializer_class(product)

        return Response(serializer.data)


class ProductView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'put', 'delete', ]

    def get_queryset(self):
        return None

    def get(self, request, *args, **kwargs):
        pk = kwargs.get(PK)

        product = ProductService.get(pk=pk)
        serializer = self.serializer_class(product)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get(PK)
        serializer = self.serializer_class(data=request.data, partial=True)

        if serializer.is_valid() is False:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        product = ProductService.put(pk=pk, request=serializer.data)
        serializer = ProductSerializer(product, partial=True)

        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get(PK)

        __ = ProductService.delete(pk=pk)

        return Response()


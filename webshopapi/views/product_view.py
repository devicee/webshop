from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from webshopapi.serializers.product_serializer import ProductSerializer
from webshopapi.service.product_service import ProductService


class ProductCreateView(ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    http_method_names = ['post',]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            product = ProductService.post(request=serializer.validated_data)

            serializer = ProductSerializer(product)

            return Response(serializer.data)

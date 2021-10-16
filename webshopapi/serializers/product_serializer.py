from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(allow_null=False, read_only=True)
    name = serializers.CharField(max_length=100, required=False, allow_null=False)
    price = serializers.DecimalField(decimal_places=2, max_digits=5, required=False, allow_null=False)


class ProductSerializerPost(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=True, allow_null=False)
    price = serializers.DecimalField(decimal_places=2, max_digits=5, required=True, allow_null=False)

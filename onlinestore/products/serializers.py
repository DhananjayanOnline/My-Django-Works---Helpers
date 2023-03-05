from dataclasses import field
from rest_framework import serializers

from products.models import Mobiles

class ProductSerializers(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    brand = serializers.CharField()
    price = serializers.IntegerField()
    specs = serializers.CharField()
    band = serializers.CharField()

class MobileSerializers(serializers.ModelSerializer):
    id = serializers.CharField(read_only = True)
    class Meta:
        model = Mobiles
        fields = '__all__'
        # fields = [
        #     'name',
        #     'brand',
        #     'price',
        #     'specs',
        #     'band'
        # ]

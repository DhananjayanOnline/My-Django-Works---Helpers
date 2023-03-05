from django.shortcuts import render

# Create your views here.

from products.models import Mobiles
from rest_framework.views import APIView
from rest_framework.response import Response
from products.serializers import ProductSerializers, MobileSerializers

class ProductsView(APIView):
    def get(self, request, *args, **kwargs):
        mobiles = Mobiles.objects.all()
        if "brand" in request.query_params:
           mobiles = mobiles.filter(brand=request.query_params.get("brand"))
        if "band" in request.query_params:
            mobiles = mobiles.filter(band=request.query_params.get("band"))
        serialier = MobileSerializers(mobiles, many=True)
        return Response(data=serialier.data)

    def post(self, request, *args, **kwargs):
        # serializer = ProductSerializers(data=request.data)
        # if serializer.is_valid():
        #     Mobiles.objects.create(**serializer.validated_data)
        #     return Response(data=serializer.validated_data)
        # else:
        #     return Response(data=serializer.errors)

        serializer = MobileSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class ProductDetailView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        ob = Mobiles.objects.get(id=id)
        serializer = MobileSerializers(ob)
        return Response(data=serializer.data)
    
    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        Mobiles.objects.get(id=id).delete()
        return Response(data="item removed")

    def put(self, request, *args, **kwargs):
        # id = kwargs.get("id")
        # serializer = ProductSerializers(data=request.data)
        # if serializer.is_valid():
        #     Mobiles.objects.filter(id=id).update(**serializer.validated_data)
        #     return Response(data=serializer.data)
        # else:
        #     return Response(data=serializer.errors)
        
        id = kwargs.get('id')
        mobile = Mobiles.objects.get(id=id)
        serializer = MobileSerializers(data=request.data, instance=mobile)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


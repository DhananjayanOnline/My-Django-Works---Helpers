from django.shortcuts import render


# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response


class GoodMorningView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(data='Good Morning')

class GoodAfternoonView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(data='Good Afternoon')



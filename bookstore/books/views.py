from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book

# Create your views here.

class BookView(APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        serialer = BookSerializer(books, many=True)
        return Response(data=serialer.data)

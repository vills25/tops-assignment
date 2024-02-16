from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializers
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST'])
def BookListAPI(request):
    if request.method == 'GET':
        querySet = Book.objects.all()
        serializer = BookSerializers(querySet, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def BookDetailAPI(request, blog_id):

    try:
        querySet = Book.objects.get(id=blog_id)
    except Book.DoesNotExist:
        return Response({'message': "Data Not Found"},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializers(querySet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = BookSerializers(querySet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        serializer = BookSerializers(querySet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        querySet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
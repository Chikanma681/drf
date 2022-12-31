from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
import json
# Create your views here.

@api_view(['POST','GET'])
def books(request):
    if request.method == "POST":
        return Response((request.body).decode("utf-8"))
    author = request.GET.get('author')
    print(request.data)
    if (author):
        return Response({"message":"list of the books by "+author},status.HTTP_200_OK)
class Orders():
    @staticmethod
    @api_view
    def listOrders(request):
        return Response({'message':'list of orders'}, 200)


class BookView(APIView):
    def get(self, request, pk):


        return Response({
            "message":"single book with id "+ str(pk)}, status.HTTP_200_OK
     )
    def put (self, request, pk):
        return Response ({"title":request.data.get('title')}, status.HTTP_200_OK)


# class Book(APIView):
#     def get(self,request, pk):
#         return Response({"message":"single book with id "+str(pk)},status.HTTP_201_CREATED)

# you can use viewsets if you want
# Class BookView(viewsets.ViewSet):
# 	def list(self, request):
#     	return Response({"message":"All books"}, status.HTTP_200_OK)
# 	def create(self, request):
#     	return Response({"message":"Creating a book"}, status.HTTP_201_CREATED)
# 	def update(self, request, pk=None):
#     	return Response({"message":"Updating a book"}, status.HTTP_200_OK)
# 	def retrieve(self, request, pk=None):
#     	return Response({"message":"Displaying a book"}, status.HTTP_200_OK)
# 	def partial_update(self, request, pk=None):
#         return Response({"message":"Partially updating a book"}, status.HTTP_200_OK)
# 	def destroy(self, request, pk=None):
#     	return Response({"message":"Deleting a book"}, status.HTTP_200_OK)
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
import json
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
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


# class MenuItemsView(generics.ListCreateAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer

@api_view(['GET','POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all() # select_related from the SQL queries in one call
        serialized_items = MenuItemSerializer(items, many= True) # many = True is essential when transforming a list to JSON data
        return Response(serialized_items.data)

    if request.method == 'POST':
        serializer = MenuItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        serializer.save()
        return Response(serializer.data)

@api_view()
def single_item(request,id):
    # item = MenuItem.objects.get(pk=id) #NORMAL GET WITHOUT CUSTOM 404 PAGE
    item = get_object_or_404(MenuItem,pk=id)
    serialized_item = MenuItemSerializer(item) # many = True is essential when transforming a list to JSON data
    return Response(serialized_item.data)

# class SingleMenuItenView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer

##
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
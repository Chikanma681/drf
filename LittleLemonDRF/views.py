from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes,throttle_classes
from rest_framework.views import APIView
from rest_framework import generics
import json
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from django.core.paginator import Paginator, EmptyPage
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttle import TenCallsPerMinute
from rest_framework.permissions import IsAdminUser
# Create your views here.

from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group

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
        category_name = request.query_params.get('category') #category name
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')

        #Implementing pagination
        perpage = request.query_params.get('perpage',default=2)
        page = request.query_params.get('page',default=1)

        paginator = Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items=[]

        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price__lte=to_price) #equals to also works here
        if search:
            items = items.filter(title__istartswith=search)
        if ordering: #to call descending order you can do ?ordering=-(field)
            items = items.order_by(ordering)
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

@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({
        "message":"Some secret message"
    })

@api_view()
@permission_classes
def manager_view(request):
    return Response({
        "message":"Only Manager Should See This"
    })

@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({"message":"Only Manager should see this"})
    else:
        return Response({
            "message":"You are not authorized"
        },403)


@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({
        "message":"succesful"
    })

@api_view()
@permission_classes([IsAuthenticated])
# @throttle_classes([UserRateThrottle])
@throttle_classes([TenCallsPerMinute])
def throttle_check_auth(request):
    return Response({
        "message":"message for the logged in users only"
    })


@api_view(['POST'])
@permission_classes([IsAdminUser])
def managers(request):
    username = request.data['username']
    if username:
        user = get_object_or_404(user, username=username)
        managers = Group.objects.get(name="Manager")
        if request.method == 'POST':
            managers.user_set.add(user)
        if request.method == 'DELETE':
            managers.user_set.remove(user)
        return Response({
            "message":"ok"
        })
    return Response({
        "message":"error"
    },status.HTTP_400_BAD_REQUEST)


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
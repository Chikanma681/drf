from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books),
    path('orders/', views.Orders.listOrders),
    path('books/<int:pk>',views.BookView.as_view())
]


# for viewsets
# urlpatterns = [
# 	path('books', views.BookView.as_view(
#     	{
#         	'get': 'list',
#         	'post': 'create',
#     	})
# 	),
#     path('books/<int:pk>',views.BookView.as_view(
#     	{
#         	'get': 'retrieve',
#         	'put': 'update',
#         	'patch': 'partial_update',
#         	'delete': 'destroy',
#     	})
# 	)
# ]
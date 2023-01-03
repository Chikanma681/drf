from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books),
    path('orders/', views.Orders.listOrders),
    # path('books/<int:pk>',views.BookView.as_view()),
    path('books/<int:pk>/',views.BookView.as_view()),

    # path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/', views.menu_items),
    # path('menu-items/<int:pk>',views.SingleMenuItenView.as_view())# class based
    path('menu-items/<int:id>/',views.single_item)# function based

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
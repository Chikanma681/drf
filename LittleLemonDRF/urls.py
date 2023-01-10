from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('books/', views.books),
    path('orders/', views.Orders.listOrders),
    # path('books/<int:pk>',views.BookView.as_view()),
    path('books/<int:pk>/',views.BookView.as_view()),

    # path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/', views.menu_items),
    # path('menu-items/<int:pk>',views.SingleMenuItenView.as_view())# class based
    path('menu-items/<int:id>/',views.single_item),# function based
    path('secret',views.secret),
    path('api-token-auth/', obtain_auth_token),
    path('manager-view/',views.manager_view),
    path('throttle-check',views.throttle_check),
    path('throttle-check-auth', views.throttle_check_auth),
    path('groups/manager/users',views.manager)

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
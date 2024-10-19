from django.urls import path
from .views import MenuItemsView, SingleMenuItemView, index, msg# Import views from the current app
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', index, name='index'),  # Route for the index view
    path('menu/', MenuItemsView.as_view(), name='menu-items-list'), 
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('message/', msg),
    path('api-token-auth/', obtain_auth_token)
    
]

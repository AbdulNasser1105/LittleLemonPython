"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include  # Import include for including other URL configurations
from rest_framework.routers import DefaultRouter
from restaurant.views import BookingViewSet, MenuItemViewSet

router = DefaultRouter()
router.register(r'tables', BookingViewSet, basename='booking')
router.register(r'menu-items', MenuItemViewSet, basename='menu-items')

urlpatterns = [
    path('restaurant/booking/', include(router.urls)),  # Include the router's URLs
    path('admin/', admin.site.urls),  # URL route for the admin interface
    path('restaurant/', include('restaurant.urls')), # Corrected syntax for including the restaurant app URLs
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)), 
]

from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.index, name='index'),
    path('menu-items/', views.MenuItemsView.as_view(), name="menu-list"),  
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name="menu-detail"),  
]

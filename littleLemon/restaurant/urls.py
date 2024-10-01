from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu-items/', views.MenuItemsView.as_view(), name="menu-list"),  # Changed name for clarity
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name="menu-detail"),  # Added trailing slash
]

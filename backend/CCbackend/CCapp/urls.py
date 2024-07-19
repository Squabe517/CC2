from django.urls import path
from . import views

urlpatterns = [
    path('menus/', views.menu, name='menu'),
    path('menus/<uuid:pk>/', views.menu_item, name='menu_item'),
    path('menus/add/', views.add_menu_item, name='add_menu_item'),
]

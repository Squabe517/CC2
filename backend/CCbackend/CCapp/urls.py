from django.urls import path
from . import views

urlpatterns = [
    path('menus/', views.get_menus, name='get_menus'),
    path('menus/<uuid:pk>', views.get_menu, name="get_menu"),
    path('menus/add/', views.add_menu, name='add_menu'),
    path('menu/<uuid:pk>/delete/', views.menu_delete, name='menu_delete'),
    path('menus/<uuid:pk>/add_category/', views.add_category, name='add_category'),
    path('menus/<uuid:pk>/add_item/', views.add_menu_item, name='add_item'),
]

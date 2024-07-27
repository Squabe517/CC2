from django.urls import path
from . import views

urlpatterns = [
    path('menus/', views.get_menus, name='get_menus'),
    path('menus/<uuid:pk>', views.get_menu, name="get_menu"),
    path('menus/add/', views.add_menu, name='add_menu'),
    path('menu/<uuid:pk>/delete/', views.menu_delete, name='menu_delete'),
]

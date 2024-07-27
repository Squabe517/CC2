from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Menu
from .forms import ItemForm, MenuForm


def get_menus(request):
    
    menus = Menu.objects.all()
    return render(request, 'menus.html', {'menus': menus})

def get_menu(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    
    return render(request, 'menu.html', {'menu': menu})

def add_menu(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_menus')
    else:
        form = MenuForm()
    return render(request, 'add_menu.html', {'form': form})

def menu_delete(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    
    if request.method == 'POST':
        menu.delete()
        return redirect('get_menus')  # Redirect to a list of menus or another appropriate view

    return render(request, 'menu_confirm_delete.html', {'menu': menu})
        

def item(request):

    items = Item.objects.all()
    return render(request, 'menu.html', {'items': items})

def menu_item(request, pk):

    item = get_object_or_404(Item, pk=pk)
    return render(request, 'menu_item.html', {'item': item})

def add_menu_item(request):

    if request.method == "POST":
        form = ItemForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('menu')  # Redirect to the menu list view after saving
    else:
        form = ItemForm()
    return render(request, 'add_menu_item.html', {'form': form})

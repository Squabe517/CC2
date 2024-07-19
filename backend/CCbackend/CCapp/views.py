from django.shortcuts import render, get_object_or_404, redirect
from .models import Menu
from .forms import MenuForm

def menu(request):
    items = Menu.objects.all();
    return render(request, 'menu.html', {'items' : items})

def menu_item(request, pk):
    item = get_object_or_404(Menu, pk=pk)
    return render(request, 'menu_item.html', {'item' : item})

def add_menu_item(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')  # Redirect to the menu list view after saving
    else:
        form = MenuForm()
    return render(request, 'add_menu_item.html', {'form': form})
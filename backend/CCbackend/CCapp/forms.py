from django import forms
from .models import Item, Menu

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'available']
        
class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name']

from django import forms
from .models import Item, Menu, Category

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'available', 'category']
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
        
class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        
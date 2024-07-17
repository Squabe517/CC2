from django.contrib import admin
from .models import MyModel, User

# Register your models here.
admin.site.register(MyModel)
admin.site.register(User)
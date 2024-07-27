from django.contrib import admin
from .models import (
    Analytics,
    Item,
    ItemAnalytics,
    ItemModifier,
    Menu,
    Modifier,
    ModifierCategory,
    Order,
    OrderItem,
    OrderItemModifier,
    Payment,
    User
)

@admin.register(Analytics)
class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'user', 'action', 'timestamp')
    search_fields = ('action',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'available')
    search_fields = ('name',)
    list_filter = ('available',)

@admin.register(ItemAnalytics)
class ItemAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'action', 'count', 'timestamp')
    search_fields = ('action',)

@admin.register(ItemModifier)
class ItemModifierAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'modifier')

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'item')
    search_fields = ('name',)

@admin.register(Modifier)
class ModifierAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'additional_price')
    search_fields = ('name',)

@admin.register(ModifierCategory)
class ModifierCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'status', 'created_at', 'updated_at')
    search_fields = ('status',)
    list_filter = ('status',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'item', 'quantity', 'price')

@admin.register(OrderItemModifier)
class OrderItemModifierAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_item', 'modifier')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'amount', 'payment_method', 'status', 'created_at')
    search_fields = ('status', 'payment_method')
    list_filter = ('status', 'payment_method')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_admin')
    search_fields = ('username', 'email')
    list_filter = ('is_admin',)

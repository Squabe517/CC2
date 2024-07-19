from django.contrib import admin
from .models import (
    Analytics, Menu, MenuAnalytics, MenuModifier, Modifier, ModifierCategory,
    Order, OrderItem, OrderItemModifier, Payment, User, AuthGroup,
    AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups,
    AuthUserUserPermissions, DjangoAdminLog, DjangoContentType,
    DjangoMigrations, DjangoSession
)

admin.site.register(Analytics)
admin.site.register(Menu)
admin.site.register(MenuAnalytics)
admin.site.register(MenuModifier)
admin.site.register(Modifier)
admin.site.register(ModifierCategory)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderItemModifier)
admin.site.register(Payment)
admin.site.register(User)
admin.site.register(AuthGroup)
admin.site.register(AuthGroupPermissions)
admin.site.register(AuthPermission)
admin.site.register(AuthUser)
admin.site.register(AuthUserGroups)
admin.site.register(AuthUserUserPermissions)
admin.site.register(DjangoAdminLog)
admin.site.register(DjangoContentType)
admin.site.register(DjangoMigrations)
admin.site.register(DjangoSession)

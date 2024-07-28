import uuid
from django.db import models


class Analytics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey('Order', models.DO_NOTHING, related_name='analytics', null=True, blank=True)
    user = models.ForeignKey('User', models.DO_NOTHING, related_name='analytics', null=True, blank=True)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField()

    class Meta:
        db_table = 'Analytics'

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'Category'

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items', null=True, blank=True)

    class Meta:
        db_table = 'Item'


class ItemAnalytics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(Item, models.DO_NOTHING, related_name='item_analytics', null=True, blank=True)
    action = models.CharField(max_length=255)
    count = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        db_table = 'ItemAnalytics'


class ItemModifier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(Item, models.DO_NOTHING, related_name='item_modifiers', null=True, blank=True)
    modifier = models.ForeignKey('Modifier', models.DO_NOTHING, related_name='item_modifiers', null=True, blank=True)

    class Meta:
        db_table = 'ItemModifier'


class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    items = models.ManyToManyField(Item, related_name='menus')
    categories = models.ManyToManyField(Category, related_name='menus')

    class Meta:
        db_table = 'Menu'


class Modifier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey('ModifierCategory', models.DO_NOTHING, related_name='modifiers', null=True, blank=True)
    name = models.CharField(max_length=255)
    additional_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Modifier'


class ModifierCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'ModifierCategory'


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('User', models.DO_NOTHING, related_name='orders', null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'Order'


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, models.DO_NOTHING, related_name='order_items', null=True, blank=True)
    item = models.ForeignKey(Item, models.DO_NOTHING, related_name='order_items', null=True, blank=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'OrderItem'


class OrderItemModifier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_item = models.ForeignKey(OrderItem, models.DO_NOTHING, related_name='order_item_modifiers', null=True, blank=True)
    modifier = models.ForeignKey(Modifier, models.DO_NOTHING, related_name='order_item_modifiers', null=True, blank=True)

    class Meta:
        db_table = 'OrderItemModifier'


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, models.DO_NOTHING, related_name='payments', null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'Payment'


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    is_admin = models.BooleanField()

    class Meta:
        db_table = 'User'
        

        
        

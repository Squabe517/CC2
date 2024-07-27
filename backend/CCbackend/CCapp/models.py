import uuid
from django.db import models


class Analytics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey('Order', models.DO_NOTHING, related_name='analytics')
    user = models.ForeignKey('User', models.DO_NOTHING, related_name='analytics')
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Analytics'


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'Item'


class ItemAnalytics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(Item, models.DO_NOTHING, related_name='item_analytics')
    action = models.CharField(max_length=255)
    count = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ItemAnalytics'


class ItemModifier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(Item, models.DO_NOTHING, related_name='item_modifiers')
    modifier = models.ForeignKey('Modifier', models.DO_NOTHING, related_name='item_modifiers')

    class Meta:
        managed = False
        db_table = 'ItemModifier'


class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    item = models.ForeignKey(Item, models.DO_NOTHING, related_name='menus', null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'Menu'


class Modifier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey('ModifierCategory', models.DO_NOTHING, related_name='modifiers')
    name = models.CharField(max_length=255)
    additional_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'Modifier'


class ModifierCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ModifierCategory'


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('User', models.DO_NOTHING, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Order'


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, models.DO_NOTHING, related_name='order_items')
    item = models.ForeignKey(Item, models.DO_NOTHING, related_name='order_items')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'OrderItem'


class OrderItemModifier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_item = models.ForeignKey(OrderItem, models.DO_NOTHING, related_name='order_item_modifiers')
    modifier = models.ForeignKey(Modifier, models.DO_NOTHING, related_name='order_item_modifiers')

    class Meta:
        managed = False
        db_table = 'OrderItemModifier'


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, models.DO_NOTHING, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Payment'


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    is_admin = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'User'

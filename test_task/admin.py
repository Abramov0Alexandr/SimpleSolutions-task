from django.contrib import admin

from test_task.models import Item, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price',)
    list_display_links = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id',)
    filter_horizontal = ('order',)

from rest_framework import serializers

from test_task.models import Order
from test_task.serializers import ItemSerializer


class OrderSerializer(serializers.ModelSerializer):

    order_id = serializers.IntegerField(source='id', read_only=True)
    items_in_order = ItemSerializer(source='order', required=False, read_only=True, many=True)

    class Meta:
        model = Order
        fields = ('order_id', 'items_in_order',)

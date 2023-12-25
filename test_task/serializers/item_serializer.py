from rest_framework import serializers

from test_task.models import Item


class ItemSerializer(serializers.ModelSerializer):

    item_id = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Item
        fields = ('item_id', 'name', 'description', 'price')

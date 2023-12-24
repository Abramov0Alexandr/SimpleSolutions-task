from rest_framework import serializers

from test_task.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        models = Item
        fields = '__all__'

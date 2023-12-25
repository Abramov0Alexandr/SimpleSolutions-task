from rest_framework import generics

from .models import Item
from .models import Order
from .serializers.item_serializer import ItemSerializer
from .serializers.order_serializer import OrderSerializer


class ItemListView(generics.ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

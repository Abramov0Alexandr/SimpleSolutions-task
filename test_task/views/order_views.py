from rest_framework import generics

from test_task.models import Order
from test_task.serializers.order_serializer import OrderSerializer


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

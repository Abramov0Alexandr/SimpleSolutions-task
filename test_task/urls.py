from django.urls import path
from .apps import TestTaskConfig
from .views import ItemListView, OrderListView


app_name = TestTaskConfig.name


urlpatterns = [
    path('item-list/', ItemListView.as_view(), name='item_list'),
    path('order-list/', OrderListView.as_view(), name='order_list'),
]

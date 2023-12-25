from django.urls import path

from .apps import TestTaskConfig
from .views.item_views import ItemListView, StripeSessionRetrieveView, ItemDetailView
from .views.order_views import OrderListView

app_name = TestTaskConfig.name

urlpatterns = [
    path('item-list/', ItemListView.as_view(), name='item_list'),
    path('order-list/', OrderListView.as_view(), name='order_list'),
    path('buy/<int:pk>/', StripeSessionRetrieveView.as_view(), name='stripe_session_retrieve'),
    path('item-retrieve/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
]

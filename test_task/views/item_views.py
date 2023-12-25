import os

import stripe
from django.shortcuts import redirect
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from test_task.models import Item
from test_task.serializers.item_serializer import ItemSerializer


class ItemListView(generics.ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class ItemDetailView(generics.RetrieveAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class StripeSessionRetrieveView(APIView):
    STRIPE_API_KEY = os.getenv('STRIPE_API_KEY')

    def get(self, request, pk):

        try:
            item = Item.objects.get(pk=pk)

        except Item.DoesNotExist:
            return Response(
                {
                    'error': 'Item not found',
                    'status': status.HTTP_404_NOT_FOUND
                }
            )

        stripe.api_key = self.STRIPE_API_KEY

        try:
            session = stripe.checkout.Session.create(
                line_items=[
                    {
                        "price_data": {
                            "currency": "rub",
                            "unit_amount_decimal": item.price * 100,
                            "product_data": {"name": item.name},
                        },
                        "quantity": 1,
                    },
                ],
                mode="payment",
                success_url=f'http://127.0.0.1:8000/api/item-retrieve/{item.pk}',
            )
            return redirect(session.url)

        except stripe.error.StripeError as e:
            return Response(
                {
                    'message': 'Something went wrong when creating stripe checkout session',
                    'error': f'{e}',
                    'status': status.HTTP_500_INTERNAL_SERVER_ERROR
                }
            )

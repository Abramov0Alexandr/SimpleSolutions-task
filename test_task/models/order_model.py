from django.db import models


class Order(models.Model):
    order = models.ManyToManyField('Item', related_name='item_order')

    objects = models.Manager()

    class Meta:
        ordering = ('pk',)

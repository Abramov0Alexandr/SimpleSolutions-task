from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(**NULLABLE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name} {self.price}'

    class Meta:
        ordering = ('pk',)

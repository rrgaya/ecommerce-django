from django.db import models
from django.conf import settings


class Items(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Item"


class OrderItem(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)

    def __str__(self):
        return self.item

    class Meta:
        verbose_name = "Ordem Item"
        verbose_name_plural = "Ordem Item"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Order"
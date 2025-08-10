from django.db import models

from core.models import BaseModel

from apps.pizza_shop.models import PizzaShopModel


class PizzaModel(BaseModel):
    class Meta:
        db_table = 'pizza'
    name = models.CharField(max_length=20)
    size = models.IntegerField()
    price = models.FloatField()
    pizza_shop = models.ForeignKey(PizzaShopModel,on_delete=models.CASCADE, related_name='pizzas' )


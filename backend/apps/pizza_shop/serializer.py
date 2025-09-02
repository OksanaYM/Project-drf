from rest_framework import serializers

from backend.apps.pizza.serializer import PizzaSerializer
from backend.apps.pizza_shop.models import PizzaShopModel


class PizzaShopSerializer(serializers.ModelSerializer):
    pizzas = PizzaSerializer(many=True, read_only=True)
    class Meta:
        model = PizzaShopModel
        fields = ('id', 'name', 'pizzas')
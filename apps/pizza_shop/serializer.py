from rest_framework import serializers

from apps.models import PizzaShopModel
from apps.pizza.serializer import PizzaSerializer


class PizzaShopSerializer(serializers.ModelSerializer):
    pizzas = PizzaSerializer(many=True, read_only=True)
    class Meta:
        model = PizzaShopModel
        fields = ('id', 'name', 'pizzas')
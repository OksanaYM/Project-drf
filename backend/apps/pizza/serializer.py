from rest_framework import serializers

from apps.pizza.models import PizzaModel


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaModel
        fields = ('id', 'name', 'size', 'price', 'day', 'created_at', 'updated_at')

    def validate_price(self, price):
        if price <= 0:
            raise serializers.ValidationError('Price must be greater than 0')
        return price
    def create(self, validated_data):
        return PizzaModel.objects.create(**validated_data, pizza_shop_id=1)

class PizzaPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaModel
        fields = ('photo', )
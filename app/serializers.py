from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'quantity', 'thumbnail']

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Назва повинна містити щонайменше 3 символи.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Ціна повинна бути більше 0.")
        return value

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Кількість не може бути від'ємною.")
        return value
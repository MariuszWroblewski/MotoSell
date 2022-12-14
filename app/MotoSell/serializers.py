from rest_framework import serializers
from .models import *
from datetime import date


class OfferSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Offer
        fields = ['id', 'title', 'description', 'category', 'brand', 'model',
                 'production_year', 'mileage', 'capacity', 'power', 'fuel', 'user',
                 'image', 'add_date', 'pub_date', 'is_pub', 'is_deleted']

    def create(self, validated_data):
        request = self.context.get('request')
        instance = self.Meta.model(**validated_data)
        instance.user = request.user
        instance.save()
        return instance

    def validate_production_year(self, production_year):
        if production_year > date.today().year or production_year < 1800:
            raise serializers.ValidationError('Błedna data produkcji. Data nie może być wcześniejsza'
                                              ' niż 1800 rok i pożniejsza niż obecny')
        return production_year

    def validate_mileage(self, mileage):
        if mileage < 0:
            raise serializers.ValidationError('Błędny przebieg. Podaj poprawną wartość')
        return mileage

    def validate_capacity(self, capacity):
        if capacity < 0:
            raise serializers.ValidationError('Błędna pojemność. Podaj poprawną wartość')
        return capacity

    def validate_power(self, power):
        if power < 0:
            raise serializers.ValidationError('Błędna moc. Podaj poprawną wartość')
        return power

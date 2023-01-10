from rest_framework import serializers
from .models import Category, Food, Table, Event, BookTable


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class BookTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTable
        fields = '__all__'

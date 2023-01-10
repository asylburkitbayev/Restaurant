from rest_framework.viewsets import ModelViewSet
from .models import Category, Food, Table, Event, BookTable
from .serializers import CategorySerializer, FoodSerializer, TableSerializer, EventSerializer, BookTableSerializer


class TableModelViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FoodModelViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class EventModelViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class BookTableModelViewSet(ModelViewSet):
    queryset = BookTable.objects.all()
    serializer_class = BookTableSerializer

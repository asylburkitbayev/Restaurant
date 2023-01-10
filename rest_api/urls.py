from rest_framework.routers import DefaultRouter
from .views import CategoryModelViewSet, FoodModelViewSet, TableModelViewSet, EventModelViewSet, BookTableModelViewSet

routers = DefaultRouter()

routers.register('category', CategoryModelViewSet)
routers.register('food', FoodModelViewSet)
routers.register('table', TableModelViewSet)
routers.register('event', EventModelViewSet)
routers.register('booktable', BookTableModelViewSet)


urlpatterns = routers.urls

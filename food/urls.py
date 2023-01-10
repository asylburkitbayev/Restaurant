from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu', views.menu, name='menu'),
    path('menu/category/<id>', views.menu_category, name='menu_id'),
    path('booktable', views.booktable, name='booktable'),
    path('contact', views.contact, name='contact'),
    path('event', views.event, name='Event')
]
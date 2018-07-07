from django.urls import path
from zomato import views

urlpatterns = [
path('zomato', views.search, name='search'),
        ]
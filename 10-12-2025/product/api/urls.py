from django.urls import path
from .views import products

urlpatterns = [
    path('product/', products),
]
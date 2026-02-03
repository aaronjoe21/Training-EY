from django.urls import path
from .views import vehicle

urlpatterns = [
    path('vehicle/', vehicle),
]
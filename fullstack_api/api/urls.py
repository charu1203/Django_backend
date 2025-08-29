from django.urls import path
from .views import bfhl

urlpatterns = [
    path('bfhl', bfhl),
]

# apmtest/urls.py
from django.urls import path
from .views import homeTestView

urlpatterns = [
    path('', homeTestView, name='home')
]
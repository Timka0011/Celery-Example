from django.contrib import admin
from django.urls import path
from .views import index, success

urlpatterns = [
    path('', index, name="index"),
    path('sucess/', success, name="sources"),
]

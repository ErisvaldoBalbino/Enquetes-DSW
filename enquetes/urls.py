from django.contrib import admin
from django.urls import path, include
from enquetes import views

urlpatterns = [
    path('', views.index, name='index-enquetes'),
]
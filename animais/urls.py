from django.contrib import admin
from django.urls import path, include
from animais.views import index

urlpatterns = [    
    path('', index),
]

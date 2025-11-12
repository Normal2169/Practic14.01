from django.urls import path
from Oleg import views

urlpatterns = [
    path('', views.index),
]

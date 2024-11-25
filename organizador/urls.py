from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_organizador, name='home_organizador'),
]
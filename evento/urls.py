from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('buy_ticket/', views.buy_ticket, name='buy_ticket'),
    path('termos/', views.termos, name='termos'),
    path('meus_pagamentos/', views.meus_pagamentos, name='meus_pagamentos'),
]
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Pagamento
from lutadores.models import Lutas
import time


def home(request):
    lutas_dia1 = Lutas.objects.filter(dia_luta='Dia 1')
    lutas_dia2 = Lutas.objects.filter(dia_luta='Dia 2')
    return render(request, 'home.html', {'lutas_dia1': lutas_dia1, 'lutas_dia2': lutas_dia2})

def buy_ticket(request):
    if request.method == "GET":
        return render(request, 'buy_ticket.html')

    elif request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('login')

        tipo_ingresso = request.POST.get('tipo_ingresso')
        quantidade = int(request.POST.get('quantidade'))
        valor_final = float(request.POST.get('valor_final').replace('R$', '').strip())

        pagamento = Pagamento.objects.create(
            usuario=request.user,
            data_pagamento=timezone.now().date(),
            hora_pagamento=timezone.now().time(),
            status_pagamento='Aguardando Pagamento',
            tipo_ingresso=tipo_ingresso,
            quantidade=quantidade,
            valor_final=valor_final
        )
        pagamento.save()
        
        messages.add_message(request, messages.SUCCESS, 'Pagamento registrado com sucesso! Aguardando confirmação.')
        time.sleep(3)
        return redirect('buy_ticket')
    

def termos(request):
    if request.method == "GET":
        return render(request, 'termos.html')
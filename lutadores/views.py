from lutadores.models import Lutadores
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from evento.models import Pagamento
from django.utils import timezone

@login_required(login_url = '/auth/login')
def portal(request):
    if request.method == "GET":
        if request.user.lutador:
            # Lógica para lutadores
            return render(request, 'portal.html')
        else:
            # Lógica para não lutadores
            return render(request, 'cadastro_lutador.html')    
        """lutadores = Lutadores.objects.all()
        return render(request, 'portal.html', {'lutadores': lutadores})"""
    
def cadastro_lutador(request):
    if request.method == "GET":
        return render(request, 'cadastro_lutador.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        data_nascimento = request.FILES.get('data_nascimento')
        peso = request.POST.get('peso')
        nivel = request.POST.get('nivel')
        equipe = request.POST.get('equipe')
        coach = request.POST.get('coach')
        contato = request.POST.get('contato')

        lutadores = Lutadores(
            nome = nome,
            data_nascimento = data_nascimento,
            peso = peso,
            nivel = nivel,
            equipe = equipe,
            coach = coach,
            contato = contato,
        )
        lutadores.save()

        user = request.user
        user.lutador = True
        user.save()

        messages.add_message(request, messages.SUCCESS, 'Lutador cadastrado com sucesso!')

        tipo_ingresso = 'Lutador'
        valor_final = 180.00
        quantidade = 1

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
        
        return redirect('portal')
    

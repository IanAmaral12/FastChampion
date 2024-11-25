from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Pagamento(models.Model):
    STATUS_CHOICES = [
        ('Aguardando Pagamento', 'Aguardando Pagamento'),
        ('Pagamento Aprovado', 'Pagamento Aprovado'),
        ('Pagamento Expirado', 'Pagamento Expirado'),
    ]

    TIPO_INGRESSO_CHOICES = [
        ('Dia 1', 'Dia 1'),
        ('Dia 1 VIP', 'Dia 1 VIP'),
        ('Dia 2', 'Dia 2'),
        ('Dia 2 VIP', 'Dia 2 VIP'),
        ('Lutador', 'Lutador'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_pagamento = models.DateField(default=timezone.now)
    hora_pagamento = models.TimeField(default=timezone.now)
    status_pagamento = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Aguardando Pagamento')
    tipo_ingresso = models.CharField(max_length=20, choices=TIPO_INGRESSO_CHOICES)
    quantidade = models.PositiveIntegerField()
    valor_final = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return f"{self.usuario.username} - {self.tipo_ingresso} - {self.status_pagamento}"
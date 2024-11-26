from django.db import models

# Crie seus modelos aqui.
class Lutadores(models.Model):
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField(null=True, blank=True)
    peso = models.FloatField(max_length=50)
    nivel = models.CharField(max_length=50)
    equipe = models.CharField(max_length=50)
    coach = models.CharField(max_length=50)
    contato = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Lutas(models.Model):
    DIA_CHOICES = [
        ('Dia 1', 'Dia 1'),
        ('Dia 2', 'Dia 2'),
    ]
    dia_luta = models.CharField(max_length=5, choices=DIA_CHOICES)
    hora_luta = models.TimeField()
    local_luta = models.CharField(max_length=100)
    lutador1 = models.ForeignKey(Lutadores, related_name='luta_lutador1', on_delete=models.CASCADE)
    lutador2 = models.ForeignKey(Lutadores, related_name='luta_lutador2', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.lutador1} vs {self.lutador2} - {self.dia_luta} {self.hora_luta}"
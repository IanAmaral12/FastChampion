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
from tkinter import CASCADE
from django.db import models
from usuarios.models import User

# Create your models here.

class Projeto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(verbose_name='Descrição')
    membros = models.ManyToManyField(User, related_name='membros')

    def __str__(self):
        return '{}'.format(self.nome)
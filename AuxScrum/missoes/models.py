from django.db import models

class Missao(models.Model):
    nome = models.CharField(max_length=128)
    feita = models.BooleanField(default=False)

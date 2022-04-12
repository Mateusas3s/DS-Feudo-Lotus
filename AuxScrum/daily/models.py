from tkinter import CASCADE
from django.db import models
from datetime import date
from usuarios.models import User
from cadastros.models import Projeto

class dateDaily(models.Model):
    date =  models.DateField(default=date.today, blank=True)
    user = models.CharField(max_length=50)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(str(self.date), self.user)

class formularioDaily(models.Model):
    date_daily = models.ForeignKey(dateDaily, on_delete=models.CASCADE)
    q1 = models.CharField(max_length=2500)
    q2 = models.CharField(max_length=2500)
    q3 = models.CharField(max_length=2500)

    def __str__(self):
        return 'Daily do dia {}'.format(str(self.date_daily))
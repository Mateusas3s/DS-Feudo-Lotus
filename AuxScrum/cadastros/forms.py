from django import forms
from django.forms import ModelForm
from . models import Projeto


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'membros']

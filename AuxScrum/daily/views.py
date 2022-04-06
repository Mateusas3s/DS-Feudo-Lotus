from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import formDaily

class dailyCreate(CreateView):
    model= formDaily
    fields = [
        'q1',
        'q2',
        'q3',
    ]
    template_name = 'daily/relatorio_daily.html'
    reverse_lazy = 'daily'

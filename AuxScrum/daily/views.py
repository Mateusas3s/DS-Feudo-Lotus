from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .models import formDaily
from django.urls import reverse_lazy

class dailyCreate(CreateView):
    model= formDaily
    fields = [
        'q1',
        'q2',
        'q3',
        'date',
    ]
    template_name = 'daily/relatorio_daily.html'
    succsess_url = reverse_lazy('home')

#### Update View ####
class dailyUpdate(UpdateView):
    model= formDaily
    fields = [
        'q1',
        'q2',
        'q3',
        'date',
    ]
    template_name = 'daily/relatorio_daily.html'
    succsess_url = reverse_lazy('home')

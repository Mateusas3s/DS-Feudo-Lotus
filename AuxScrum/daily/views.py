from audioop import reverse
from dataclasses import fields
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView 
from .models import dateDaily, formularioDaily

#página da daily
class daily_Pag(TemplateView):
    template_name = 'daily/daily_pag.html'

##### CREATE #####
#criação da daily
class dailyCreate(CreateView):
    model = dateDaily
    fields = [
        'date'
    ]
    template_name = 'daily/inicio_daily.html'
    success_url= reverse_lazy('form-daily')

#formulário da daily
class formDailyCreate(CreateView):
    model = formularioDaily
    fields = [
        'date_daily',
        'q1',
        'q2',
        'q3',
    ]
    template_name = 'daily/form_daily.html'
    success_url = reverse_lazy('pagina-daily')

##### UPDATE #####
#update da data da daily
class dailyUpdate(UpdateView):
    model = dateDaily
    fields = [
        'date'
    ]
    template_name = 'daily/inicio_daily.html'
    url = 'update-daily'
    success_url= reverse_lazy(url)
    
#update do formulário da daily
class formDailyUpdate(UpdateView):
    model = formularioDaily
    fields = [
        'date_daily',
        'q1',
        'q2',
        'q3',
    ]
    template_name = 'daily/form_daily.html'
    success_url = reverse_lazy('pagina-daily')

##### DELETE #####
class dailyDelete(DeleteView):
    model = dateDaily
    template_name = 'daily/excluir_daily.html'
    success_url = reverse_lazy('pagina-daily')

##### LISTAS #####
class dailyList(ListView):
    model = dateDaily
    template_name= 'daily/listas/data.html'
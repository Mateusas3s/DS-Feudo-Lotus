from multiprocessing import context
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .forms import dateForm, formDateForm
from .models import dateDaily, formularioDaily

#página da daily
class daily_Pag(TemplateView):
    template_name = 'daily/daily_pag.html'

##### CREATE #####
#criação da daily
def dailyCreate(request):
    form = dateForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('form-daily')
    context = {
        'form': form
    }
    return render(request, 'daily/inicio_daily.html', context)

#formulário da daily
def formDailyCreate(request):
    form = formDateForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('pagina-daily')
    context = {
        'form': form
    }
    return render(request, 'daily/form_daily.html', context)

##### UPDATE #####
#update da data da daily
def dailyUpdate(request, pk):
    daily = dateDaily.objects.get(id=pk)
    form = dateForm(instance=daily)
    if request.method == 'POST':
        form = dateForm(request.POST, instance=daily)
        if form.is_valid():
            form.save()
            url = '/update/form/{}'.format(pk)
            return redirect(url)
    context = {
        'form': form,
        'daily': daily,
    }
    return render(request, 'daily/inicio_daily_edit.html', context)
    
#update do formulário da daily
def formDailyUpdate(request, pk):
    formDaily = formularioDaily.objects.get(id=pk)
    form = formDateForm(instance=formDaily)
    if request.method == 'POST':
        form = formDateForm(request.POST, instance=formDaily)
        if form.is_valid():
            form.save()
            return redirect('pagina-daily')
    context = {
        'form': form,
        'formDaily': formDaily,
    }
    return render(request, 'daily/form_daily_edit.html', context)


##### DELETE #####
class dailyDelete(DeleteView):
    model = dateDaily
    template_name = 'daily/excluir_daily.html'
    success_url = reverse_lazy('lista-date')

##### LISTAS #####
class dailyList(ListView):
    model = dateDaily
    template_name= 'daily/listas/data.html'

def contribList(request):
    daily = formularioDaily.objects.all()
    return render(request,'daily/listas/contribuicoes.html', {'daily':daily})
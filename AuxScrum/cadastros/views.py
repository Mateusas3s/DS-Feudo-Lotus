from audioop import reverse
from multiprocessing import context
from re import template
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Projeto
from .forms import ProjetoForm

# #Create your views here.

# # Create

# class ProjetoCreate(CreateView):
#     model = Projeto
#     fields = ['nome', 'descricao', 'membros']
#     template_name = 'cadastros/cadastrarProjeto.html'
#     success_url = reverse_lazy('home')


# # Update

# class ProjetoUpdate(UpdateView):
#     model = Projeto
#     fields = ['nome', 'descricao', 'membros']
#     template_name = 'cadastros/editarProjeto.html'
#     success_url = reverse_lazy('home')

# # Delete

class ProjetoDelete(DeleteView):
    model = Projeto
    template_name = 'cadastros/excluirProjeto.html'
    success_url = reverse_lazy('home')

# # List

class ProjetoList(ListView):
    model = Projeto
    template_name = 'usuarios/home.html'
    
    def get_queryset(self):
        self.object_list = Projeto.objects.filter(membros=self.request.user)
        return self.object_list

def paginaProjeto(request, pk):
    projeto = Projeto.objects.get(id=pk)
    context = {
        'projeto': projeto
    }
    return render(request, 'cadastros/paginaProjeto.html', context)


def cadastrarProjeto(request):
    form = ProjetoForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'cadastros/cadastrarProjeto.html', context)

def editarProjeto(request, pk):
    projeto = Projeto.objects.get(id=pk)
    form = ProjetoForm(instance=projeto)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
        'projeto': projeto,
    }
    return render(request, 'cadastros/editarProjeto.html', context)



    
        
    





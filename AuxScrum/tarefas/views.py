from django.shortcuts import get_object_or_404, render, redirect
from .models import Tarefa
from .forms import AdicionarTarefa, EditarTarefaForm

def tarefas_pendentes_list(request):
    tarefas_pendentes = Tarefa.objects.filter(status='pendente')
    
    return render(request, 'tarefas/tarefas_pendentes.html',
                  {'tarefas_pendentes':tarefas_pendentes,})
                   
def concluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = 'concluído'
    tarefa.save()
    return redirect('tarefas_progresso_list')

def excluir_tarefa_pendente(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.delete()
    return redirect('tarefas_pendentes_list')

def excluir_tarefa_progresso(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.delete()
    return redirect('tarefas_progresso_list')

def excluir_tarefa_concluidas(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.delete()
    return redirect('tarefas_concluidas_list')

def adiar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = 'adiado'
    tarefa.save()
    return redirect('tarefas_pendentes_list')

def editar_tarefa_pendente(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == 'POST':
        form = EditarTarefaForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            tarefa.descricao = cd['tarefa']
            tarefa.categoria = cd['categoria']
            tarefa.save()
            return redirect('tarefas_pendentes_list')
    else:
        form = EditarTarefaForm(initial={'tarefa':tarefa.descricao, 'categoria':tarefa.categoria})
    return render(request, 'tarefas/editar_tarefa_pendente.html', {'tarefa':tarefa, 'form':form})

def editar_tarefa_progresso(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == 'POST':
        form = EditarTarefaForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            tarefa.descricao = cd['tarefa']
            tarefa.categoria = cd['categoria']
            tarefa.save()
            return redirect('tarefas_progresso_list')
    else:
        form = EditarTarefaForm(initial={'tarefa':tarefa.descricao, 'categoria':tarefa.categoria})
    return render(request, 'tarefas/editar_tarefa_progresso.html', {'tarefa':tarefa, 'form':form})

def tarefas_concluidas_list(request):
    tarefas_concluidas = Tarefa.objects.filter(status='concluído')
    return render(request, 'tarefas/tarefas_concluidas.html', {'tarefas_concluidas':tarefas_concluidas})

def tarefas_adiadas_list(request):
    tarefas_adiadas = Tarefa.objects.filter(status='adiado')
    return render(request, 'tarefas/tarefas_adiadas.html', {'tarefas_adiadas':tarefas_adiadas})

def mover_para_pendente(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = 'pendente'
    tarefa.save()
    return redirect('tarefas_progresso_list')

def mover_para_progresso(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = 'adiado'
    tarefa.save()
    return redirect('tarefas_concluidas_list')

def tarefaPage(request):
    if request.method == 'POST':
        form = AdicionarTarefa(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefas_page')
    else:
        form = AdicionarTarefa()
    return render(request, 'tarefas/tarefas.html', context={'form':form})

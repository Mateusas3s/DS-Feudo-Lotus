from django.urls import path, include
from . import views

urlpatterns = [
    path('tarefas/', views.tarefaPage, name='tarefas_page' ),
    path('pendentes/', views.tarefas_pendentes_list, name='tarefas_pendentes_list' ),
    path('<int:tarefa_id>/concluir/', views.concluir_tarefa, name='concluir_tarefa'),
    path('<int:tarefa_id>/excluir/pendente', views.excluir_tarefa_pendente, name='excluir_tarefa_pendente'),
    path('<int:tarefa_id>/excluir/progresso', views.excluir_tarefa_progresso, name='excluir_tarefa_progresso'),
    path('<int:tarefa_id>/excluir/concluidas', views.excluir_tarefa_concluidas, name='excluir_tarefa_concluidas'),
    path('<int:tarefa_id>/comecar/', views.adiar_tarefa, name='comecar_tarefa'),
    path('<int:tarefa_id>/editar/progresso', views.editar_tarefa_progresso, name='editar_tarefa_progresso'),
    path('<int:tarefa_id>/editar/pendente', views.editar_tarefa_pendente, name='editar_tarefa_pendente'),
    path('concluidas/', views.tarefas_concluidas_list, name='tarefas_concluidas_list'),
    path('progresso/', views.tarefas_adiadas_list, name='tarefas_progresso_list'),
    path('<int:tarefa_id>/mover-para-lista-pendente/', views.mover_para_pendente, name='mover_para_pendente'),
    path('<int:tarefa_id>/mover-para-lista-progresso/', views.mover_para_progresso, name='mover_para_progresso'),
]
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ProjetoList, ProjetoDelete
from . import views


urlpatterns = [
    #path('', view, name=''),
    path('home/', ProjetoList.as_view(), name='home'),
    path('projeto/<int:pk>', views.paginaProjeto, name='pagina-projeto'),
    path('cadastrar/projeto/', views.cadastrarProjeto, name='cadastrarProjeto'),
    path('editar/projeto/<int:pk>', views.editarProjeto, name='editarProjeto'),
    path('excluir/projeto/<int:pk>', ProjetoDelete.as_view(), name='excluir-projeto'),
]
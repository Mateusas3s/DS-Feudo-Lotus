from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ProjetoCreate, ProjetoDelete, ProjetoList, ProjetoUpdate


urlpatterns = [
    #path('', view, name=''),
    path('home/', ProjetoList.as_view(), name='home'),
    path('cadastrar/projeto/', ProjetoCreate.as_view(), name='cadastrar-projeto'),
    path('editar/projeto/<int:pk>', ProjetoUpdate.as_view(), name='editar-projeto'),
    path('excluir/projeto/<int:pk>', ProjetoDelete.as_view(), name='excluir-projeto'),
]
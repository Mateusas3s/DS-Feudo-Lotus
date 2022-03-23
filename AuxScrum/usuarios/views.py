from re import template
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import UsuarioForm
from django.urls import reverse_lazy


# Create your views here.

class PaginaInicial(TemplateView):
    template_name = 'usuarios/index.html'

class UsuarioCreate(CreateView):
    template_name = 'usuarios/formCadastro.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')




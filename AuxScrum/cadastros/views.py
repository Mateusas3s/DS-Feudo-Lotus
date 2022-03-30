from re import template
from django.views.generic import TemplateView

# Create your views here.

class PaginaInicial(TemplateView):
    template_name = 'usuarios/home.html'
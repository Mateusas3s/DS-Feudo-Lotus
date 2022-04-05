from django.shortcuts import render
from . import forms

# Create your views here.

def daily(request):
    form = forms.formularioDaily()
    context = {
        'form': form
    }
    return render(request, 'daily/relatorio_daily.html', context= context)
from django.shortcuts import redirect, render
from .forms import CadastroForm

# Create your views here.

def cadastro(response):
    if response.method == 'POST':
        form = CadastroForm(response.POST)
        if form.is_valid:
            form.save()
        
    else:
        form = CadastroForm()
    
    return render(response, 'cadastro/cadastro.html', {'form': form})


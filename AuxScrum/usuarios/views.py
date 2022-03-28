from dataclasses import fields
from re import template
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from .models import UserProfile
from .forms import UsuarioForm, UserProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User



# Create your views here.

class UsuarioCreate(CreateView):
    template_name = 'usuarios/formCadastro.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

def edit_profile(request, user_id):
    usuario = UserProfile.objects.get(user_id=user_id)
    user_dado = User.objects.get(id=user_id)
    context={
        'usuario': usuario,
        'user_dado':user_dado,
        }
    return render(request, 'usuarios/formEdicao.html', context)

def salvarProfile(request, user_id):
    usuario = UserProfile.objects.get(user_id=user_id)
    user_dado = User.objects.get(id=user_id)
    nome_completo = request.POST.get('nome_completo')
    telefone = request.POST.get('telefone')
    username = request.POST.get('username')
    email = request.POST.get('email')
    usuario.user_id = user_id
    usuario.nome_completo = nome_completo
    usuario.telefone = telefone
    usuario.save()
    user_dado.id = user_id
    user_dado.username = username
    user_dado.email = email
    user_dado.save()
    return redirect('home')
    


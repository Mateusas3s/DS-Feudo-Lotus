from dataclasses import fields
from multiprocessing import context
from re import template
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import TemplateView
from flask import request
from .models import UserProfile
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

class UsuarioCreate(CreateView):
    template_name = 'usuarios/formCadastro.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

# Perfil de Usuário 
def paginaPerfil(request, user_id):
    usuario = UserProfile.objects.get(user_id=user_id)
    user_dado = User.objects.get(id=user_id)
    context={
        'usuario': usuario,
        'user_dado':user_dado,
        }
    return render(request, 'usuarios/paginaPerfil.html', context)

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

def alterarSenha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, 'usuarios/home.html')
        else:
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
        context = {
            'form': form
        }
    return render(request, 'usuarios/alterarSenha.html', context)

class UserDelete(DeleteView):
    template_name = 'usuarios/formDelete.html'
    model = User
    success_url = reverse_lazy('login')



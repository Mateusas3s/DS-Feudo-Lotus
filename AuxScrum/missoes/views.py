from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from missoes.models import Missao

from missoes.forms import NovaMissaoForm

def home(request):
    if request.method == 'POST':
        form = NovaMissaoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('missoes:home'))
        else:
            missoes_pendentes = Missao.objects.filter(feita=False).all()
            return render(request,'missoes/home.html', {'form':form, 'missoes_pendentes': missoes_pendentes}, status=400)
    missoes_pendentes = Missao.objects.filter(feita=False).all()        
    return render (request, 'missoes/home.html',  {'missoes_pendentes': missoes_pendentes})

from dataclasses import fields
from django import forms
from django.forms import ModelForm
from . models import dateDaily, formularioDaily, dateRetro, formularioRetro

##DAILY##
class dateForm(forms.ModelForm):
    class Meta:
        model = dateDaily
        fields = ['date', 'user']

class formDateForm(forms.ModelForm):
    class Meta:
        model = formularioDaily
        fields = ['date_daily', 'q1', 'q2', 'q3']

##RETROSPECTIVA##
class retroForm(forms.ModelForm):
    class Meta:
        model = dateRetro
        fields = ['date', 'user']

class formRetroForm(forms.ModelForm):
    class Meta:
        model = formularioRetro
        fields = ['date_retro', 'q1', 'q2', 'q3']
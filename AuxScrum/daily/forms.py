from dataclasses import fields
from django import forms
from django.forms import ModelForm
from . models import dateDaily, formularioDaily

class dateForm(forms.ModelForm):
    class Meta:
        model = dateDaily
        fields = ['date', 'user']

class formDateForm(forms.ModelForm):
    class Meta:
        model = formularioDaily
        fields = ['date_daily', 'q1', 'q2', 'q3']
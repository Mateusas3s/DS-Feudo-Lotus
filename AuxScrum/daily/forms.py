from django import forms

class formularioDaily(forms.Form):
    q1 = forms.CharField(max_length=2500)
    q2 = forms.CharField(max_length=2500)
    q3 = forms.CharField(max_length=2500)
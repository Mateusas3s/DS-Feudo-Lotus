from django.forms import ModelForm
from missoes.models import Missao

class NovaMissaoForm(ModelForm):
    class Meta:
        model = Missao
        fields = ['nome']

class MissaoForm(ModelForm):
    class Meta:
        model = Missao
        fields = ['nome', 'feita']

class MissaoForm2(ModelForm):
    class Meta:
        model = Missao
        fields = ['nome', 'feita']
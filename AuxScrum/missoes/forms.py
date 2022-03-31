from django.forms import ModelForm
from missoes.models import Missao

class NovaMissaoForm(ModelForm):
    class Meta:
        model = Missao
        fields = ['nome']
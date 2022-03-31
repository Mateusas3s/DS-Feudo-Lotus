from django.urls import reverse
from pytest_django.asserts import assertContains
import pytest

from AuxScrum.missoes.models import Missao

@pytest.fixture
def resposta(client, db):
    resp = client.get(reverse('missoes:home'))
    return resp

def test_status_code(resposta):
    assert resposta.status_code == 200

def test_formulario_presente(resposta):
    assertContains(resposta, '<form')

def test_botao_adcionar_presente(resposta):
    assertContains (resposta, '<button type="submit"')

@pytest.fixture
def lista_de_missoes_pendentes(db):
    missoes = [ 
        Missao(nome='Missao 1', feita=False),
        Missao(nome='Missao 2', feita=False),
    ]
    Missao.objects.bulk_create(missoes)
    return missoes

@pytest.fixture
def resposta_com_lista_de_missoes(client, lista_de_missoes_pendentes):
    resp = client.get(reverse('missoes:home'))
    return resp

def test_lista_de_missoes_pendentes_presente(resposta_com_lista_de_missoes, lista_de_missoes_pendentes):
    for missao in lista_de_missoes_pendentes:
        assertContains(resposta_com_lista_de_missoes, missao.nome)
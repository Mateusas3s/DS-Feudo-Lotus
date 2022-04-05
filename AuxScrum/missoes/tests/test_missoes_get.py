# from django.urls import reverse
# from pytest_django.asserts import assertContains
# import pytest

# from AuxScrum.missoes.models import Missao

# @pytest.fixture
# def resposta(client, db):
#     resp = client.get(reverse('missoes:home'))
#     return resp

# def test_status_code(resposta):
#     assert resposta.status_code == 200

# def test_formulario_presente(resposta):
#     assertContains(resposta, '<form')

# def test_botao_adcionar_presente(resposta):
#     assertContains (resposta, '<button type="submit"')

# @pytest.fixture
# def lista_de_missoes_pendentes(db):
#     missoes = [ 
#         Missao(nome='Missao 1', feita=False),
#         Missao(nome='Missao 2', feita=False),
#     ]
#     Missao.objects.bulk_create(missoes)
#     return missoes

# @pytest.fixture
# def lista_de_missoes_progresso(db):
#     missoes = [ 
#         Missao(nome='Missao 5', feita=False),
#         Missao(nome='Missao 6', feita=False),
#     ]
#     Missao.objects.bulk_create(missoes)
#     return missoes

# @pytest.fixture
# def lista_de_missoes_feitas(db):
#     missoes = [ 
#         Missao(nome='Missao 3', feita=True),
#         Missao(nome='Missao 4', feita=True),
#     ]
#     Missao.objects.bulk_create(missoes)
#     return missoes

# @pytest.fixture
# def resposta_com_lista_de_missoes(client, lista_de_missoes_pendentes, lista_de_missoes_feitas):
#     resp = client.get(reverse('missoes:home'))
#     return resp

# def test_lista_de_missoes_pendentes_presentes(resposta_com_lista_de_missoes, lista_de_missoes_pendentes):
#     for missao in lista_de_missoes_pendentes:
#         assertContains(resposta_com_lista_de_missoes, missao.nome)

# def test_lista_de_missoes_progresso_presentes(resposta_com_lista_de_missoes, lista_de_missoes_pendentes):
#     for missao in lista_de_missoes_pendentes:
#         assertContains(resposta_com_lista_de_missoes, missao.nome)

# def test_lista_de_missoes_feitas_presentes(resposta_com_lista_de_missoes, lista_de_missoes_feitas):
#     for missao in lista_de_missoes_feitas:
#         assertContains(resposta_com_lista_de_missoes, missao.nome)
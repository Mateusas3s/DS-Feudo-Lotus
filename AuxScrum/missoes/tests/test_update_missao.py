# from django.urls import reverse
# from pytest_django.asserts import assertContains
# import pytest
# from AuxScrum.missoes.models import Missao
# from AuxScrum.missoes.tests.test_missoes_get import test_status_code

# @pytest.fixture
# def missao_pendente(db):
#     return Missao.objects.create(nome='Missao 1', feita=False)

# @pytest.fixture
# def missao_progresso(db):
#     return Missao.objects.create(nome='Missao 1', feita=False)

# @pytest.fixture
# def resposta_com_missao_pendente(client, missao_pendente):
#     resp = client.post (
#         reverse('missoes:detalhe', kwargs={'missao_id': missao_pendente.id}),
#         data = {'feita':'true', 'nome': f'{missao_pendente.nome}-editada'}
#     )
#     return resp

# @pytest.fixture
# def resposta_com_missao_progresso(client, missao_progresso):
#     resp = client.post (
#         reverse('missoes:detalhe2', kwargs={'missao_id': missao_progresso.id}),
#         data = {'feita':'true', 'nome': f'{missao_progresso.nome}-editada'}
#     )
#     return resp

# def test_status_code (resposta_com_missao_pendente):
#     assert resposta_com_missao_pendente.status_code == 302

# def test_status_code (resposta_com_missao_progresso):
#     assert resposta_com_missao_progresso.status_code == 302

# def test_missao_feita (resposta_com_missao_pendente):
#     assert Missao.objects.first().feita

# def test_missao_feita (resposta_com_missao_progresso):
#     assert Missao.objects.first().feita


# @pytest.fixture
# def missao_feita(db):
#     return Missao.objects.create(nome='Missao 1', feita=True)

# @pytest.fixture
# def resposta_com_missao_feita(client, missao_feita):
#     resp = client.post (
#         reverse('missoes:detalhe', kwargs={'missao_id': missao_feita.id}),
#         data = {'nome': f'{missao_feita.nome}-editada'}
#     )
#     return resp


# def test_missao_pendente (resposta_com_missao_feita):
#     assert not Missao.objects.first().feita
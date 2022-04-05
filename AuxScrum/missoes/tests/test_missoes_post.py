# from dataclasses import dataclass
# import pytest


# import pytest
# from django.urls import reverse
# from AuxScrum.missoes.models import Missao

# def test_missao_existe_no_bd(resposta):
#     assert Missao.objects.exists()

# def test_redirecionamento_depois_do_salvamento(resposta):
#     assert resposta.status_code==302

# @pytest.fixture
# def resposta_dado_invalido(client, db):
#     resp = client.post(reverse('tarefas:home'), data={'nome':''})
#     return resp


# def test_missao_nao_existe_no_bd(resposta_dado_invalido):
#     assert not Missao.objects.exists()

# def test_pagina_com_dados_invalidos(resposta_dado_invalido):
#     assert resposta_dado_invalido.status_code == 400
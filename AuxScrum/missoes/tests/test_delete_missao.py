from audioop import reverse
import pytest
from missoes.models import Missao

@pytest.fixture
def tarefa(db):
    return Missao.objects.create(nome='Missao 1', feita=False)

@pytest.fixture
def resposta(client, tarefa):
    resp = client.post (
        reverse('missoes:excluir', kwargs={'missao_id': tarefa.id}),
    )
    return resp

def test_excluir_missao(resposta):
    assert not Missao.objects.exists()
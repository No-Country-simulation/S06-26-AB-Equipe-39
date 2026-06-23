"""Testes do endpoint POST /saude.

Foco especial na regra crítica: nota_semanal < 4 deve derivar ao CVV.
"""

import pytest

BASE = {
    "usuario_id": "u_123",
    "humor": "ansioso",
    "nota_semanal": 7,
    "contexto": "semana cheia",
}


def test_saude_sem_crise(client):
    resp = client.post("/saude", json=BASE)
    assert resp.status_code == 200
    body = resp.json()
    assert body["derivar_cvv"] is False
    assert body["alerta"] is None
    assert body["nota_atual"] == 7
    assert body["mensagem"]
    assert body["acao_sugerida"]


def test_saude_crise_deriva_cvv(client):
    """nota_semanal=3 (< 4) deve acionar a derivação ao CVV."""
    resp = client.post("/saude", json={**BASE, "nota_semanal": 3})
    assert resp.status_code == 200
    body = resp.json()
    assert body["derivar_cvv"] is True
    assert body["alerta"] is not None
    assert "188" in body["mensagem"]


@pytest.mark.parametrize("nota,espera_cvv", [(0, True), (3, True), (4, False), (10, False)])
def test_saude_limiar_de_crise(client, nota, espera_cvv):
    """O corte é estrito: nota < 4 deriva; nota == 4 não deriva."""
    resp = client.post("/saude", json={**BASE, "nota_semanal": nota})
    assert resp.status_code == 200
    assert resp.json()["derivar_cvv"] is espera_cvv


def test_saude_humor_desconhecido_usa_default(client):
    resp = client.post("/saude", json={**BASE, "humor": "confuso"})
    assert resp.status_code == 200
    assert resp.json()["mensagem"]  # cai no default, mas sempre responde algo


def test_saude_nota_fora_do_intervalo(client):
    resp = client.post("/saude", json={**BASE, "nota_semanal": 99})
    assert resp.status_code == 422

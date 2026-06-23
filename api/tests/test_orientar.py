"""Testes do endpoint POST /orientar."""

PERFIL_ENGENHARIA = {
    "usuario_id": "u_123",
    "perfil": "Engenharia Informática",
    "nivel": "junior",
    "regiao": "Luanda, AO",
    "idioma": "pt",
    "lat": -8.8383,
    "lng": 13.2344,
}


def test_orientar_engenharia(client):
    resp = client.post("/orientar", json=PERFIL_ENGENHARIA)
    assert resp.status_code == 200
    body = resp.json()
    # Contrato completo presente
    assert set(body) == {
        "gap_percentual",
        "gap_itens",
        "trilha_sugerida",
        "vagas_compativeis",
        "confianca",
    }
    assert 0 <= body["gap_percentual"] <= 100
    assert "GEAR" in body["trilha_sugerida"]
    assert len(body["vagas_compativeis"]) >= 1
    assert 0.0 <= body["confianca"] <= 1.0


def test_orientar_gestao_usa_trilha_agil(client):
    payload = {**PERFIL_ENGENHARIA, "perfil": "Tecnologia em Gestão Empresarial"}
    resp = client.post("/orientar", json=payload)
    assert resp.status_code == 200
    assert "ONE" in resp.json()["trilha_sugerida"]


def test_orientar_design_usa_trilha_uiux(client):
    payload = {**PERFIL_ENGENHARIA, "perfil": "Design Gráfico"}
    resp = client.post("/orientar", json=payload)
    assert resp.status_code == 200
    assert "UI/UX" in resp.json()["trilha_sugerida"]


def test_orientar_nivel_pleno_reduz_gap(client):
    """Nível mais sênior aumenta o percentual já atendido (gap menor a fechar)."""
    junior = client.post("/orientar", json=PERFIL_ENGENHARIA).json()
    pleno = client.post(
        "/orientar", json={**PERFIL_ENGENHARIA, "nivel": "pleno"}
    ).json()
    assert pleno["gap_percentual"] >= junior["gap_percentual"]


def test_orientar_campo_obrigatorio_ausente(client):
    payload = {k: v for k, v in PERFIL_ENGENHARIA.items() if k != "perfil"}
    resp = client.post("/orientar", json=payload)
    assert resp.status_code == 422

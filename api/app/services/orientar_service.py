"""Lógica do /orientar (primeira fase: mockada).

Identifica a área do usuário a partir do campo `perfil`, escolhe a trilha/vagas
correspondentes no catálogo e calcula um gap percentual simples. Em fases
seguintes, esta função delega ao agente de IA e a consultas reais.
"""

from app.data.mocks import (
    CATALOGO_AREAS,
    CATALOGO_DEFAULT,
    PALAVRAS_CHAVE_AREA,
)
from app.schemas.orientar import OrientarRequest, OrientarResponse, VagaCompativel

# Ajuste de gap por nível: quanto mais sênior, menor o gap esperado.
_AJUSTE_GAP_POR_NIVEL: dict[str, int] = {
    "junior": 0,
    "júnior": 0,
    "pleno": 10,
    "senior": 20,
    "sênior": 20,
}


def _identificar_area(perfil: str) -> str:
    """Retorna a chave de área do catálogo a partir do texto do perfil."""
    perfil_norm = perfil.lower()
    for palavra, area in PALAVRAS_CHAVE_AREA.items():
        if palavra in perfil_norm:
            return area
    return "default"


def orientar(req: OrientarRequest) -> OrientarResponse:
    """Gera a orientação (gap + trilha + vagas) para o perfil informado."""
    area = _identificar_area(req.perfil)
    dados = CATALOGO_AREAS.get(area, CATALOGO_DEFAULT)

    # Gap base: maior match entre as vagas compatíveis (o "70% que você já atende").
    melhor_match = max((v["match"] for v in dados["vagas"]), default=60)
    ajuste = _AJUSTE_GAP_POR_NIVEL.get(req.nivel.lower(), 0)
    gap_percentual = min(100, melhor_match + ajuste)

    vagas = [VagaCompativel(**v) for v in dados["vagas"]]

    return OrientarResponse(
        gap_percentual=gap_percentual,
        gap_itens=dados["gap_itens"],
        trilha_sugerida=dados["trilha_sugerida"],
        vagas_compativeis=vagas,
        confianca=0.82,
    )

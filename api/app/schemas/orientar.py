"""Schemas do endpoint POST /orientar.

Contrato em docs/api.md. Cruza o perfil do usuário com trilhas e vagas e devolve
o gap percentual + o próximo passo concreto.
"""

from pydantic import BaseModel, Field


class OrientarRequest(BaseModel):
    """Entrada do /orientar — o perfil do usuário e seu contexto geográfico."""

    usuario_id: str = Field(..., examples=["u_123"], description="Identificador do usuário")
    perfil: str = Field(..., examples=["Engenharia Informática"], description="Formação/área principal")
    nivel: str = Field(..., examples=["junior"], description="Nível profissional (ex.: junior, pleno)")
    regiao: str = Field(..., examples=["Luanda, AO"], description="Região do usuário (cidade, país)")
    idioma: str = Field("pt", examples=["pt"], description="Idioma preferido (pt, es)")
    lat: float | None = Field(None, examples=[-8.8383], description="Latitude (geolocalização)")
    lng: float | None = Field(None, examples=[13.2344], description="Longitude (geolocalização)")


class VagaCompativel(BaseModel):
    """Uma vaga compatível com o perfil, com o percentual de match."""

    titulo: str = Field(..., examples=["Programador Júnior"])
    empresa: str = Field(..., examples=["TechAO"])
    match: int = Field(..., ge=0, le=100, examples=[70], description="Match percentual (0–100)")


class OrientarResponse(BaseModel):
    """Saída do /orientar — gap, trilha e vagas compatíveis."""

    gap_percentual: int = Field(..., ge=0, le=100, description="Quanto o usuário já atende (0–100)")
    gap_itens: list[str] = Field(..., description="Competências que faltam para fechar o gap")
    trilha_sugerida: str = Field(..., description="Próximo passo concreto de formação")
    vagas_compativeis: list[VagaCompativel] = Field(..., description="Vagas com match percentual")
    confianca: float = Field(..., ge=0.0, le=1.0, description="Confiança da recomendação (0–1)")

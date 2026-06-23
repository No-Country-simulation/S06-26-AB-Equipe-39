"""Schemas do endpoint POST /saude.

Contrato em docs/api.md. Endpoint SENSÍVEL — diretrizes em docs/saude-mental.md.
Regra crítica: nota_semanal < CRISIS_THRESHOLD aciona derivar_cvv=True.
"""

from pydantic import BaseModel, Field


class SaudeRequest(BaseModel):
    """Entrada do /saude — o check-in emocional do usuário."""

    usuario_id: str = Field(..., examples=["u_123"], description="Identificador do usuário")
    humor: str = Field(
        ...,
        examples=["ansioso"],
        description="Emoji/estado: feliz, cansado, triste, ansioso, sobrecarregado…",
    )
    nota_semanal: int = Field(
        ...,
        ge=0,
        le=10,
        examples=[3],
        description="Nota de bem-estar da semana (0–10)",
    )
    contexto: str | None = Field(
        None,
        examples=["semana de provas e sem retorno de vagas"],
        description="Texto livre opcional com o contexto do usuário",
    )


class SaudeResponse(BaseModel):
    """Saída do /saude — mensagem acolhedora + ação sugerida (+ derivação CVV)."""

    mensagem: str = Field(..., description="Resposta acolhedora do agente")
    acao_sugerida: str = Field(..., description="Ação concreta e humana de bem-estar")
    derivar_cvv: bool = Field(..., description="True quando nota_semanal < limiar de crise")
    nota_atual: int = Field(..., ge=0, le=10, description="Nota registrada no check-in")
    alerta: str | None = Field(None, description="Mensagem de alerta interno, quando aplicável")

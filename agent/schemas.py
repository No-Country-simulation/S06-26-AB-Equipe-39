"""
Schemas utilizados pelo módulo de IA.
"""

from typing import Optional
from pydantic import BaseModel, Field


class UserInput(BaseModel):
    """
    Dados recebidos do backend.
    """

    message: str = Field(
        ...,
        description="Mensagem enviada pelo utilizador."
    )

    language: str = "pt"

    country: Optional[str] = None

    profile: Optional[str] = None

    level: Optional[str] = None

    area: Optional[str] = None

    objective: Optional[str] = None

    mood: Optional[str] = None


class AIResponse(BaseModel):
    """
    Resposta devolvida ao backend.
    """

    success: bool

    route: str

    response: str

    model: str

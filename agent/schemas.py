from pydantic import BaseModel
from typing import List, Optional


class UserInput(BaseModel):
    usuario_id: str
    perfil: str
    nivel: str
    objetivo: str
    area: str
    regiao: Optional[str] = None


class AIResponse(BaseModel):
    perfil_resumido: str
    pontos_fortes: List[str]
    lacunas: List[str]
    gap_percentual: int
    recomendacao: List[str]
    trilha_sugerida: str
    confianca: float

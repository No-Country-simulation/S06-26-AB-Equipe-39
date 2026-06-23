"""Router POST /saude.

⚠️ Endpoint sensível — ver docs/saude-mental.md.
"""

from fastapi import APIRouter

from app.schemas.saude import SaudeRequest, SaudeResponse
from app.services.saude_service import avaliar_saude

router = APIRouter(tags=["saude"])


@router.post("/saude", response_model=SaudeResponse, summary="Check-in de saúde mental")
def post_saude(req: SaudeRequest) -> SaudeResponse:
    """Recebe o check-in emocional e devolve mensagem + ação sugerida.

    Regra crítica: nota_semanal < limiar de crise aciona derivar_cvv=True.
    Ver contrato em docs/api.md e diretrizes em docs/saude-mental.md.
    """
    return avaliar_saude(req)

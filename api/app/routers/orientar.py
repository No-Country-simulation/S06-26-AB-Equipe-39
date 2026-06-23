"""Router POST /orientar."""

from fastapi import APIRouter

from app.schemas.orientar import OrientarRequest, OrientarResponse
from app.services.orientar_service import orientar

router = APIRouter(tags=["orientar"])


@router.post("/orientar", response_model=OrientarResponse, summary="Orientação de carreira")
def post_orientar(req: OrientarRequest) -> OrientarResponse:
    """Cruza o perfil com trilhas e vagas e devolve o gap + próximo passo.

    Ver contrato em docs/api.md.
    """
    return orientar(req)

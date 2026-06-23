"""Router GET /health — verificação simples de disponibilidade."""

from fastapi import APIRouter

from app import __version__

router = APIRouter(tags=["health"])


@router.get("/health", summary="Health check")
def health() -> dict:
    """Retorna o status da API (útil para o deploy em Railway/Render)."""
    return {"status": "ok", "version": __version__}

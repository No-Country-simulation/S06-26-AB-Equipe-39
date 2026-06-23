"""Ponto de entrada da API do App BiT (FastAPI).

Sobe a aplicação, configura CORS para o front e registra os routers.
Rode com:  uvicorn app.main:app --reload --port 3000  (a partir de api/).
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import __version__
from app.config import settings
from app.routers import health, orientar, saude

app = FastAPI(
    title=settings.app_name,
    version=__version__,
    description=(
        "API do App BiT — orientação de carreira (/orientar) e check-in de "
        "saúde mental (/saude). Primeira fase com dados mockados. "
        "Contrato em docs/api.md."
    ),
)

# CORS aberto na primeira fase para facilitar o desenvolvimento do front.
# ⚠️ Restrinja allow_origins ao domínio do front antes de ir para produção.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registro dos endpoints.
app.include_router(health.router)
app.include_router(orientar.router)
app.include_router(saude.router)


@app.get("/", tags=["root"], summary="Raiz")
def root() -> dict:
    """Mensagem de boas-vindas e ponteiros úteis."""
    return {
        "app": settings.app_name,
        "version": __version__,
        "docs": "/docs",
        "endpoints": ["/health", "/orientar", "/saude"],
    }

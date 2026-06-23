"""Lógica do /saude (primeira fase: mockada).

⚠️ SENSÍVEL — ver docs/saude-mental.md.

Regra crítica de negócio: se `nota_semanal` for MENOR que o limiar de crise
(settings.crisis_threshold, padrão 4), a resposta deve obrigatoriamente derivar
ao CVV (derivar_cvv=True) e exibir o contato de forma acolhedora.
"""

from app.config import settings
from app.data.mocks import RESPOSTA_HUMOR_DEFAULT, RESPOSTAS_HUMOR
from app.schemas.saude import SaudeRequest, SaudeResponse


def _mensagem_crise() -> str:
    """Mensagem de derivação ao CVV, exibida em situação de crise."""
    return (
        "Sentimos que você está passando por um momento difícil. Você não está "
        f"sozinho. Fale com o CVV — Centro de Valorização da Vida: ligue {settings.cvv_phone} "
        f"(gratuito, 24h) ou acesse {settings.cvv_url}."
    )


def avaliar_saude(req: SaudeRequest) -> SaudeResponse:
    """Avalia o check-in emocional e devolve mensagem + ação (+ derivação CVV)."""
    em_crise = req.nota_semanal < settings.crisis_threshold

    if em_crise:
        # Em crise, a prioridade é acolher e derivar — a ação sugerida é o contato do CVV.
        return SaudeResponse(
            mensagem=_mensagem_crise(),
            acao_sugerida=(
                f"Procure ajuda agora: CVV {settings.cvv_phone} ou {settings.cvv_url} "
                "(chat e e-mail disponíveis)."
            ),
            derivar_cvv=True,
            nota_atual=req.nota_semanal,
            alerta=(
                f"Nota {req.nota_semanal} abaixo de {settings.crisis_threshold} — "
                "derivação ao CVV acionada."
            ),
        )

    # Fora de crise: resposta acolhedora baseada no humor informado.
    resposta = RESPOSTAS_HUMOR.get(req.humor.lower(), RESPOSTA_HUMOR_DEFAULT)
    return SaudeResponse(
        mensagem=resposta["mensagem"],
        acao_sugerida=resposta["acao_sugerida"],
        derivar_cvv=False,
        nota_atual=req.nota_semanal,
        alerta=None,
    )

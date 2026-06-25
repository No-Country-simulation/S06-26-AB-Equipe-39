"""

Configurações globais do módulo de IA.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Diretório raiz do módulo agent
BASE_DIR = Path(__file__).resolve().parent

# Diretório dos prompts
PROMPTS_DIR = BASE_DIR / "prompts"

# Configurações da API Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

MODEL_NAME = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)

TEMPERATURE = float(
    os.getenv("TEMPERATURE", "0.7")
)

MAX_OUTPUT_TOKENS = int(
    os.getenv("MAX_OUTPUT_TOKENS", "2048")
)

TOP_P = float(
    os.getenv("TOP_P", "0.95")
)

TOP_K = int(
    os.getenv("TOP_K", "40")
)

REQUEST_TIMEOUT = int(
    os.getenv("REQUEST_TIMEOUT", "60")
)


def validate_config() -> None:
    """
    Verifica se as configurações obrigatórias existem.
    """

    if not GEMINI_API_KEY:
        raise EnvironmentError(
            "A variável GEMINI_API_KEY não foi encontrada no arquivo .env."
        )

    if not PROMPTS_DIR.exists():
        raise FileNotFoundError(
            f"Pasta de prompts não encontrada: {PROMPTS_DIR}"
        )

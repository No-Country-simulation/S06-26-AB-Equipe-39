"""
Configuração do módulo de IA.

Responsável por carregar as variáveis de ambiente
utilizadas pelos fornecedores de Inteligência Artificial
(como Gemini e OpenAI).
"""

import os
from dotenv import load_dotenv

# Carrega as variáveis do ficheiro .env
load_dotenv()

# ==========================================================
# Fornecedor de IA
# ==========================================================

# Opções disponíveis:
# - gemini (padrão)
# - openai
AI_PROVIDER = os.getenv("AI_PROVIDER", "gemini").lower()

# ==========================================================
# Google Gemini
# ==========================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

# ==========================================================
# OpenAI
# ==========================================================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mi

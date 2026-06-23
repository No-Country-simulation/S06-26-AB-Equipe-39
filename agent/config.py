"""
Agent/config.py

Configuração do módulo de Inteligência Artificial.

Este ficheiro é responsável por carregar as variáveis de ambiente
utilizadas na integração com a Google Gemini.
"""

import os
from dotenv import load_dotenv

# Carrega as variáveis do ficheiro .env
load_dotenv()

# ==========================================================
# Google Gemini
# ==========================================================

# Chave da API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Modelo padrão
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

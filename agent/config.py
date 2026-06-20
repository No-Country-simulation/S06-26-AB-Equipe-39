"""
Configuração do módulo de IA.

Responsável por carregar variáveis de ambiente
utilizadas pela integração com a OpenAI.
"""

import os
from dotenv import load_dotenv

# Carrega o ficheiro .env
load_dotenv()

# Chave da API OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Modelo padrão
DEFAULT_MODEL = "gpt-4.1-mini"

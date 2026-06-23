"""Configuração da API, carregada de variáveis de ambiente (.env).

Mantém num único lugar as constantes de negócio e os ajustes de execução. Nunca
coloque segredos diretamente aqui — use o arquivo .env (ver ../.env.example).
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configurações da aplicação.

    Os valores podem ser sobrescritos por variáveis de ambiente de mesmo nome
    (case-insensitive) ou por um arquivo .env na raiz do projeto.
    """

    model_config = SettingsConfigDict(
        env_file=(".env", "../.env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # --- Servidor ---
    app_name: str = "App BiT API"
    environment: str = "development"
    port: int = 3000

    # --- Internacionalização ---
    default_locale: str = "pt"  # pt | es

    # --- Regra de negócio: Saúde Mental / CVV ---
    # nota_semanal < CRISIS_THRESHOLD aciona a derivação automática ao CVV.
    crisis_threshold: int = 4
    cvv_phone: str = "188"
    cvv_url: str = "https://www.cvv.org.br"


# Instância única reutilizada em toda a aplicação.
settings = Settings()

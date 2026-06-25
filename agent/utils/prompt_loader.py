"""
Funções utilitárias para carregamento dos prompts.
"""

from pathlib import Path

from agent.config import PROMPTS_DIR


class PromptLoader:
    """
    Responsável por carregar prompts da pasta prompts/.
    """

    @staticmethod
    def load(prompt_name: str) -> str:
        """
        Carrega um prompt markdown.

        Exemplo:

        PromptLoader.load("career_guidance")
        """

        filename = f"{prompt_name}.md"

        path = PROMPTS_DIR / filename

        if not path.exists():
            raise FileNotFoundError(
                f"Prompt '{filename}' não encontrado em {PROMPTS_DIR}"
            )

        return path.read_text(
            encoding="utf-8"
        )

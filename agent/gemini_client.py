"""
Cliente responsável pela comunicação com a API Gemini.
"""

from typing import Optional

import google.generativeai as genai

from agent.config import (
    GEMINI_API_KEY,
    MODEL_NAME,
    TEMPERATURE,
    TOP_P,
    TOP_K,
    MAX_OUTPUT_TOKENS,
    validate_config
)


class GeminiClient:
    """
    Cliente responsável pela comunicação com a API Gemini.
    """

    def __init__(self):

        validate_config()

        genai.configure(api_key=GEMINI_API_KEY)

        self.model_name = MODEL_NAME

        generation_config = {

            "temperature": TEMPERATURE,

            "top_p": TOP_P,

            "top_k": TOP_K,

            "max_output_tokens": MAX_OUTPUT_TOKENS

        }

        self.model = genai.GenerativeModel(

            model_name=self.model_name,

            generation_config=generation_config

        )

    def generate(
        self,
        prompt: str
    ) -> str:
        """
        Gera uma resposta utilizando o modelo Gemini.
        """

        try:

            response = self.model.generate_content(
                prompt
            )

            if not response:
                raise RuntimeError(
                    "Nenhuma resposta foi retornada pela API."
                )

            text = getattr(response, "text", None)

            if text:
                return text.strip()

            candidates = getattr(response, "candidates", [])

            if candidates:

                parts = candidates[0].content.parts

                final_text = ""

                for part in parts:

                    if hasattr(part, "text"):

                        final_text += part.text

                if final_text:

                    return final_text.strip()

            raise RuntimeError(
                "Resposta inválida da API Gemini."
            )

        except Exception as e:

            raise RuntimeError(
                f"Erro ao comunicar com Gemini: {str(e)}"
            ) from e

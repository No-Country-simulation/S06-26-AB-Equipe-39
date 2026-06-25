"""
Responsável por identificar qual prompt deve ser utilizado.
"""

from typing import Dict


class AgentRouter:

    CAREER_KEYWORDS = {

        "emprego",
        "vaga",
        "trabalho",
        "currículo",
        "curriculo",
        "carreira",
        "profissão",
        "profissao",
        "curso",
        "estudo",
        "aprender",
        "python",
        "programação",
        "programacao",
        "java",
        "javascript",
        "react",
        "backend",
        "frontend",
        "dados",
        "ia",
        "inteligência artificial",
        "inteligencia artificial",
        "skill",
        "skills",
        "competência",
        "competencia",
        "linkedin"

    }

    MENTAL_KEYWORDS = {

        "triste",
        "tristeza",
        "ansioso",
        "ansiedade",
        "deprimido",
        "depressão",
        "depressao",
        "sozinho",
        "solidão",
        "solidao",
        "feliz",
        "desmotivado",
        "motivado",
        "cansado",
        "raiva",
        "medo",
        "stress",
        "estresse",
        "sobrecarregado",
        "emocional",
        "emoções",
        "emocoes"

    }

    DEFAULT_ROUTE = "system_prompt"

    @classmethod
    def detect_route(cls, message: str) -> str:

        text = message.lower()

        career_score = sum(
            word in text
            for word in cls.CAREER_KEYWORDS
        )

        mental_score = sum(
            word in text
            for word in cls.MENTAL_KEYWORDS
        )

        if career_score > mental_score and career_score > 0:
            return "career_guidance"

        if mental_score > career_score and mental_score > 0:
            return "mental_health"

        return cls.DEFAULT_ROUTE

    @classmethod
    def analyse(cls, message: str) -> Dict:

        route = cls.detect_route(message)

        return {

            "route": route,

            "confidence": "high"

        }

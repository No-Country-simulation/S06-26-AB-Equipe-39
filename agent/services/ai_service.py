"""
Serviço principal do módulo de IA.
"""

from agent.schemas import (
    UserInput,
    AIResponse
)

from agent.utils import PromptLoader
from agent.services.agent_router import AgentRouter

from agent.gemini_client import GeminiClient


class AIService:

    def __init__(self):

        self.client = GeminiClient()

    def build_prompt(
        self,
        prompt_name: str,
        user_message: str
    ) -> str:

        system_prompt = PromptLoader.load(prompt_name)

        final_prompt = f"""
{system_prompt}

----------------------------

Mensagem do utilizador:

{user_message}
"""

        return final_prompt.strip()

    def generate(
        self,
        request: UserInput
    ) -> AIResponse:

        analysis = AgentRouter.analyse(
            request.message
        )

        route = analysis["route"]

        prompt = self.build_prompt(
            route,
            request.message
        )

        response = self.client.generate(
            prompt
        )

        return AIResponse(

            success=True,

            route=route,

            response=response,

            model=self.client.model_name

        )

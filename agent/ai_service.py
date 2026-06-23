from Agent.agent_router import route_request
from Agent.utils.prompt_loader import load_prompt


class AIService:

    def __init__(self, gemini_client):
        self.client = gemini_client

    def build_prompt(self, prompt_type: str, user_input: dict):
        base_prompt = load_prompt(f"{prompt_type}_prompt.md")

        return f"""
{base_prompt}

USER DATA:
{user_input}
"""

    def generate_response(self, user_input: dict):

        route = route_request(user_input.get("objetivo", ""))

        if route == "career":
            prompt_type = "career_guidance"
        elif route == "mental":
            prompt_type = "mental_health"
        else:
            prompt_type = "system_prompt"

        prompt = self.build_prompt(prompt_type, user_input)

        response = self.client.generate_content(prompt)

        return {
            "response": response.text,
            "type": route
        }

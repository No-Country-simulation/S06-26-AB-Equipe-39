from ai_service import AIService

# Mock simples (simulando Gemini)
class MockGemini:
    def generate_content(self, prompt):
        class Response:
            text = "IA respondeu com sucesso (mock)"
        return Response()


ai = AIService(MockGemini())

user_input = {
    "usuario_id": "123",
    "perfil": "estudante de programação",
    "nivel": "junior",
    "objetivo": "carreira",
    "area": "backend",
    "regiao": "Luanda"
}

result = ai.generate_response(user_input)

print(result)

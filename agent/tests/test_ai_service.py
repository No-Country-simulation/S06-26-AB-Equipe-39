import unittest
from unittest.mock import patch

from agent.schemas import UserInput
from agent.services.ai_service import AIService


class TestAIService(unittest.TestCase):

    @patch("agent.gemini_client.GeminiClient.generate")

    def test_generate(self, mock_generate):

        mock_generate.return_value = "Resposta de teste."

        service = AIService()

        request = UserInput(

            message="Olá"

        )

        response = service.generate(request)

        self.assertTrue(response.success)

        self.assertEqual(

            response.response,

            "Resposta de teste."

        )


if __name__ == "__main__":

    unittest.main()

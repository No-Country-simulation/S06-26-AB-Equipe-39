import unittest

from agent.gemini_client import GeminiClient


class TestGeminiClient(unittest.TestCase):

    def test_create_client(self):

        client = GeminiClient()

        self.assertIsNotNone(client)


if __name__ == "__main__":

    unittest.main()

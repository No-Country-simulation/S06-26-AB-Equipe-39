import unittest

from agent.utils.prompt_loader import PromptLoader


class TestPromptLoader(unittest.TestCase):

    def test_load_system_prompt(self):

        prompt = PromptLoader.load(

            "system_prompt"

        )

        self.assertTrue(

            len(prompt) > 0

        )


if __name__ == "__main__":

    unittest.main()

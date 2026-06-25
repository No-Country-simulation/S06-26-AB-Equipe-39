import unittest

from agent.services.agent_router import AgentRouter


class TestAgentRouter(unittest.TestCase):

    def test_career(self):

        route = AgentRouter.detect_route(

            "Quero aprender Python para conseguir emprego."

        )

        self.assertEqual(route, "career_guidance")

    def test_mental(self):

        route = AgentRouter.detect_route(

            "Estou muito triste e ansioso."

        )

        self.assertEqual(route, "mental_health")

    def test_default(self):

        route = AgentRouter.detect_route(

            "Olá"

        )

        self.assertEqual(route, "system_prompt")


if __name__ == "__main__":

    unittest.main()

def route_request(user_input: str) -> str:
    """
    Decide qual agente usar baseado no input do usuário.
    """

    text = user_input.lower()

    if any(word in text for word in ["emprego", "vaga", "carreira", "job"]):
        return "career"

    if any(word in text for word in ["triste", "ansioso", "stress", "saúde", "mental"]):
        return "mental"

    return "system"

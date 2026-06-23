from pathlib import Path

def load_prompt(file_name: str) -> str:
    """
    Carrega prompts .md da pasta prompts
    """

    base_path = Path(__file__).resolve().parent.parent / "prompts"
    file_path = base_path / file_name

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

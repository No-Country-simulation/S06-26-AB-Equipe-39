"""Catálogo mockado de trilhas, vagas e respostas de bem-estar.

Tudo aqui é estático e serve apenas à primeira fase. As personas (Mateus,
Camila, Alejandro) guiam os exemplos — ver docs/personas.md.
"""

# --- Trilhas e vagas por área de tecnologia -------------------------------------
# Cada área mapeia o gap típico, a trilha recomendada e vagas compatíveis.
# A chave é casada por palavra-chave contra o campo "perfil" do request.

CATALOGO_AREAS: dict[str, dict] = {
    "engenharia": {
        "gap_itens": ["Git avançado", "Testes automatizados", "Inglês técnico"],
        "trilha_sugerida": "Fundamentos de Cloud — Programa GEAR (Google Cloud)",
        "vagas": [
            {"titulo": "Programador Júnior", "empresa": "TechAO", "match": 70},
            {"titulo": "Administrador de Redes", "empresa": "NetLuanda", "match": 65},
        ],
    },
    "gestao": {
        "gap_itens": ["Certificação Scrum", "Métricas ágeis", "Ferramentas de PMO"],
        "trilha_sugerida": "Metodologias Ágeis para Produto — Programa ONE (Oracle & Alura)",
        "vagas": [
            {"titulo": "Estágio em Projetos (PMO)", "empresa": "AgileBR", "match": 72},
            {"titulo": "Assistente de Product Owner", "empresa": "StartupSP", "match": 68},
        ],
    },
    "design": {
        "gap_itens": ["Design de produto digital", "Arquitetura de informação", "Portfólio de UX"],
        "trilha_sugerida": "UI/UX para Produtos Digitais — trilha de Design aplicado",
        "vagas": [
            {"titulo": "UI/UX Designer Júnior", "empresa": "ProdutoLatam", "match": 71},
            {"titulo": "Designer de Produto", "empresa": "Medellín Labs", "match": 64},
        ],
    },
}

# Resposta padrão quando a área não é reconhecida.
CATALOGO_DEFAULT: dict = {
    "gap_itens": ["Portfólio prático", "Networking na área", "Inglês técnico"],
    "trilha_sugerida": "Trilha introdutória — descubra seu caminho na tecnologia",
    "vagas": [
        {"titulo": "Vaga de entrada em Tecnologia", "empresa": "BiT Partners", "match": 60},
    ],
}

# Palavras-chave -> área do catálogo. Casado contra o "perfil" em minúsculas.
PALAVRAS_CHAVE_AREA: dict[str, str] = {
    "engenharia": "engenharia",
    "informática": "engenharia",
    "informatica": "engenharia",
    "programa": "engenharia",
    "software": "engenharia",
    "desenvolv": "engenharia",
    "redes": "engenharia",
    "gestão": "gestao",
    "gestao": "gestao",
    "projeto": "gestao",
    "scrum": "gestao",
    "product": "gestao",
    "produto": "gestao",
    "ágil": "gestao",
    "agil": "gestao",
    "design": "design",
    "ui": "design",
    "ux": "design",
    "gráfico": "design",
    "grafico": "design",
}


# --- Respostas de bem-estar por humor -------------------------------------------
# Mensagem acolhedora + ação concreta e humana, por estado emocional.
RESPOSTAS_HUMOR: dict[str, dict[str, str]] = {
    "feliz": {
        "mensagem": "Que bom te ver assim! Aproveite essa energia.",
        "acao_sugerida": "Que tal registrar uma pequena vitória da semana num caderno?",
    },
    "cansado": {
        "mensagem": "Descansar também é produtivo. Você merece uma pausa.",
        "acao_sugerida": "Experimente 10 minutos longe das telas, de olhos fechados.",
    },
    "triste": {
        "mensagem": "Obrigado por compartilhar. Dias assim passam — você não está sozinho.",
        "acao_sugerida": "Ouça um episódio de podcast que costuma te confortar.",
    },
    "ansioso": {
        "mensagem": "Respira. Um passo de cada vez é suficiente por agora.",
        "acao_sugerida": "Que tal uma caminhada curta de 10 minutos ao ar livre agora?",
    },
    "sobrecarregado": {
        "mensagem": "É muita coisa ao mesmo tempo. Vamos aliviar um pouco a carga.",
        "acao_sugerida": "Escolha só UMA tarefa pequena para concluir hoje. O resto pode esperar.",
    },
}

# Resposta padrão quando o humor não é reconhecido.
RESPOSTA_HUMOR_DEFAULT: dict[str, str] = {
    "mensagem": "Obrigado por fazer seu check-in de hoje.",
    "acao_sugerida": "Reserve um momento para você: um copo d'água e três respirações fundas.",
}

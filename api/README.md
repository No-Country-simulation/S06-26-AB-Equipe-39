# api/ — Backend

API do App BiT. Responsável pelos endpoints, validação, persistência e por orquestrar o
agente de IA.

## Endpoints

- `POST /orientar` — gap percentual + trilha + vagas
- `POST /saude` — check-in emocional + ação sugerida (+ derivação CVV)

Contrato completo: [../docs/api.md](../docs/api.md).

## Estrutura

```text
api/
├── src/      # código-fonte da API
└── tests/    # testes automatizados
```

## Stack (livre)

Escolha o que a equipe domina — Node.js (Express/Fastify), FastAPI (Python),
Spring Boot (Java)… Veja exemplos de execução em [../docs/setup.md](../docs/setup.md).

## Começar (Dia 1)

Comece retornando dados **mockados** no formato do contrato para destravar o front.

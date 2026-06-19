# agent/ — Agente de IA

Lógica do agente de IA do App BiT: matching perfil↔vagas/trilhas e o agente de
saúde mental.

## Responsabilidades

- Cruzar perfil do usuário com trilhas e vagas → `gap_percentual`, `trilha_sugerida`.
- Detectar estado emocional no check-in → `mensagem`, `acao_sugerida`.
- Acionar derivação ao **CVV** quando `nota_semanal < 4`.

## Estrutura

```text
agent/
├── prompts/   # prompts versionados (orientar, saúde…)
└── tests/     # casos de teste do agente
```

## ⚠️ Atenção — agente sensível

O agente de saúde mental é **sensível**. Teste exaustivamente os limiares (em especial o
corte em `nota < 4`) **antes** de qualquer integração em produção. Diretrizes completas
em [../docs/saude-mental.md](../docs/saude-mental.md).

## Começar (Dia 1)

Comece com um **prompt isolado**, revisado por mais de uma pessoa, antes de integrar à
API.

> 🔐 Nunca suba chaves de API. Use `.env` (ver [../.env.example](../.env.example)).

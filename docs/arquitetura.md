# Arquitetura

> O stack **não é obrigatório**. Cada equipe escolhe a tecnologia que melhor domina
> (React, Vue, Node.js, Spring Boot, Python, Java…). Este documento descreve a
> arquitetura de referência e o **contrato de integração** — que deve ser acordado no
> **Dia 1**.

## Visão de componentes

```text
┌──────────────────────────────────────────────────────────────────┐
│                         CLIENTE (PWA)                            │
│  Web App responsiva — funciona no celular e no desktop          │
│  • Onboarding  • Home  • Tela funcional (orientar OU saúde)     │
│  • Geolocalização (lat/lng)  • Suporte offline (opcional)       │
└───────────────────────────┬──────────────────────────────────────┘
                            │ HTTPS / JSON
                            ▼
┌──────────────────────────────────────────────────────────────────┐
│                          API / BACKEND                           │
│  POST /orientar  → gap percentual, trilha, vagas                 │
│  POST /saude     → mensagem, ação sugerida, derivação CVV        │
│  (auth, validação, persistência de perfil)                      │
└──────────┬────────────────────────────────┬──────────────────────┘
           │                                │
           ▼                                ▼
┌────────────────────┐          ┌────────────────────────────────┐
│   AGENTE DE IA     │          │   DADOS / DATASET              │
│  • Cruza perfil ×  │          │  • Perfis de usuário (DB)      │
│    trilhas/vagas   │          │  • Trilhas e vagas (mock/real) │
│  • Detecta humor   │          │  • Vísent CDRView (geo/rede)   │
│  • Sugere ações    │          │                                │
└────────────────────┘          └────────────────────────────────┘
```

## Camadas

| Camada | Responsabilidade |
|--------|------------------|
| **Front-end (PWA)** | Onboarding, home, tela funcional, geolocalização, modo offline |
| **API / Backend** | Endpoints `/orientar` e `/saude`, validação, persistência |
| **Agente de IA** | Matching perfil↔vaga, geração de trilha, detecção de humor, sugestões |
| **Dados** | Perfis, catálogo de trilhas/vagas, dataset CDRView |

## Contrato de integração (Dia 1)

A primeira tarefa da equipe é fixar o **contrato** entre as frentes para que possam
trabalhar em paralelo:

1. **Interface** consome `/orientar` e `/saude` com payloads definidos em
   [api.md](api.md).
2. **API** retorna dados **mockados** no início (mesmo formato do contrato), liberando o
   front para desenvolver sem esperar o backend completo.
3. **Agente** começa com um **prompt isolado** e evolui para integração via API.

> Comece pelo contrato de integração no **Dia 1** — é o que permite as três frentes
> avançarem sem bloqueios.

## Divisão de frentes

- **Interface:** tela de onboarding + home + uma tela funcional.
- **API:** `/orientar` retornando dados mockados → depois dados reais.
- **Agente:** primeiro prompt isolado → integração.

## Stack sugerido (exemplos)

| Frente | Opções comuns |
|--------|---------------|
| Front-end | React, Vue, Next.js (PWA) |
| Backend | Node.js (Express/Fastify), Spring Boot, FastAPI (Python) |
| Banco | PostgreSQL, MongoDB, SQLite (MVP) |
| Agente de IA | Claude (Anthropic) ou outro LLM via API |
| Deploy | **Railway** ou **Render** |

## Boas práticas

- **Nunca** suba credenciais/chaves no repositório — use `.env` (ver [setup.md](setup.md)).
- O **agente de saúde mental é sensível** — teste exaustivamente antes de produção
  ([saude-mental.md](saude-mental.md)).
- Mantenha o front desacoplado da API por trás do contrato — facilita mocks e testes.

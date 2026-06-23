# api/ — Backend (FastAPI)

API do App BiT em **Python + FastAPI**. Responsável pelos endpoints, validação do
contrato e regras de negócio. **Primeira fase: dados mockados** no formato do contrato,
para destravar o front sem depender de banco nem do agente de IA.

> 📄 Documentação completa do backend: [../docs/backend.md](../docs/backend.md)
> 📄 Contrato dos endpoints: [../docs/api.md](../docs/api.md)

## Requisitos

- **Python 3.12+** (recomendado). O Python 3.14 ainda não tem wheels pré-compilados de
  `pydantic-core` — ver nota em [../docs/backend.md](../docs/backend.md#por-que-python-312).

## Como rodar

```bash
cd api

# 1. Ambiente virtual + dependências
python3.12 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 2. Subir a API (http://localhost:3000)
uvicorn app.main:app --reload --port 3000
```

- Docs interativas (Swagger UI): http://localhost:3000/docs
- Health check: http://localhost:3000/health

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/` | Raiz com ponteiros úteis |
| `GET` | `/health` | Health check (para Railway/Render) |
| `POST` | `/orientar` | Gap percentual + trilha + vagas |
| `POST` | `/saude` | Check-in emocional + ação (+ derivação CVV) |

### Exemplos

```bash
curl -X POST http://localhost:3000/orientar -H "Content-Type: application/json" \
  -d '{"usuario_id":"u_123","perfil":"Engenharia Informática","nivel":"junior","regiao":"Luanda, AO","idioma":"pt","lat":-8.8383,"lng":13.2344}'

curl -X POST http://localhost:3000/saude -H "Content-Type: application/json" \
  -d '{"usuario_id":"u_123","humor":"triste","nota_semanal":3}'
```

> ⚠️ `nota_semanal < 4` aciona `derivar_cvv: true` (situação de crise). Endpoint
> sensível — ver [../docs/saude-mental.md](../docs/saude-mental.md).

## Testes

```bash
cd api
.venv/bin/python -m pytest -q
```

## Estrutura

```text
api/
├── app/
│   ├── main.py              # FastAPI app, CORS, registro de routers
│   ├── config.py            # settings via .env (inclui regra do CVV)
│   ├── schemas/             # contrato Pydantic (orientar, saude)
│   ├── routers/             # camada HTTP (health, orientar, saude)
│   ├── services/            # regras de negócio
│   └── data/mocks.py        # catálogo mockado (1ª fase)
├── tests/                   # pytest (15 testes)
├── requirements.txt
└── pyproject.toml           # config do pytest
```

## Stack (livre)

A frente de backend escolheu **Python + FastAPI**. Esta escolha é local à pasta `api/`
e não obriga as outras frentes.

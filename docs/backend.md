# Backend — API FastAPI

Documentação da implementação do backend do App BiT, na pasta [`api/`](../api/).
Responsável: frente de **Backend**. Stack: **Python + FastAPI**.

> Esta página descreve **como o backend foi construído e por quê**. O contrato externo
> (request/response) fica em [api.md](api.md); o passo a passo de execução, em
> [setup.md](setup.md).

## Status — Fase 1 (mockada)

A primeira fase entrega a API **funcional com dados mockados**, no formato exato do
contrato. Isso cumpre o objetivo do Dia 1 (destravar o front sem depender de banco nem
do agente de IA) e atende o entregável mínimo do MVP de ter `/orientar` **e** `/saude`
respondendo.

- ✅ `POST /orientar` — gap percentual + trilha + vagas (mock por área)
- ✅ `POST /saude` — check-in emocional + ação sugerida
- ✅ Regra crítica do **CVV** (`nota_semanal < 4`) implementada de verdade
- ✅ `GET /health` e `GET /` utilitários
- ✅ CORS liberado (dev) para o front consumir
- ✅ 15 testes automatizados (pytest) passando

## Arquitetura em camadas

A lógica HTTP é separada da regra de negócio para facilitar testes e a troca futura dos
mocks por banco/agente sem mexer na camada de rede.

```text
Request → router (HTTP) → service (regra) → mocks (dados) → Response (schema)
```

| Camada | Pasta | Responsabilidade |
|--------|-------|------------------|
| Schemas | [`app/schemas/`](../api/app/schemas/) | Contrato Pydantic (validação de entrada/saída) |
| Routers | [`app/routers/`](../api/app/routers/) | Endpoints HTTP; delegam ao service |
| Services | [`app/services/`](../api/app/services/) | Regra de negócio (gap, derivação CVV) |
| Data | [`app/data/mocks.py`](../api/app/data/mocks.py) | Catálogo mockado da fase 1 |
| Config | [`app/config.py`](../api/app/config.py) | Settings via `.env` + constantes de negócio |

## Estrutura de arquivos

```text
api/
├── app/
│   ├── __init__.py          # versão do pacote
│   ├── main.py              # cria o app, CORS, registra routers
│   ├── config.py            # Settings (pydantic-settings) — lê .env
│   ├── schemas/
│   │   ├── orientar.py      # OrientarRequest / OrientarResponse / VagaCompativel
│   │   └── saude.py         # SaudeRequest / SaudeResponse
│   ├── routers/
│   │   ├── health.py        # GET /health
│   │   ├── orientar.py      # POST /orientar
│   │   └── saude.py         # POST /saude
│   ├── services/
│   │   ├── orientar_service.py
│   │   └── saude_service.py
│   └── data/
│       └── mocks.py         # trilhas/vagas por área + respostas de humor
├── tests/                   # pytest + fixtures
├── requirements.txt
├── pyproject.toml           # config do pytest (pythonpath)
└── README.md
```

## Lógica de negócio (fase 1)

### `/orientar`

1. **Identifica a área** a partir do campo `perfil` por palavras-chave
   (engenharia / gestão / design / default) — ver `PALAVRAS_CHAVE_AREA` em `mocks.py`.
2. Seleciona **trilha e vagas** do catálogo da área.
3. **Calcula o `gap_percentual`**: parte do melhor `match` entre as vagas e aplica um
   ajuste por `nivel` (mais sênior → percentual já atendido maior).
4. Retorna `gap_itens`, `trilha_sugerida`, `vagas_compativeis`, `confianca`.

As três áreas mapeiam diretamente as personas (ver [personas.md](personas.md)):
Mateus → engenharia, Camila → gestão, Alejandro → design.

### `/saude` — endpoint sensível ⚠️

1. Compara `nota_semanal` com `settings.crisis_threshold` (padrão **4**).
2. **Se `nota_semanal < 4`** → resposta de **crise**: `derivar_cvv=True`, mensagem
   acolhedora com o contato do **CVV (188 / cvv.org.br)** e `alerta` preenchido.
3. **Caso contrário** → mensagem + ação baseadas no `humor` informado (catálogo de
   humores; cai num default acolhedor se o humor não for reconhecido).

O limiar, o telefone e a URL do CVV ficam em [`config.py`](../api/app/config.py) — um
único lugar para auditar a regra. Diretrizes completas em
[saude-mental.md](saude-mental.md).

## Configuração (.env)

`config.py` usa `pydantic-settings` e lê `.env` (raiz ou `api/`). Variáveis relevantes
(ver [../.env.example](../.env.example)):

| Variável | Padrão | Uso |
|----------|--------|-----|
| `PORT` | `3000` | Porta do servidor |
| `ENVIRONMENT` | `development` | Ambiente |
| `DEFAULT_LOCALE` | `pt` | Idioma padrão (pt/es) |
| `CRISIS_THRESHOLD` | `4` | Nota abaixo da qual deriva ao CVV |
| `CVV_PHONE` | `188` | Telefone do CVV exibido na crise |
| `CVV_URL` | `https://www.cvv.org.br` | Site do CVV |

## Testes

15 testes em [`api/tests/`](../api/tests/), cobrindo contrato, lógica de área, ajuste por
nível, validação (422) e — com atenção especial — o **limiar de crise do CVV**
(parametrizado em `0, 3, 4, 10`).

```bash
cd api && .venv/bin/python -m pytest -q
```

## Decisões de implementação

### Por que `app/` em vez de `src/`

Convenção idiomática de FastAPI; o nome do pacote (`app`) torna o import previsível
(`uvicorn app.main:app`). O placeholder `src/` criado na fase de scaffolding foi
removido.

### Por que Python 3.12

O ambiente tinha Python **3.14**, mas `pydantic-core` ainda **não publica wheels** para
3.14 — a instalação tentava compilar do código-fonte (precisa de Rust) e falhava. O
projeto usa **Python 3.12.12**, estável e com wheels para todas as dependências. Os pins
em `requirements.txt` usam faixas (`>=,<`) para pegar as versões compatíveis mais
recentes.

### Dados mockados

Toda a "inteligência" da fase 1 é estática (`app/data/mocks.py`). Nas próximas fases,
os services passam a consultar banco e o agente de IA — **sem alterar o contrato**, então
o front não precisa mudar.

## Próximos passos (fases seguintes)

- [ ] Persistência do perfil do usuário (DB) e do onboarding
- [ ] Autenticação (`401`) e identificação real do `usuario_id`
- [ ] Integração com o **agente de IA** (substituir mocks do `/orientar` e `/saude`)
- [ ] Integração com o **dataset Vísent CDRView** (recursos por geolocalização) —
      ver [dataset-cdrview.md](dataset-cdrview.md)
- [ ] Restringir CORS ao domínio do front
- [ ] Deploy em Railway/Render com variáveis de ambiente seguras

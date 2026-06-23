# Setup Local

Como rodar o App BiT na sua máquina. O stack é livre — adapte os comandos abaixo à
tecnologia escolhida pela equipe.

## Pré-requisitos

- **Git**
- Runtime do stack escolhido (ex.: **Node.js 18+**, **Python 3.10+**, **Java 17+**)
- Um banco de dados (PostgreSQL, MongoDB ou SQLite para o MVP)
- (Opcional) Chave de API do provedor de LLM para o agente de IA

## 1. Clonar o repositório

```bash
git clone https://github.com/<org>/S06-26-AB-Equipe-39.git
cd S06-26-AB-Equipe-39
```

## 2. Variáveis de ambiente

Copie o exemplo e preencha com suas chaves. **Nunca** suba o `.env` para o repositório.

```bash
cp .env.example .env
```

Exemplo de `.env.example`:

```dotenv
# Servidor
PORT=3000
NODE_ENV=development

# Banco de dados
DATABASE_URL=postgresql://user:pass@localhost:5432/appbit

# Agente de IA (LLM)
LLM_API_KEY=coloque-sua-chave-aqui
LLM_MODEL=claude-...

# Dataset CDRView (opcional)
CDRVIEW_PATH=./data/cdrview.csv

# Multilíngue
DEFAULT_LOCALE=pt
```

> 🔐 O `.env` já deve estar listado no `.gitignore`. **Nunca** suba credenciais ou
> chaves de API.

## 3. Instalar dependências e rodar

Neste projeto, o **backend (`api/`) é Python + FastAPI** e o **front-end (`web/`) é
Node**. Suba os dois separadamente.

### Backend — Python (FastAPI)

Implementado e funcional (ver [backend.md](backend.md)). Requer **Python 3.12+**
(o 3.14 ainda não tem wheels de `pydantic-core`).

```bash
cd api
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 3000
```

- Swagger UI: http://localhost:3000/docs
- Testes: `.venv/bin/python -m pytest -q`

### Front-end — Node (PWA)

```bash
cd web && npm install && npm run dev    # Front em http://localhost:5173
```

## 4. Testar os endpoints

```bash
# /orientar
curl -X POST http://localhost:3000/orientar \
  -H "Content-Type: application/json" \
  -d '{"usuario_id":"u_123","perfil":"Engenharia Informática","nivel":"junior","regiao":"Luanda, AO","idioma":"pt","lat":-8.8383,"lng":13.2344}'

# /saude
curl -X POST http://localhost:3000/saude \
  -H "Content-Type: application/json" \
  -d '{"usuario_id":"u_123","humor":"ansioso","nota_semanal":3,"contexto":"semana de provas"}'
```

Veja o contrato completo em [api.md](api.md).

## 5. Deploy (MVP)

Recomendado: **Railway** ou **Render**.

1. Conecte o repositório GitHub à plataforma.
2. Configure as variáveis de ambiente no painel (as mesmas do `.env`, sem subir o arquivo).
3. Defina o comando de build e start conforme o stack.
4. Faça o deploy e valide os endpoints em produção.

> ⚠️ Antes de subir o agente de saúde mental para produção, **teste exaustivamente** —
> ver [saude-mental.md](saude-mental.md).

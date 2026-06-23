# API — Endpoints

Contrato de integração da API do App BiT. Defina e congele este contrato no **Dia 1**
para que front, back e agente trabalhem em paralelo.

> ✅ **Implementado** (Fase 1, dados mockados) — backend em Python/FastAPI. Como rodar e
> detalhes da implementação em [backend.md](backend.md). Docs interativas (Swagger) em
> `http://localhost:3000/docs` com o servidor no ar.

Base URL (local): `http://localhost:3000`
Formato: `application/json`

---

## `POST /orientar`

Cruza o perfil do usuário com trilhas e vagas, retornando o **gap percentual** e o
**próximo passo concreto**.

### Request

```json
{
  "usuario_id": "u_123",
  "perfil": "Engenharia Informática",
  "nivel": "junior",
  "regiao": "Luanda, AO",
  "idioma": "pt",
  "lat": -8.8383,
  "lng": 13.2344
}
```

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `usuario_id` | string | Identificador do usuário |
| `perfil` | string | Formação/área principal |
| `nivel` | string | Nível profissional (ex.: `junior`, `pleno`) |
| `regiao` | string | Região do usuário (cidade, país) |
| `idioma` | string | Idioma preferido (`pt`, `es`) |
| `lat` | number | Latitude (geolocalização) |
| `lng` | number | Longitude (geolocalização) |

### Response

```json
{
  "gap_percentual": 70,
  "gap_itens": ["Git avançado", "Testes automatizados", "Inglês técnico"],
  "trilha_sugerida": "Fundamentos de Cloud — Programa GEAR (Google Cloud)",
  "vagas_compativeis": [
    { "titulo": "Programador Júnior", "empresa": "TechAO", "match": 70 }
  ],
  "confianca": 0.82
}
```

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `gap_percentual` | number | Quanto o usuário já atende dos requisitos (0–100) |
| `gap_itens` | string[] | Competências que faltam para fechar o gap |
| `trilha_sugerida` | string | Próximo passo concreto de formação |
| `vagas_compativeis` | object[] | Vagas com match percentual |
| `confianca` | number | Confiança do agente na recomendação (0–1) |

---

## `POST /saude`

Recebe o check-in emocional do usuário e devolve uma mensagem acolhedora + ação
sugerida. **Sensível** — ver [saude-mental.md](saude-mental.md).

### Request

```json
{
  "usuario_id": "u_123",
  "humor": "ansioso",
  "nota_semanal": 3,
  "contexto": "semana de provas e sem retorno de vagas"
}
```

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `usuario_id` | string | Identificador do usuário |
| `humor` | string | Emoji/estado: feliz, cansado, triste, ansioso, sobrecarregado… |
| `nota_semanal` | number | Nota de bem-estar da semana (0–10) |
| `contexto` | string | Texto livre opcional com o contexto do usuário |

### Response

```json
{
  "mensagem": "Obrigado por compartilhar. Semanas assim pesam — você não está sozinho.",
  "acao_sugerida": "Que tal uma caminhada curta de 10 minutos ao ar livre agora?",
  "derivar_cvv": true,
  "nota_atual": 3,
  "alerta": "Nota abaixo de 4 — derivação ao CVV acionada."
}
```

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `mensagem` | string | Resposta acolhedora do agente |
| `acao_sugerida` | string | Ação concreta e humana de bem-estar |
| `derivar_cvv` | boolean | `true` quando `nota_semanal < 4` (situação de crise) |
| `nota_atual` | number | Nota registrada no check-in |
| `alerta` | string\|null | Mensagem de alerta interno, quando aplicável |

> ⚠️ **Regra crítica:** `nota_semanal < 4` **sempre** aciona `derivar_cvv: true`. A UI
> deve exibir o contato do **CVV (188 / cvv.org.br)** de forma clara e acolhedora.

---

## Códigos de status sugeridos

| Código | Significado |
|--------|-------------|
| `200` | Sucesso |
| `400` | Payload inválido (campos obrigatórios ausentes) |
| `401` | Não autenticado |
| `500` | Erro interno |

## Observações

- Comece com respostas **mockadas** no mesmo formato — isso destrava o front no Dia 1.
- Valide os campos obrigatórios e trate `idioma` para suporte multilíngue (PT/ES).

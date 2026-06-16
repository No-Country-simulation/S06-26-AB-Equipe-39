# App BiT — Orientação Pessoal 360° (B2C)

> Ecossistema web responsivo (PWA) com agente de IA para apoiar pessoas de grupos
> sub-representados em **cinco dimensões**: formação, empregabilidade, experiências,
> mentorias e saúde mental.

**Hackathon NoCountry** · Setor: EdTech / HRTech · Web App Development
**Equipe 39** — `S06-26-AB-Equipe-39` · Semana 2 de 5

---

## 🎯 O problema

Pessoas de grupos sub-representados enfrentam barreiras **simultâneas** de emprego,
formação e saúde mental, sem um suporte integrado e humanizado. Uma barreira leva à
outra (ciclo de exclusão), e falta o senso de pertencimento no mercado de tecnologia.

O App BiT não é só um app de vagas, nem só uma plataforma de cursos, nem só uma
solução de bem-estar. É um **ecossistema 360°** que reúne, num só lugar, o suporte
para que cada pessoa possa **se desenvolver, pertencer e avançar**.

## 🧩 Os 5 serviços

| # | Serviço | O que faz |
|---|---------|-----------|
| 1 | **Formações** | Trilhas personalizadas (GEAR/Google, ONE/Oracle+Alura) baseadas no gap do perfil |
| 2 | **Empregabilidade** | Match perfil ↔ vaga com gap percentual ("você atende 70%") |
| 3 | **Experiências** | Eventos e depoimentos de quem superou as mesmas barreiras |
| 4 | **Mentorias** | Networking humanizado — convite para uma prática, não só entrevista |
| 5 | **Saúde Mental** | Check-in diário por emojis + ações concretas; deriva ao CVV em crise |

## 🚀 Início rápido

```bash
# 1. Clone o repositório
git clone https://github.com/<org>/S06-26-AB-Equipe-39.git
cd S06-26-AB-Equipe-39

# 2. Configure as variáveis de ambiente
cp .env.example .env   # edite com suas chaves

# 3. Suba a API e o front (ver docs/setup.md para detalhes do stack escolhido)
```

> O stack **não é obrigatório** — cada equipe escolhe o que melhor domina (React, Vue,
> Node.js, Spring Boot, Python, Java…). Instruções completas em
> [docs/setup.md](docs/setup.md).

### Exemplo de request/response

```bash
curl -X POST http://localhost:3000/orientar \
  -H "Content-Type: application/json" \
  -d '{
    "usuario_id": "u_123",
    "perfil": "Engenharia Informática",
    "nivel": "junior",
    "regiao": "Luanda, AO",
    "idioma": "pt",
    "lat": -8.8383, "lng": 13.2344
  }'
```

```json
{
  "gap_percentual": 70,
  "gap_itens": ["Git avançado", "Testes automatizados", "Inglês técnico"],
  "trilha_sugerida": "Fundamentos de Cloud — Programa GEAR (Google Cloud)",
  "vagas_compativeis": [{ "titulo": "Programador Júnior", "match": 70 }],
  "confianca": 0.82
}
```

Contrato completo dos endpoints em [docs/api.md](docs/api.md).

## 📚 Documentação

Toda a documentação está na pasta [`docs/`](docs/):

| Documento | Conteúdo |
|-----------|----------|
| [Visão Geral](docs/visao-geral.md) | Problema, proposta de valor e perfil do usuário |
| [Personas](docs/personas.md) | Mateus, Camila e Alejandro (V3) |
| [Os 5 Serviços (MVP)](docs/servicos-mvp.md) | Detalhe de cada serviço |
| [Fluxo do Usuário](docs/fluxo-usuario.md) | Jornada do onboarding ao bem-estar |
| [Arquitetura](docs/arquitetura.md) | Componentes, contrato de integração, stack |
| [API / Endpoints](docs/api.md) | `/orientar` e `/saude` — request/response |
| [Agente de Saúde Mental](docs/saude-mental.md) | Diretrizes de segurança e derivação ao CVV |
| [Dataset Vísent CDRView](docs/dataset-cdrview.md) | Geolocalização e cobertura de rede |
| [Setup Local](docs/setup.md) | Como rodar o projeto na sua máquina |
| [Roadmap & Entregáveis](docs/roadmap.md) | Escopo do MVP, opcionais e cronograma |
| [Referências Culturais](docs/referencias.md) | Filmes e livros que inspiram a proposta |
| [Contribuindo](docs/contribuindo.md) | Fluxo de trabalho da equipe |

## ✅ Escopo do MVP (mínimo exigido)

- [ ] Onboarding completo (dados pessoais e profissionais)
- [ ] Endpoint `/orientar` com gap percentual + trilha sugerida **OU** `/saude` com check-in por emojis
- [ ] Interface responsiva com **home + uma tela funcional**
- [ ] README com instruções de execução local e exemplos de request/response

## 🔐 Segurança

- **Nunca** suba credenciais ou chaves de API no repositório — use `.env` (já no `.gitignore`).
- O agente de saúde mental é **sensível**: teste exaustivamente antes de produção. Ver
  [docs/saude-mental.md](docs/saude-mental.md).

## 🚢 Deploy

MVP recomendado em **Railway** ou **Render**. Detalhes em [docs/setup.md](docs/setup.md).

## 👥 Equipe 39

Engenharia/Desenvolvimento · Gestão/Processos · Design/Experiência — os três pilares
representados pelas nossas personas.

---

_Este projeto faz parte de um desafio com uma empresa real e não implica vínculo
empregatício. A equipe decide quais funcionalidades construir e como construí-las._

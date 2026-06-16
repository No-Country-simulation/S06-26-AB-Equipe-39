# Roadmap & Entregáveis

## Funcionalidades exigidas (MVP mínimo)

- [ ] **Onboarding completo:** dados pessoais e profissionais
- [ ] **Endpoint `/orientar`** com gap percentual + trilha sugerida
      **OU** **endpoint `/saude`** com check-in via emojis + ação sugerida
- [ ] **Interface responsiva** com ao menos **home + uma tela funcional**
- [ ] **README** com instruções de execução local e exemplos de request/response

## Funcionalidades opcionais

- [ ] **Ambos os endpoints** em produção e integrados
- [ ] Integração com **dataset Vísent CDRView** (eventos por geolocalização)
- [ ] Seção **Experiências Estruturantes** com vídeos e depoimentos reais
- [ ] Módulo de **Mentorias** com agenda e convite de prática
- [ ] **Download offline** de recursos para regiões de baixa conectividade
- [ ] **Notificações push** diárias de bem-estar
- [ ] **Suporte multilíngue PT + ES**
- [ ] **Derivação automática para CVV** em situações de crise (nota < 4)

## Por onde começar — Dia 1

1. **Reunião de equipe:** apresentação, divisão de responsabilidades e alinhamento do
   **contrato de integração**.
2. **Configurar ambiente local:** repositório GitHub, arquivo `.env`, banco de dados.
3. **Dividir as frentes:**
   - Interface com tela de **onboarding**
   - API com **`/orientar` retornando dados mockados**
   - Agente com **primeiro prompt isolado**

## Cronograma do desafio

Projeto de **5 semanas** (S0 → S4). Atual: **Semana 2 de 5**.

| Semana | Foco sugerido |
|--------|---------------|
| S0 | Kickoff, contrato de integração, ambiente |
| S1 | Onboarding + endpoints mockados + esqueleto do agente |
| **S2** | **Integração real dos endpoints + UI funcional** |
| S3 | Opcionais (CDRView, mentorias, multilíngue) + testes do agente |
| S4 | Polimento, deploy, documentação final e apresentação |

## Definição de pronto (DoD)

- Endpoint funcional e testado (mock → real).
- UI responsiva validada em mobile e desktop.
- README e docs atualizados com exemplos de request/response.
- Nenhuma credencial no repositório.
- Agente de saúde mental testado exaustivamente (se incluído).

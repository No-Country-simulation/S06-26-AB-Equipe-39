# Contribuindo

Guia de trabalho da **Equipe 39** no App BiT.

## Fluxo de trabalho (Git)

1. Crie uma branch a partir de `main`:
   ```bash
   git checkout -b feat/onboarding
   ```
2. Faça commits pequenos e descritivos.
3. Abra um **Pull Request** para `main` e peça revisão de ao menos uma pessoa.
4. Faça merge após aprovação e CI verde.

## Convenção de commits (sugerida)

Use prefixos no estilo *Conventional Commits*:

| Prefixo | Uso |
|---------|-----|
| `feat:` | Nova funcionalidade |
| `fix:` | Correção de bug |
| `docs:` | Documentação |
| `style:` | Formatação (sem mudança de lógica) |
| `refactor:` | Refatoração |
| `test:` | Testes |
| `chore:` | Tarefas de manutenção |

Exemplo: `feat: adiciona endpoint /orientar com dados mockados`

## Divisão de frentes

- **Interface (Front/PWA):** onboarding, home, telas funcionais, responsividade.
- **API (Backend):** endpoints `/orientar` e `/saude`, validação, persistência.
- **Agente (IA):** prompts, matching, detecção de humor, sugestões.

Trabalhem em paralelo apoiados no **contrato de integração** (ver
[arquitetura.md](arquitetura.md) e [api.md](api.md)).

## Regras de ouro

- 🔐 **Nunca** suba credenciais, `.env` ou chaves de API.
- 🧠 O **agente de saúde mental é sensível** — toda mudança nele exige revisão extra e
  testes ([saude-mental.md](saude-mental.md)).
- 🌍 Mantenha textos preparados para **PT/ES** (multilíngue).
- 📱 Teste sempre em **mobile e desktop** (mobile-first).
- 📝 Atualize a documentação em `docs/` ao mudar contratos ou fluxos.

## Checklist de PR

- [ ] Código testado localmente
- [ ] Sem credenciais commitadas
- [ ] Docs atualizadas (se houve mudança de contrato/fluxo)
- [ ] Funciona em mobile e desktop
- [ ] Revisado por ao menos uma pessoa

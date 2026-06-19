# web/ — Front-end (PWA)

Web app responsiva (PWA) do App BiT — funciona no celular e no desktop.

## Telas (MVP)

- **Onboarding** — dados pessoais e profissionais
- **Home**
- **Uma tela funcional** — orientação (gap/trilha) **ou** saúde (check-in por emojis)

## Estrutura

```text
web/
├── src/      # componentes, telas, lógica do front
└── public/   # estáticos, manifest PWA, ícones
```

## Diretrizes

- **Mobile-first** — as personas acessam majoritariamente pelo celular.
- **UX/UI caprichado** — o Alejandro (persona Designer) é o usuário mais crítico da
  interface (ver [../docs/personas.md](../docs/personas.md)).
- **Multilíngue PT/ES** (opcional, mas recomendado).
- **Offline** para regiões de baixa conectividade (opcional — ver
  [../docs/dataset-cdrview.md](../docs/dataset-cdrview.md)).

## Stack (livre)

React, Vue, Next.js… Consome a API pelo contrato em [../docs/api.md](../docs/api.md).

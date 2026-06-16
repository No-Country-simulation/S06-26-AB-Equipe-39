# Fluxo do Usuário

A jornada do usuário no App BiT, do cadastro ao acompanhamento de bem-estar.

## Passo a passo

1. **Cria conta e preenche o perfil** pessoal e profissional completo (onboarding).
2. **App analisa o perfil** e mostra vagas compatíveis + o **gap percentual**
   ("você atende 70%").
3. **Recebe uma trilha de formação concreta** para fechar o gap identificado.
4. **Acessa mentores disponíveis** e agenda uma conversa ou uma prática.
5. **Agente de saúde mental faz o primeiro check-in:** "Como você está hoje?"
6. **Recebe sugestões de ações concretas** de bem-estar, baseadas no seu estado
   emocional e contexto regional.
7. **Visualiza eventos e recursos próximos** por geolocalização
   (dataset Vísent CDRView — ver [dataset-cdrview.md](dataset-cdrview.md)).

## Diagrama do fluxo

```text
  ┌─────────────┐
  │  Onboarding │  dados pessoais + profissionais
  └──────┬──────┘
         │
         ▼
  ┌──────────────────┐     POST /orientar
  │ Análise de perfil│ ──────────────────────► gap_percentual + vagas + trilha
  └──────┬───────────┘
         │
         ▼
  ┌──────────────┐   ┌──────────────┐   ┌────────────────────┐
  │  Formações   │   │  Mentorias   │   │  Experiências      │
  │ (trilha)     │   │ (prática)    │   │  (eventos/vídeos)  │
  └──────────────┘   └──────────────┘   └────────────────────┘
         │
         ▼
  ┌──────────────────┐     POST /saude
  │ Check-in diário  │ ──────────────────────► mensagem + ação_sugerida
  │  (emojis)        │                          (+ derivar_cvv se nota < 4)
  └──────────────────┘
         │
         ▼
  ┌──────────────────────────┐
  │ Recursos próximos por     │  geolocalização + cobertura de rede
  │ geolocalização (CDRView)  │  (sugere conteúdo offline se rede baixa)
  └──────────────────────────┘
```

## Notas de experiência

- **Mobile-first:** as personas acessam majoritariamente pelo celular (ver
  [personas.md](personas.md)). O onboarding deve ser curto e claro.
- **Tom acolhedor:** desmistificar a tecnologia; evitar excesso de jargão técnico.
- **Conectividade variável:** em regiões com cobertura baixa, oferecer conteúdo offline.

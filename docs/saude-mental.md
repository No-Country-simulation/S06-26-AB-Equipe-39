# Agente de Saúde Mental — Diretrizes

> ⚠️ **O agente de saúde mental é sensível. Teste exaustivamente antes de colocar em
> produção.** Erros aqui têm impacto humano real.

## Propósito

Acolher o usuário com um **check-in diário** e oferecer **ações concretas e humanas** de
bem-estar — sem julgar. A inspiração é o modelo dos **Alcoólicos Anônimos**: escutar sem
julgar já é o início da cura.

## Check-in via emojis

Ao entrar no app, o usuário escolhe como está se sentindo:

😀 feliz · 😴 cansado · 😢 triste · 😰 ansioso · 🥵 sobrecarregado · …

O agente detecta o estado emocional e sugere ações como:

- um capítulo de livro
- um episódio de podcast
- caminhar descalço no gramado
- uma série na Netflix
- uma caminhada sob a chuva

As sugestões devem considerar o **contexto regional** do usuário (clima, recursos
locais, conectividade — ver [dataset-cdrview.md](dataset-cdrview.md)).

## Regra de crise — derivação ao CVV 🆘

**`nota_semanal < 4` aciona obrigatoriamente `derivar_cvv: true`.**

Quando isso acontece, o app deve:

1. Exibir, de forma clara e acolhedora, o contato do **CVV — Centro de Valorização da
   Vida**:
   - **Telefone: 188** (ligação gratuita, 24h)
   - **Site: https://www.cvv.org.br**
   - Chat e e-mail disponíveis no site
2. **Nunca** minimizar o sentimento do usuário nem substituir ajuda profissional.
3. Registrar o alerta para acompanhamento (sem expor dados sensíveis).

## O que o agente NÃO deve fazer

- ❌ Dar diagnósticos clínicos ou prescrever tratamentos.
- ❌ Julgar, minimizar ("não é para tanto") ou pressionar o usuário.
- ❌ Prometer sigilo absoluto em situação de risco de vida — priorize a segurança.
- ❌ Substituir profissionais de saúde mental ou serviços de emergência.

## Boas práticas de implementação

- **Teste exaustivo** dos limiares (especialmente o corte em `nota < 4`).
- Escreva casos de teste para humores extremos e mensagens ambíguas.
- Defina um **prompt isolado** e revisado por mais de uma pessoa antes de integrar.
- Tom de voz: caloroso, breve, humano. Nunca robótico ou clínico.
- Privacidade: trate os dados de humor como sensíveis; não logue contexto pessoal em
  texto plano em produção.

## Contrato

Ver o endpoint `POST /saude` em [api.md](api.md).

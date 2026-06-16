# Os 5 Serviços (MVP)

O App BiT atua em cinco dimensões da jornada do usuário. Cada serviço pode ser
construído de forma incremental — o MVP exige ao menos um endpoint funcional
(`/orientar` **ou** `/saude`).

---

## 1. Formações 🎓

Cursos gratuitos e pagos com **trilhas personalizadas** baseadas no gap identificado no
perfil do usuário.

- Fontes de cursos gratuitos: **Programa GEAR** (Google Cloud), **Programa ONE**
  (Oracle & Alura), entre outros.
- O agente cruza o perfil do usuário com as trilhas disponíveis e recomenda o
  **próximo passo concreto**.

**Exemplo:** Mateus (Engenharia, junior) recebe *"Fundamentos de Cloud — Programa GEAR"*
porque o gap de uma vaga compatível inclui experiência em nuvem.

---

## 2. Empregabilidade 💼

**Match automático** entre perfil e vagas, com o gap exibido de forma clara:

> "Você atende **70%** dos requisitos desta vaga — veja o que falta e como resolver."

A lógica: o mercado já atende 70% das necessidades do usuário; a plataforma mostra o
**30% que falta** e oferece uma solução concreta (uma trilha do serviço de Formações).

**Modelo de negócio:** se o usuário for contratado via plataforma, o App BiT recebe um
percentual da **empresa**. O usuário **não paga nada**.

---

## 3. Experiências Estruturantes 🎤

Eventos **ao vivo e gravados** com testemunhos de pessoas que viveram trajetórias
semelhantes: CEOs, líderes e profissionais que superaram as mesmas barreiras.

- O usuário se identifica com as histórias e encontra **referências reais** de que é
  possível.
- O engajamento acontece quando a pessoa reconhece a própria dor na trajetória de outra
  e encontra ali uma saída.

---

## 4. Mentorias 🤝

**Networking humanizado** — mentores que convidam o usuário para uma **prática**, não
apenas para uma entrevista formal.

> "Você quer vir a uma prática comigo?" — uma conexão real, baseada em confiança, não em
> currículo. Outras formas de entrar no mercado além da porta convencional.

---

## 5. Saúde Mental 🧠

**Check-in diário via emojis** (feliz, cansado, triste, ansioso, sobrecarregado…) ao
entrar no app. O agente de IA detecta o estado emocional e sugere **ações concretas e
humanas**:

- um capítulo de livro
- um episódio de podcast
- caminhar descalço no gramado
- uma série na Netflix
- uma caminhada sob a chuva

A referência inspiradora é o modelo dos **Alcoólicos Anônimos** — escutar sem julgar já
é o início da cura.

> ⚠️ Em situações de crise (`nota_semanal < 4`), o agente **deriva automaticamente** para
> o **CVV — Centro de Valorização da Vida**. Ver [saude-mental.md](saude-mental.md).

---

## Resumo

| Serviço | Endpoint relacionado | Status MVP |
|---------|----------------------|------------|
| Formações | `/orientar` (`trilha_sugerida`) | Exigido (via `/orientar`) |
| Empregabilidade | `/orientar` (`gap_percentual`, `vagas_compativeis`) | Exigido (via `/orientar`) |
| Experiências | — (tela/seção) | Opcional |
| Mentorias | — (agenda/convite) | Opcional |
| Saúde Mental | `/saude` | Exigido (alternativa a `/orientar`) |

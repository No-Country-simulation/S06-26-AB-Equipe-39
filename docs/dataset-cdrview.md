# Dataset Vísent CDRView

Dados de **concentração de pessoas por zona** + **cobertura de rede ERB (5G/4G/3G)** com
coordenadas reais de antenas (Anatel). Os dados são **emulados, mas com coordenadas
reais**.

- **Repositório:** https://github.com/wongola-bit/appbit
- Inclui **README** e **dicionário de colunas**.

## Uso neste desafio

Mostrar **eventos e recursos próximos** conforme a **zona** e a **conectividade** do
usuário:

- Cruzar a geolocalização do usuário (`lat`, `lng`) com as zonas do dataset.
- Recomendar eventos/recursos próximos.
- Se a **cobertura de rede for baixa** na região, o agente pode sugerir **conteúdo
  offline** para garantir acesso mesmo sem internet estável.

## Conexão com as personas

A conectividade variável é uma dor concreta das personas:

- **Mateus (Luanda):** depende de dados móveis que esgotam rápido → priorizar conteúdo
  leve e offline.
- **Camila (Zona Leste/SP):** rede 4G instável → degradar a experiência graciosamente.
- **Alejandro (Comuna 13/Medellín):** conexão estável só em pontos comunitários →
  permitir download para consumo no trajeto.

## Como integrar (sugestão)

1. Baixe o dataset do repositório oficial e leia o **dicionário de colunas**.
2. Carregue os dados de zonas e cobertura num serviço/consulta do backend.
3. No `/orientar` (ou endpoint dedicado de recursos), use `lat`/`lng` para encontrar a
   zona e o nível de cobertura.
4. Ajuste as recomendações: cobertura alta → conteúdo em streaming; cobertura baixa →
   conteúdo offline.

> Integração com o CDRView é **opcional** no MVP, mas agrega muito valor à dimensão de
> geolocalização e acessibilidade.

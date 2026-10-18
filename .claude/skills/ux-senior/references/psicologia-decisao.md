# Psicologia da Decisão — por que a página funciona (ou não)

Use isto pra **justificar escolhas** e pra diagnosticar. Não é enfeite acadêmico: é o que separa
"acho que fica melhor assim" de um argumento que o Richard pode levar pro cliente.

Aviso de honestidade: esses princípios explicam tendências de comportamento, não leis. Servem pra
priorizar hipóteses — não pra prometer número. Quem promete "+37% de conversão trocando a cor do
botão" está vendendo, não medindo.

---

## 1. Comportamento = motivação + facilidade + gatilho (Fogg)

Uma ação acontece quando a pessoa **quer o suficiente**, consegue **fazer com facilidade
suficiente**, e existe um **gatilho** naquele momento. Faltando um dos três, não acontece.

Consequência operacional — a ordem de ataque quando a conversão está baixa:

1. **Facilidade primeiro.** É mais barata, mais previsível e não depende de convencer ninguém.
   Menos campos, menos passos, menos decisões, botão maior e mais perto do polegar.
2. **Gatilho depois.** O CTA existe, está visível no momento certo, e diz o que faz.
3. **Motivação por último.** Copy, prova e oferta — mais caro de mudar e mais fácil de errar.

Página com motivação altíssima e fricção alta (formulário de 11 campos) converte pior que uma
promessa morna com um botão de WhatsApp. É o padrão mais recorrente em auditoria.

## 2. Carga cognitiva

Toda informação na tela consome atenção. Atenção gasta em entender o layout não sobra pra decidir.

- Agrupe o que é relacionado; separe o que não é. Proximidade comunica relação antes de qualquer
  texto explicar.
- Uma ideia por seção. Duas ideias competindo = nenhuma lembrada.
- Padrões conhecidos (menu no topo, logo à esquerda, carrinho à direita) são grátis; reinventá-los
  cobra atenção que você queria pra conversão. Gaste a originalidade na estética, não na navegação.

## 3. Custo da escolha (Hick)

Quanto mais opções, mais demorada a decisão — e "decisão demorada" na web significa "decisão adiada
pra nunca".

- Três planos, não sete. Se precisa de mais, agrupe e destaque um recomendado.
- Um CTA primário por seção. Secundário no máximo, visualmente rebaixado.
- Menu enxuto em landing. Cada item é uma rota de fuga.
- Formulário: campo opcional ainda é uma decisão ("preencho ou não?"). Se é opcional, questione se
  precisa existir.

## 4. Alvo e distância (Fitts)

O tempo pra atingir um alvo cresce com a distância e diminui com o tamanho. No celular isso é
literal e físico:

- Alvo de toque **≥ 44×44px**, com espaço entre alvos (dois botões colados geram toque errado, e
  toque errado gera desistência).
- Botão importante dentro da zona confortável do polegar (ver `ux-mobile.md`).
- Link de texto curto no meio de um parágrafo é um alvo ruim. Se é ação importante, vira botão.

## 5. Efeito de isolamento (Von Restorff)

O elemento visualmente diferente do entorno é o que se lembra e o que se clica. Isso transforma a
cor do CTA em **recurso escasso**:

- A cor de ação é **exclusiva** do CTA. Se o mesmo laranja aparece em ícone, borda, tag e link, o
  botão vira paisagem.
- Vale pro tamanho e pro espaço em volta: respiro ao redor do botão é o que faz ele existir.
- Corolário: página com cinco elementos "gritando" não tem nenhum destaque — tem ruído.

## 6. Ancoragem e enquadramento

O primeiro número visto vira a régua de todos os outros.

- Mostrar o plano mais caro primeiro faz o do meio parecer razoável.
- Comparar com o custo do problema ("R$ 380/mês de conta de luz") ancora melhor que comparar com
  concorrente.
- Enquadramento importa: "12x de R$ 97" e "R$ 1.164" são o mesmo valor com percepções diferentes —
  escolha com intenção, e **sem esconder o total**, que aí vira problema de confiança e de CDC.

## 7. Aversão à perda

Perder pesa mais que ganhar o equivalente. Isso é uma ferramenta afiada — e por isso perigosa:

- **Ético e eficaz:** tornar visível o custo de continuar como está ("cada mês sem regularizar é
  mais imposto pago a mais"). É verdade, e ajuda a decidir.
- **Antiético e burro:** escassez fabricada, contador falso, "restam 2 vagas" perpétuo. Quando
  descoberto — e é descoberto — destrói a confiança que o resto da página construiu, e configura
  publicidade enganosa. Ver `confianca-e-risco.md`.

Regra: **só use urgência que existe de verdade.** Turma que fecha, agenda que enche, preço que sobe
na data X. Se não existe, não invente — construa desejo em vez de medo.

## 8. Prova social

As pessoas usam o comportamento dos outros como atalho quando estão inseguras — e insegurança é
exatamente o estado de quem está decidindo.

Força, do mais forte pro mais fraco:
1. Resultado específico e verificável de alguém parecido com o visitante (mesma cidade, mesmo
   problema, mesma idade).
2. Depoimento com nome, rosto e contexto.
3. Números reais ("2.400 atendimentos", "8 anos").
4. Logos de clientes/parceiros.
5. Estrelas e contagem de avaliação.
6. "Milhares de clientes satisfeitos" — genérico, próximo de zero.

Semelhança vence volume: um depoimento de alguém igual ao visitante convence mais que cem
depoimentos de estranhos.

## 9. Progresso e conclusão

Tarefa começada cria desconforto até ser concluída — o que faz **formulário multi-etapa com
indicador de progresso** converter melhor que uma parede de campos, mesmo com o mesmo número total
de campos.

- Comece pelo campo mais fácil e menos invasivo (nome antes de telefone; telefone antes de CPF).
- Mostre "Etapa 1 de 3" ou uma barra. Progresso visível é o que mantém a pessoa dentro.
- Não abuse: fatiar 3 campos em 3 telas é fricção, não progresso. Multi-etapa compensa a partir de
  ~6 campos, ou quando há campos sensíveis.

## 10. Efeito de mera exposição e consistência

Repetir a mesma promessa, com as mesmas palavras, do anúncio ao botão, aumenta fluência e confiança.
Sinônimo criativo a cada seção parece rico pro redator e confuso pro visitante. Escolha o termo e
repita — a página não é um exercício de vocabulário.

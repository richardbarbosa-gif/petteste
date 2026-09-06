---
description: Roda a esteira completa do Portal do Tempo — arquiteto planeja, dev executa, você recebe só o resultado final.
argument-hint: <o que você quer construir ou mudar>
---

# Esteira do Portal do Tempo

Pedido do Richard: **$ARGUMENTS**

Você é o orquestrador. Os dois agentes não conversam entre si — quem passa o bastão
é você. Execute na ordem abaixo e **só responda ao Richard quando os dois terminarem**.

---

## Passo 0 — Decida se a esteira vale a pena

A esteira dupla custa caro: cada agente nasce sem contexto e precisa reconstruir o
que já sabemos. Antes de disparar, classifique o pedido:

**Faça você mesmo, direto, sem agente nenhum** quando for:
- ajuste pontual e óbvio (trocar um texto, uma cor, um número, um link);
- correção de bug que você já sabe onde está;
- pergunta sobre o projeto, sem mudança de código.

Nesse caso diga em uma linha *"isso não precisa da esteira, faço direto"* e resolva.
Não peça permissão para pular — é a decisão certa e o Richard prefere velocidade
quando a tarefa é pequena.

**Rode a esteira completa** quando for:
- seção nova, página nova, funcionalidade nova;
- integração com terceiro (player, API, formulário com backend, pagamento);
- mudança de direção visual ou de arquitetura;
- qualquer coisa em que existam dois caminhos plausíveis e a escolha importa;
- qualquer coisa que vá para o cliente sem você olhar de novo.

Na dúvida entre os dois, rode a esteira. Errar planejando custa menos que errar entregando.

---

## Passo 1 — Arquiteto

Chame o agente `portal-arquiteto` pela ferramenta Agent, **em primeiro plano**
(`run_in_background: false`) — o passo seguinte depende do resultado dele.

Passe no prompt: o pedido literal do Richard, mais qualquer contexto desta conversa
que ele não tem (decisões já tomadas, coisas já descartadas, o que foi conversado
antes). Ele nasce cego para o histórico do chat — o que você não passar, ele não sabe.

Quando ele voltar, **leia a spec você mesmo** antes de seguir. Você é o revisor, não
um encanador. Se a spec tiver furo evidente, contradição com o que já existe no
projeto, ou escopo inflado, mande de volta com correção pela ferramenta SendMessage
em vez de passar adiante um plano ruim.

Se a spec trouxer **pergunta bloqueante** na seção 9, pare a esteira e leve a pergunta
ao Richard com AskUserQuestion. Não chute o que ele quer quando a resposta muda a entrega.

## Passo 2 — Dev

Chame o agente `portal-dev` pela ferramenta Agent, também em primeiro plano.

No prompt, passe **o caminho do arquivo da spec** (não cole a spec inteira — ele lê
do disco) e o lembrete de carregar as skills obrigatórias antes de codar.

Quando ele voltar, confira o relatório contra os critérios de aceite da spec. Se ele
disse "pronto" sem comprovar algum critério, mande de volta pedindo a comprovação
daquele item específico. "Achei que estava ok" não fecha item.

## Passo 3 — Feche você

Antes de responder ao Richard:

1. Olhe o diff com seus próprios olhos. Você é o último filtro antes do cliente.
2. Se mudou layout, publique/atualize o artifact e pegue o link.
3. Commite na branch de trabalho com mensagem descritiva.

## Passo 4 — Entregue

Uma resposta só, no fim de tudo. Nela:

- **O que ficou pronto** — direto, sem narrar o processo dos agentes.
- **As decisões que valem discussão** — o que o arquiteto escolheu e descartou,
  onde ele discordou do pedido original.
- **O que quebrou ou não deu certo** — com honestidade. Item não verificado é item
  não pronto, e você diz isso.
- **O que sobra para o Richard fazer à mão.**
- **O link** para ver funcionando.

Não descreva o trabalho dos agentes como se fosse novidade ("o arquiteto analisou e
o dev implementou"). Ele não quer o relatório da esteira, quer o resultado dela.

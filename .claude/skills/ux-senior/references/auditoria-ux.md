# Auditoria de UX e Conversão — protocolo

Use quando a página já existe e "não converte", quando o Richard pede revisão, ou como entregável
comercial (auditoria é um produto vendável por si só — e costuma virar o projeto de redesign).

Princípio: **diagnóstico antes de remédio.** Refazer o visual de uma página cujo problema é o
formulário é caro, demorado e não resolve — e queima a confiança do cliente no próximo projeto.

---

## Passo 0 — Antes de olhar a página

Estabeleça o contexto, senão você audita no vácuo:

- Qual a ação principal e quantas acontecem hoje (por semana/mês)?
- De onde vem o tráfego e quanto é?
- O que o cliente acha que é o problema? (frequentemente está errado, e frequentemente aponta pra
  algo real de outro tipo)
- Alguém atende os leads que chegam, em quanto tempo?

**Se não há tráfego, não há problema de conversão — há problema de aquisição.** Diga isso antes de
auditar. Otimizar conversão de 40 visitas/mês é otimizar o irrelevante.

## Passo 1 — Rode a página como visitante

Na ordem, e anote a reação bruta antes de racionalizar:

1. **No celular, em 4G**, não no desktop com fibra.
2. **Teste dos 5 segundos**: abra, conte 5, feche. Consegue dizer o que é, pra quem e qual a ação?
3. **Teste do sumário**: leia só os títulos e botões. O argumento fica de pé?
4. **Percorra até o fim**, contando rolagens até o primeiro CTA e até o formulário.
5. **Preencha e envie o formulário de verdade.** Metade dos problemas graves aparece aqui — e uma
   quantidade nada desprezível de formulários simplesmente não entrega o lead a lugar nenhum.
6. **Clique no WhatsApp** e veja o que chega do outro lado.

## Passo 2 — Rubrica (0 a 5 por heurística)

Nota sem evidência é opinião. **Cada nota exige a evidência concreta na página.**

| # | Heurística | O que checar |
|---|---|---|
| 1 | **Clareza em 5s** | Promessa, público e ação compreensíveis sem rolar |
| 2 | **Ação dominante** | Uma ação principal; caminhos concorrentes contados |
| 3 | **Argumento na hierarquia** | Títulos contam a história; ordem adequada à consciência |
| 4 | **Prova e confiança** | Prova específica, real, e posicionada no ponto de decisão |
| 5 | **Objeções endereçadas** | As 5 objeções reais têm resposta na página |
| 6 | **Fricção do formulário** | Nº de campos, rótulos, validação, teclado, estado de envio |
| 7 | **Ergonomia mobile** | Polegar, alvo ≥44px, teclado, sem rolagem horizontal, sem hover essencial |
| 8 | **Percepção de velocidade** | A promessa pinta rápido; sem salto de layout |
| 9 | **Acessibilidade funcional** | Contraste, foco visível, alt real, navegação por teclado |
| 10 | **Ética e conformidade** | Sem prova/urgência falsa; LGPD; restrição de conselho de classe |

Escala: **0** = ausente/quebrado · **2** = existe mas atrapalha · **3** = aceitável · **5** = exemplar.

Nota abaixo de 3 em 1, 2, 6 ou 7 explica sozinha uma conversão ruim. Comece por elas.

## Passo 3 — Priorize por impacto ÷ esforço

Lista de 20 melhorias sem ordem é igual a nenhuma melhoria: o cliente lê, se assusta e não faz nada.

Classifique cada achado em **Impacto** (alto/médio/baixo na ação principal) e **Esforço** (horas /
dias / redesign), e ordene:

1. **Faça agora** — alto impacto, baixo esforço. Tipicamente: reduzir campos do formulário, trocar
   texto do botão, subir o CTA, mensagem pré-preenchida no WhatsApp, corrigir teclado do celular,
   colocar prova junto do CTA. **Quase sempre são 3 a 5 itens que resolvem a maior parte.**
2. **Planeje** — alto impacto, alto esforço: reordenar a página para a consciência certa, refazer o
   hero, reescrever a oferta.
3. **Depois** — baixo impacto, baixo esforço: polimento.
4. **Não faça** — baixo impacto, alto esforço. **Liste explicitamente.** Dizer o que não fazer é
   metade do valor da auditoria e é o que diferencia consultor de vendedor de redesign.

## Passo 4 — Relatório

Formato curto. Ninguém lê 30 páginas — e a auditoria só vale se virar ação.

```markdown
# Auditoria de conversão — [página]
Data · Contexto (tráfego, ação principal, volume atual)

## Diagnóstico em uma frase
[O gargalo principal, sem rodeio. Ex: "A página comunica bem, mas o formulário de 9 campos
no fim de 6 rolagens está barrando a maior parte dos interessados."]

## Nota por heurística
[tabela 0–5, uma linha de evidência por item]

## Os 3 consertos que mudam o resultado
1. [O quê] — por quê (o mecanismo) — esforço estimado — como medir se funcionou
2. ...
3. ...

## Melhorias secundárias
[lista curta]

## O que NÃO fazer agora
[e por quê]

## Fora do escopo da página
[oferta, tráfego, tempo de atendimento — quando for o caso]
```

## Passo 5 — Diga quando o problema não é a página

O sinal mais valioso de um sênior é saber quando o CSS não é a resposta. Levante sempre que aparecer:

- **Tráfego errado.** Anúncio prometendo A e página vendendo B. Conserta-se no anúncio, não no hero.
- **Oferta fraca ou preço fora de mercado.** Página excelente com oferta ruim continua não vendendo —
  e o cliente vai culpar o site.
- **Atendimento lento.** Lead que espera 6 horas por resposta no WhatsApp já falou com o concorrente.
  Frequentemente esse é o gargalo inteiro, e a solução é automação (`automation-senior`), não design.
- **Público errado.** Serviço regional anunciado nacionalmente, ticket incompatível com a audiência.
- **Expectativa irreal.** "A página não converte" com 2% de conversão em tráfego frio pode ser
  normal. Estabeleça a régua antes de prometer melhoria.

Diga isso com dado, não com opinião — e traga junto o que dá pra fazer na parte que é sua.

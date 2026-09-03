# Arquitetura de Conversão — como o argumento vira estrutura

Estrutura de página não é lista de seções bonitas: é **a ordem em que um argumento é aceito**. Este
documento cobre a ordem, o comportamento de leitura e as regras de arquitetura que valem sempre.
(A anatomia visual de cada seção é da `frontend-senior`; aqui é a lógica por trás dela.)

---

## A ordem do argumento muda com a consciência

Não existe "estrutura de landing page ideal". Existe a estrutura certa pro estado de quem chega
(ver `descoberta-brief-ux.md`).

**Tráfego frio (consciente do problema):**
Problema nomeado → agitação curta e honesta → solução → como funciona → prova → oferta → objeções → CTA

**Tráfego morno (consciente da solução):**
Promessa específica → diferencial → prova → método → oferta → objeções → CTA

**Tráfego quente (consciente do produto/marca):**
Oferta e CTA no topo → prova → detalhes → objeções → CTA

Erro clássico: aplicar a estrutura fria em quem já conhece a marca. A pessoa que buscou o nome da
clínica no Google não quer ler sobre o problema dela — quer o telefone.

## Como as pessoas realmente leem

Ninguém lê uma página; as pessoas **escaneiam** e decidem se vale ler. Três padrões conhecidos de
rastreamento ocular:

- **Bolo de camadas (layer-cake)** — o mais comum em página bem estruturada: os olhos pulam de
  título em título, mergulhando só onde o título prometeu algo relevante. É o padrão que você
  **quer** provocar.
- **Padrão F** — aparece em parede de texto sem hierarquia: lê a primeira linha, depois cada vez
  menos, e desiste. Sinal de que a página está mal estruturada.
- **Padrão Z / mancha** — página esparsa com pouca informação: o olho salta entre elementos de peso.

### Teste do sumário (aplique sempre)
Leia **só** os títulos, subtítulos e textos de botão, em ordem. O argumento de venda fica de pé
sozinho? Se o sentido só existe nos parágrafos, ele não é lido. Conserto: reescrever títulos pra
serem afirmações com conteúdo ("Reduza a fatura de energia em até 90%") em vez de rótulos
("Benefícios", "Sobre nós", "Nossos serviços").

Rótulo genérico como título é a forma mais comum e mais barata de perder metade da mensagem.

## Ação dominante

Uma landing existe pra uma ação. Conte, no primeiro terço da página, quantos caminhos clicáveis
competem com ela: menu com 7 itens, redes sociais, "saiba mais", telefone, WhatsApp e formulário =
seis decisões pra tomar antes da que importa.

- **Landing de campanha paga:** um caminho. Menu reduzido ou ausente, sem links de saída no hero.
- **Site institucional:** menu é legítimo (a pessoa está explorando), mas a ação principal continua
  visualmente dominante em toda página.
- Regra prática de execução: **a cor de CTA é exclusiva do CTA**. Se botão secundário, link e ícone
  usam a mesma cor, o CTA deixa de saltar. (Peça isso à `frontend-senior` como restrição de token.)

## Continuidade da promessa

O que a pessoa clicou tem que ser o que ela encontra — nas mesmas palavras.

Anúncio: "Consulta de avaliação em Marília" → título da página: "Avaliação em Marília", não
"Transforme sua vida". A quebra dessa continuidade é o vazamento invisível mais comum em tráfego
pago: o clique foi pago, a pessoa chegou, não reconheceu o lugar e voltou. O gestor de tráfego culpa
a página, o designer culpa o anúncio, e ninguém olha as duas coisas lado a lado.

O mesmo vale internamente: o texto do botão deve prever o que vem depois. "Ver planos" leva a
planos. "Falar no WhatsApp" abre o WhatsApp — não um formulário.

## Prova no ponto de decisão

Prova social funciona onde a hesitação acontece, não onde sobrou espaço no layout.

- Um depoimento **ao lado do formulário** vale mais que uma faixa de seis depoimentos no meio.
- Selo/credencial **abaixo do botão** ("CRM 12345 • 8 anos • 2.000+ atendimentos") reduz o medo no
  instante do clique.
- Faixa de logos funciona cedo (reduz risco antes do investimento de leitura), mas não substitui a
  prova adjacente ao CTA.

## Orçamento de rolagem (mobile)

No celular, o visitante decide continuar ou sair em cerca de **três rolagens**. Dentro delas
precisam caber: a promessa, um sinal de confiança e uma ação acessível.

Consequências:
- Hero de altura de tela cheia com só um título gigante gasta o orçamento inteiro na primeira
  rolagem. Deixe a próxima seção "espiar" pra sinalizar que há conteúdo.
- Vídeo institucional de 3 minutos antes de qualquer texto é um pedágio: a maioria não paga.
- Se a página é longa (venda de infoproduto), tudo bem — mas a **primeira decisão** ainda acontece
  nas três primeiras rolagens.

## Repetição de CTA

A pessoa decide em momentos diferentes: uma decide no hero, outra depois do depoimento, outra no
FAQ. Repita o CTA ao fim de cada bloco de argumento, **sempre com o mesmo texto e a mesma cara** —
variação de texto entre botões faz parecer que levam a lugares diferentes e cria hesitação.

Em página longa no mobile, um CTA fixo discreto no rodapé resolve o "onde eu clico agora?" (ver
`ux-mobile.md`).

## Anti-padrões de arquitetura

- Sequência de 6 seções idênticas de "ícone + título + frase" — o olho desiste e a página vira ruído.
- FAQ decorativo com perguntas que ninguém faz ("Vocês são bons?"), em vez das objeções reais.
- "Sobre nós" longo antes de qualquer prova de valor — interessa ao cliente, não ao visitante.
  Autoridade entra como **prova a serviço da decisão**, não como autobiografia.
- Formulário no topo antes de qualquer motivo pra preencher (só funciona em tráfego quente).
- CTA "Saiba mais" — não pede nada, não promete nada, não converte nada.

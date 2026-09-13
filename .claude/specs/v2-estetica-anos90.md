# SPEC: Portal do Tempo v2 — Direção de arte 90s e densidade de conteúdo
Data: 2026-09-06 · Pedido original: "melhore a estética sem alterar cores nem quebrar o que funciona; aumente seções; deixe top anos 90"

---

## 0. AVISO AO EXECUTOR — LEIA ANTES DE TUDO

> **Esta spec NÃO é sobre `portal-do-tempo/index.html`.**
>
> O arquivo desta entrega é **`/home/user/petteste/portal-do-tempo-v2/index.html`** (1.449 linhas).
> É uma versão paralela, com stack e estética totalmente diferentes da v1.
>
> A seção "Contexto do projeto" do seu agente (`portal-dev.md`) descreve a v1: madeira
> escura, âmbar, tokens `--ambar/--laranja/--bordo`, sem biblioteca, sem imagem externa,
> `portal-do-tempo/index.html`. **Nada disso vale aqui. Ignore integralmente.**
>
> Aqui a stack real é:
> - Tailwind CSS via CDN (`cdn.tailwindcss.com`) com `tailwind.config` inline
> - Fontes Inter + Space Grotesk + VT323 + Press Start 2P
> - Imagens externas do Unsplash
> - `fetch` para a API do Gemini no cliente
> - Paleta neon sobre quase-preto
>
> O piso de qualidade do seu agente (mobile-first, contraste, foco de teclado,
> `prefers-reduced-motion`, nada de `innerHTML` com dado de usuário, sem `id` duplicado)
> **continua valendo integralmente**. Só o contexto de projeto muda.

---

## 1. O trabalho desta entrega

Transformar uma página que hoje parece **montada com utilitários genéricos** numa página
que parece **desenhada** — sistema visual coerente de 1994 — e adicionar 6 blocos de
conteúdo que atacam objeção de compra, sem mudar um único valor de cor e sem quebrar
nenhuma função existente.

---

## 2. Leitura crítica do pedido

### Pedido vs. querido

**Pedido:** "melhore a estética, aumente seções, não mude cores, não quebre nada".

**Querido:** o Richard olhou a página e sentiu que ela é *correta mas anônima*. Ela tem
todos os ingredientes certos (paleta neon, VT323, Win95, cupom fiscal térmico, TV de tubo)
e mesmo assim parece uma landing page de SaaS 2023 pintada de amarelo. Ele não quer mais
efeito — ele quer que **o efeito pareça intencional**.

**Onde divergem:** "não altere cores" pode ser lido como "não mexa em nada visual".
Não é isso. As cores estão certas; o que está errado é **forma, ritmo e peso**. Esta spec
não toca em um hex sequer e mesmo assim muda a página inteira. Onde eu reduzo o uso de uma
cor (ex.: matar os dois títulos com gradiente `bg-clip-text`), isso é reorganização de
hierarquia, explicitamente autorizado no briefing ("pode mudar onde e com que peso uma
cor existente aparece").

### O diagnóstico honesto: 7 coisas que estão genéricas hoje

| # | O que está genérico | Por que fere a direção | O que entra |
|---|---|---|---|
| 1 | **Raio de borda macio em tudo.** 4× `rounded-3xl`, 32× `rounded-2xl`, 55× `rounded-xl` | Cantos de 16-24px são a assinatura visual de 2020-2023. Os anos 90 são bisel, chanfro e canto vivo — plástico moldado, não vidro fosco | Escala de raio colapsada (§3.1) + bisel de plástico |
| 2 | **`shadow-retro-black` é invisível.** 18 usos de `4px 4px 0 #000000` sobre `bg-void #07070a` | O recurso mais 90s do arquivo (sombra dura, sem blur) **não aparece**. Contraste sombra/fundo ≈ 1.05:1. O Richard pagou por um efeito que ninguém vê | Sombra dura colorida (`shadow-retro-yellow`/`-pink`, já definidas e com **zero uso**) |
| 3 | **Emoji como ícone: 122 ocorrências, 39 distintos** | É o marcador mais genérico que existe e, ironicamente, **é a única coisa na página que injeta cor fora da paleta** — emoji carrega cor própria e muda de desenho em cada SO (Apple ≠ Segoe ≠ Noto). Numa página cuja regra número um é "não altere cores", emoji é a violação | Sprite SVG pixel-art monocromático em `currentColor` (§3.4) |
| 4 | **A página acha que tem 4 fontes, mas ships 5.** `font-pixel` (Press Start 2P): **0 usos**. `font-mono`: **68 usos** | `font-mono` no Tailwind é a mono do sistema (SFMono/Menlo/Consolas) — uma quinta tipografia, não escolhida, que carrega a maior parte do texto pequeno da página. E paga-se o download de uma fonte pixel que não aparece | Press Start 2P ganha função definida; `font-mono` é extinto (§3.3) |
| 5 | **Separador de seção: `border-b-2 border-gray-800` repetido 7×** | Um fio cinza plano entre blocos é o default de framework. Não comunica nada | Transição em *dithering* 45° + barra de calibração de cor (§3.5) |
| 6 | **Ritmo vertical arbitrário:** py-12, py-14/md:py-20, py-16, py-16/md:py-24, py-12 | Sem escala, o olho não sabe o que é dobra principal e o que é interlúdio | Escala de 3 níveis (§3.2) |
| 7 | **Fundos chapados.** `bg-void`, `bg-surface/50`, `bg-cardBg` sem textura; único relevo é um *blur blob* no hero | Blob borrado é vocabulário de 2021, não de 1994. E a técnica de textura já existe na casa (`.thermal-paper` usa `radial-gradient` pontilhado) | Grade de fósforo, retícula meio-tom e hachura diagonal, todas em CSS puro (§3.6) |

### Os 4 pontos que você me pediu para avaliar — veredito

**1. `const apiKey = ""` — CONFIRMADO, severidade ALTA (funcional), CRÍTICA (se ele colar chave).**
Você está certo nas duas pontas. O comentário "a plataforma injeta em runtime" só vale
dentro do sandbox do Google AI Studio. No domínio do Richard, `?key=` vai vazio, a API
devolve 400, e — pior que morrer silenciosamente — o código **faz 3 retries com backoff
exponencial (1s + 2s + 4s)**, então o usuário encara *sete segundos* de "Seu Wilson está
procurando na prateleira" antes do fallback. Sete segundos de espera para uma resposta
que já estava no arquivo desde o início. Isso não é degradação graciosa, é a feature
parecendo quebrada em câmera lenta.
E se ele colar uma chave real: ela fica em texto puro num HTML público, indexável, com
cota que qualquer um esvazia. Correção dentro de escopo em §4.6 — pequena, cirúrgica,
alto retorno. **Prioridade: alta.**

**2. Tailwind via CDN — CONFIRMADO, severidade MÉDIA. Fora de escopo nesta entrega.**
Você está certo: ~120KB de JS que compila CSS em runtime, mais FOUC. Mas trocar por CSS
buildado significa rodar a CLI do Tailwind e passar a ter etapa de build — exatamente a
refatoração que o Richard pediu para não fazer agora. **Mitigação barata que entra
nesta entrega:** CSS crítico inline no `<style>` que já existe, fixando fundo e cor de
texto antes do CDN responder, para que o flash seja escuro em vez de branco (§4.7).
A troca definitiva vai para §7 (escopo negativo) como follow-up nº 1.

**3. `history.innerHTML +=` — CONFIRMADO, severidade BAIXA-MÉDIA.**
Cada mensagem re-serializa e re-parseia todo o histórico. Com 10-15 mensagens não é crise
de performance, mas é errado e tem efeito colateral real: destrói e recria nós, o que
quebra seleção de texto do usuário e qualquer estado de scroll interno. Correção:
`insertAdjacentHTML('beforeend', ...)` nos 4 pontos. É troca de método, mesmo resultado
visual, zero risco. **Entra.** (E registro o lado bom: `escapeHtml` já é aplicado no input
do usuário e `formatMarkdown` escapa antes das regex — a superfície de XSS está fechada.
Não mexa nisso.)

**4. Emoji como ícone — CONFIRMADO, severidade ALTA para a direção de arte.**
É o item nº 3 da tabela acima e o argumento mais forte é o que ninguém costuma fazer:
**emoji é violação da regra de cor do Richard**. Ver §3.4 para o escopo exato da troca —
não é purga total, é purga por função.

### Riscos que o pedido não viu (não são estética, mas eu não posso calar)

| Severidade | Achado | Onde |
|---|---|---|
| **ALTA** | O checkout é fictício e diz **"TOTAL PAGO"** e **"★ PAGO NO BALCÃO ★"** no cupom, e esvazia o carrinho. Num domínio real, o cliente acredita que comprou. Isso é vício de informação (CDC art. 30/31) | §4.6-A |
| **ALTA** | Os 3 depoimentos são inventados, com nome completo, idade, cidade e produto. Depoimento fabricado é **publicidade enganosa** (CDC art. 37) | §4.6-B |
| **MÉDIA** | As fotos são stock do Unsplash representando **peças únicas usadas**. Para produto único, a foto precisa ser da unidade real (CDC art. 30). A licença do Unsplash permite uso comercial; o problema não é licença, é correspondência | §4.6-C, §9 |
| **MÉDIA** | CNPJ fictício com formato válido no cupom (`94.199.400/0001-90`) num site de venda real | §4.6-A |
| **MÉDIA** | O marquee promete "12x no cartão", "SEDEX", "GARANTIA DE BANCADA" sem prazo. Promessa sem termo é promessa que ele vai ter que cumprir na marra | §4.4-F (FAQ), §9 |
| **BAIXA** | Newsletter coleta e-mail sem aviso de LGPD nem finalidade declarada | §4.6-D |

### O caminho alternativo que eu considerei e descartei

Cogitei **substituir as fotos por ilustração SVG pixel-art** de todas as peças, o que
resolveria CSP, CLS, peso e coerência estética de uma vez. Descartei: para um e-commerce
de peça única de R$ 490 a R$ 890, **foto real é o principal instrumento de conversão**.
Ilustração vende conceito; foto vende objeto usado. A ilustração entra como *fallback*
(§4.6-C), não como substituta.

---

## 3. Decisões tomadas (o executor NÃO decide isso)

### Regra-mãe de cor — vale para tudo abaixo

**Nenhum hex novo. Nenhum hex existente trocado.** O conjunto permitido é exatamente o
que já está no arquivo hoje:

`#07070a #101018 #151522 #c0c0c0 #000080 #1084d0 #fef000 #ff007f #00f0ff #39ff14 #8b5cf6
#ff6b00 #00ff66 #000000 #ffffff #0a0a0a #dfdfdf #808080 #404040 #0d0d14 #222235 #28283e
#faf8ef #d3cbb5 #1f1f1f` + as classes utilitárias Tailwind já presentes (`gray-*`,
`zinc-*`, `purple-*`, `red-*`, `yellow-300`, `cyan-*`, `pink-900`, `green-400/500`).

**Permitido:** variação de opacidade/alpha de um hex já existente (`rgba(254,240,0,.35)`,
`bg-neonYellow/10`) — a própria config já faz isso nos `shadow-neon-*`.
**Proibido:** qualquer outro valor. Se um bloco novo "precisa" de uma cor que não está na
lista, a resposta é não — resolva com peso, opacidade ou textura.

---

### 3.1 Forma: escala de raio e bisel

| Decisão | Alternativa descartada | Por quê |
|---|---|---|
| Colapsar a escala de raio para **3 valores**: `rounded-none` (painéis, botões, cards), `rounded-[3px]` (campos de input e chips), `rounded-full` (só bolinha de status e badge que lê como adesivo) | Manter `rounded-xl/2xl/3xl` | Canto macio é a assinatura de 2023. Canto vivo + bisel é 1994. É a mudança de maior retorno por linha alterada de toda a spec |
| **Exceções nomeadas** (mantêm raio): a moldura da TV no hero (`rounded-3xl` → `rounded-[10px]`, plástico moldado tem raio pequeno), a fita K7 (`rounded-2xl` → `rounded-[6px]`, idem), o cupom térmico (mantém `rounded-2xl` — papel amassado, não plástico) | Zerar tudo | Objeto físico simulado tem raio real. Card de UI não tem |
| **`.win95-box` passa a `rounded-none`**, e `.win95-titlebar` perde `rounded-t-xl` | Manter | Janela do Windows 95 com canto arredondado é o erro de referência mais visível da página. Win95 não tinha raio |
| Criar a classe utilitária **`.bevel`** no `<style>` existente: `box-shadow: inset 1px 1px 0 rgba(255,255,255,.07), inset -1px -1px 0 rgba(0,0,0,.65);` aplicada em todo card/painel escuro | Borda de 1px cinza | Bisel faz o card ler como **painel de plástico moldado** (faceplate de aparelho de som) em vez de card de dashboard. Usa só `#ffffff` e `#000000` com alpha — nenhuma cor nova |
| Criar **`.key`** e **`.key:active`** (tecla de aparelho de som): bisel mais forte + `translate(1px,1px)` no active. Aplicada nos 4 botões de som do hero, nos 4 botões de canal da TV e nos botões de transporte da fita | `hover:scale` genérico | Tecla de boombox afunda quando apertada. É o gesto físico que a página inteira promete e não entrega |

**Mapa de conversão obrigatório** (aplicar em todo o arquivo, HTML e strings de template do JS):

```
rounded-3xl  → rounded-none   (exceto moldura da TV → rounded-[10px])
rounded-2xl  → rounded-none   (exceto fita K7 → rounded-[6px]; cupom térmico mantém)
rounded-xl   → rounded-none em botões e painéis
             → rounded-[3px] em <input>, <select> e chips
rounded-lg   → rounded-[3px]
rounded-full → mantém APENAS em: bolinha de status (w-2 h-2), badge numérico do carrinho,
               e os 3 "semáforos" da moldura da TV. Todo o resto vira rounded-none.
```

---

### 3.2 Ritmo: escala vertical de 3 níveis

| Decisão | Alternativa descartada | Por quê |
|---|---|---|
| **Nível A (dobra principal):** `py-20 md:py-28` — hero, grade de produtos, Balcão do Seu Wilson, FAQ | py aleatório entre 12 e 24 | Sem escala não existe hierarquia; o olho lê tudo como igualmente importante |
| **Nível B (seção de apoio):** `py-14 md:py-20` — corredores, garantia, depoimentos, estado de conservação, combos, CTA final | — | — |
| **Nível C (faixa/interlúdio):** `py-8 md:py-10` — barra de confiança, toca-fitas K7, linha do tempo, na bancada | — | Faixa é respiro entre dobras, não dobra |
| Cabeçalho de seção com **medida única**: `mb-10 md:mb-14` entre título e conteúdo, em todas | mb-8/mb-14 misturados | — |
| Largura de texto corrido travada em `max-w-[65ch]` em todo parágrafo de leitura | `max-w-2xl`/`max-w-xl` variando | Medida de linha é decisão tipográfica, não de layout |

---

### 3.3 Tipografia: 4 fontes, 4 funções, zero sobra

| Fonte | Função exclusiva | Regras duras |
|---|---|---|
| **Space Grotesk** (`font-display`) | Títulos (h1–h4), preço, rótulo de botão | Peso 900 em h1/h2, 700 em h3/h4. `tracking-tight` em ≥ text-3xl |
| **Inter** (`font-sans`) | Todo texto de leitura corrida | Mínimo `text-sm` (14px). Nunca abaixo disso em parágrafo |
| **VT323** (`font-retro`) | **Só o que é leitura de tela/aparelho**: rótulo de canal da TV, mostrador da fita, contador de itens, status, valores em painel, cupom fiscal, HUD | VT323 tem altura-x baixa: **compensar +3px**. `text-xs`→`text-[15px]`, `text-sm`→`text-base`. Nunca em parágrafo |
| **Press Start 2P** (`font-pixel`) | **Ganha função agora**: (a) kicker/olho de seção, (b) rótulo de selo e etiqueta, (c) dígitos de placar da barra de confiança e da linha do tempo | Só `text-[9px]`–`text-[11px]`. Só CAIXA ALTA. Máximo 5 palavras. Nunca quebra em 3 linhas. `leading-relaxed` obrigatório (a fonte é quadrada e sufoca) |

| Decisão | Alternativa descartada | Por quê |
|---|---|---|
| **Extinguir `font-mono` das 68 ocorrências.** Cada uma vira `font-retro` (se é leitura de aparelho/tela) ou `font-sans` (se é copy de UI que precisa de legibilidade) | Manter | A mono do sistema é uma 5ª tipografia não escolhida, que muda em cada SO e carrega a maior parte do texto pequeno. Matá-la é o ganho de coerência mais barato do arquivo |
| **Remover os dois `bg-clip-text` com gradiente** (h1 do hero e "Seu Wilson"). No lugar: texto sólido `text-neonYellow` com sombra dura de texto — `text-shadow: 3px 3px 0 #000000` no h1, e a frase-chave ganhando `2px 2px 0 #ff007f` | Manter o gradiente | Título com gradiente amarelo→ciano→rosa é o tique visual nº 1 de landing page gerada em 2023. Título de pôster/fliperama dos 90 é chapado com deslocamento duro. **Reduz** o número de cores em tela — está dentro da regra |
| Kicker de seção deixa de ser `font-mono` com `//` e `●` e passa a ser **etiqueta de lombada de VHS**: bloco `bg-neonYellow text-black font-pixel text-[10px] px-2 py-1` com `.bevel` | `//` e `●` | `//` é sintaxe de código, não de 1994. Lombada de fita na prateleira é a metáfora certa da loja |
| Nenhum `text-white` puro em parágrafo. Corpo = `text-gray-300`; meta/legenda = `text-gray-400` | 5 tons de cinza em rodízio (100/200/300/400/500) | Dois tons e só |

---

### 3.4 Ícones: sprite SVG pixel-art substitui emoji (por função, não por varredura)

| Decisão | Alternativa descartada | Por quê |
|---|---|---|
| Criar **um `<svg>` oculto com `<symbol>`** logo após `<body>`, e consumir com `<use href="#i-xxx">`. Todos os símbolos monocromáticos em `fill="currentColor"`, desenhados em `viewBox="0 0 16 16"` sobre grade de pixel inteiro, com `shape-rendering="crispEdges"` | Biblioteca de ícones; fonte de ícone; emoji | (1) Herda a cor do contexto → **força a paleta em vez de furá-la**; (2) idêntico em todo SO; (3) sprite de 16×16 com canto vivo *é* linguagem de 1994; (4) zero requisição de rede — funciona sob a CSP do preview |
| **Trocar (≈35 ocorrências):** ícones de navegação, de categoria (4), de garantia (4), do cabeçalho (som/CRT/carrinho/lupa), das teclas de som do hero (4), das abas de IA (4), dos selos do rodapé (3), das setas `➔`, dos `✕` de fechar, do `▶`/`⏸` do toca-fitas, das ★ de avaliação | Purgar os 122 | Purga total estoura o escopo e força mexer em assinatura de função |
| **Manter emoji (deliberadamente):** avatares de personagem no chat (`📼` `👤` `👨🏻‍🦳`) e o parâmetro `icon` do `showToast` (~15 chamadas) | Trocar tudo | No chat, o emoji lê como *rosto*, não como ícone — é a exceção que se justifica. No toast, é argumento de função em 15 pontos: mexer é risco sem ganho visual |
| Símbolos mínimos a desenhar: `i-tape` `i-tv` `i-joystick` `i-radio` `i-vinyl` `i-cart` `i-search` `i-close` `i-arrow` `i-play` `i-pause` `i-next` `i-sound-on` `i-sound-off` `i-star` `i-box` `i-gear` `i-doc` `i-lock` `i-globe` `i-bolt` `i-chat` `i-clock` `i-tag` `i-check` | Menos símbolos, reuso forçado | 25 símbolos cobrem 100% dos pontos de troca |
| Ícone dentro de botão que já tem texto: `aria-hidden="true"` no `<svg>`. Ícone sozinho: `<title>` dentro do símbolo **não serve** — o botão recebe `aria-label` | — | Piso de acessibilidade do agente |

---

### 3.5 Assinaturas visuais — os 3 elementos que fazem a página parecer desenhada

Use **só estes três**, e só nas quantidades indicadas. Elemento de assinatura repetido em
toda seção deixa de ser assinatura e vira ruído.

**S1 — Barra de calibração (color bars).** Faixa horizontal de 10px, 7 bandas iguais em
`neonYellow / neonCyan / neonGreen / neonPink / neonPurple / neonOrange / #ffffff`,
construída com `linear-gradient` de paradas duras (sem transição suave).
É a *carta de teste* da TV brasileira no encerramento da programação — o objeto mais
90s que existe e ele é feito **inteiramente de tokens que já estão na config**.
**Usar exatamente 3 vezes:** (a) topo do `<footer>`; (b) topo da seção `#oraculo-ia`;
(c) como camada de fundo da tela da TV quando a imagem falha (§4.6-C).

**S2 — Transição em dithering.** Faixa de 24px substituindo `border-b-2 border-gray-800`
entre seções: `repeating-linear-gradient(45deg, #151522 0 2px, transparent 2px 4px)` com
máscara de opacidade de 1 → 0 no sentido da seção seguinte.
É o *checkerboard dithering* que placas de vídeo de paleta limitada usavam para simular
degradê — visualmente inconfundível como 8/16-bit e custa 6 linhas de CSS.
Substitui **todos** os `border-b-2 border-gray-800` entre seções (7 pontos).

**S3 — Sombra dura, nunca borrada.** Regra de elevação da página inteira:

| Situação | Sombra |
|---|---|
| Elemento sobre fundo claro (win95, papel térmico) | `shadow-retro-black` (4px 4px 0 #000) — funciona, mantém |
| CTA amarelo sobre fundo escuro | `shadow-retro-pink` (**já existe na config, 0 usos**) |
| Card/painel destacado sobre fundo escuro | `shadow-retro-yellow` (**já existe, 0 usos**) |
| Cyan/green precisando de offset | Adicionar `retro-cyan: '4px 4px 0px #00f0ff'` e `retro-green: '4px 4px 0px #39ff14'` à config. **Não é cor nova** — é o mesmo hex já declarado, em outra entrada de `boxShadow` |
| Elevação difusa (`shadow-2xl` ×6, `shadow-xl`, `shadow-md`, `shadow`) | **Banidos.** Substituir pela sombra dura correspondente |
| `blur-3xl` do hero | **Único blur autorizado da página.** Blur só é permitido para simular *emissão de luz* (brilho de fósforo), nunca para elevação. Reduzir opacidade em ~30% para o brilho não competir com S1 |

Motivo: gaussian blur não existia em nada impresso ou renderizado em 1994. Sombra
deslocada sólida existia em todo lugar — capa de VHS, arte de fliperama, banner de loja.

---

### 3.6 Textura e profundidade (tudo CSS puro, zero requisição)

| Decisão | Onde | Por quê |
|---|---|---|
| **Grade de fósforo**: `repeating-linear-gradient` 1px em `#222235`, célula de 32px, `opacity: .35`, aplicada como pseudo-elemento de fundo nas seções `bg-void` | Hero, grade de produtos, FAQ | Substitui o vazio chapado por uma superfície com escala. Hard-edge, não borrado |
| **Retícula meio-tom**: `radial-gradient(#28283e 1px, transparent 1px)` em célula de 6px, `opacity: .25` | Seções `bg-surface` | Mesma técnica que a `.thermal-paper` já usa — a casa já tem o vocabulário |
| **Hachura diagonal de advertência**: `repeating-linear-gradient(45deg, #fef000 0 8px, #000000 8px 16px)`, faixa de 6px | Só no bloco de escassez ("peças únicas não voltam") e na barra de progresso de restauro | Fita zebrada de aviso. Uso raro = mantém força |
| **Nenhuma textura pode reduzir contraste de texto abaixo de 4.5:1.** Textura só em fundo de seção, nunca atrás de parágrafo em `opacity` acima de .35 | — | Piso de acessibilidade |
| A `.crt-scanlines` continua **fixa e global** com o toggle atual | Não alterar | É o efeito assinatura do arquivo e já tem controle do usuário. Não mexa (só o `100vw/100vh` → `inset: 0`, §5) |

---

### 3.7 Cartão de produto — redesenho (é a peça que vende)

| Decisão | Alternativa descartada | Por quê |
|---|---|---|
| Card vira **caixa de fita na prateleira**: canto vivo, `.bevel`, borda de 2px, faixa de lombada `font-pixel` no topo com a categoria | Card genérico com raio 16 | O produto é objeto físico; o card deve ser objeto físico |
| **Grade em 2 colunas no mobile**: `grid-cols-2 sm:grid-cols-2 lg:grid-cols-4` | `grid-cols-1` no mobile | Com 1 coluna em 360px o card vira um bloco de ~500px de altura e cabe **um** produto na tela. Toda loja brasileira de celular (ML, Shopee) é 2-up. Mais produto acima da dobra = mais conversão. Dentro do card, os dois botões empilham no base e voltam lado a lado em `sm:` |
| **Adicionar linha de parcelamento**: `em até 12x no cartão`, calculada como texto fixo (não exibir valor da parcela) | `12x de R$ 40,83 sem juros` | O marquee já promete 12x e o card não repetia — vazamento de conversão. Mas anunciar valor de parcela **sem juros** é declaração que precisa ser verdadeira (CDC/Bacen). Sem confirmação do Richard, a forma segura é sem valor |
| **Adicionar selo de estado de conservação** (§3.8), lido de um campo novo `condition` em `PRODUCTS` | Continuar só com `rarity` | Hoje `rarity` mistura três eixos incompatíveis: raridade ("Raridade 9/10", "Lendário"), estado ("Revisado", "Funcional") e categoria ("Prensagem de Época"). O comprador não consegue comparar duas peças. `condition` passa a ser o eixo comparável; `rarity` continua como tempero |
| Badge de raridade: `bg-neonPink` **`text-black`** (era `text-white`) | Manter | **Contraste medido: branco sobre `#ff007f` = 3.78:1 — reprova AA para texto de 10px.** Preto sobre rosa = 5.56:1. E preto sobre magenta é mais 90s (Memphis) que branco |
| `line-clamp-1` no título → `line-clamp-2` + `min-h` fixa | Manter 1 linha | "Walkman Sony WM-FX10 com Rádio AM/FM" está sendo cortado hoje. Título cortado é produto não vendido |

---

### 3.8 Escala de estado de conservação (decisão de conteúdo — não invente outra)

Quatro níveis, nesta ordem, com estes nomes exatos:

| Selo | Significa | Cor do selo |
|---|---|---|
| **LACRADO** | Nunca aberto, embalagem original de fábrica | `neonYellow` |
| **DE GAVETA** | Uso mínimo, sem marca visível, guardado desde a época | `neonCyan` |
| **COM PÁTINA** | Funciona perfeitamente; marcas honestas de uso do tempo | `neonGreen` |
| **RESTAURADO** | Chegou com defeito e foi refeito na bancada; peças trocadas listadas | `neonOrange` |

**Mapeamento obrigatório** (derivado do `desc`/`story` que cada produto já tem — não é invenção):

| id | condition |
|---|---|
| `prod-walkman-sony` | RESTAURADO (correia de borracha nova) |
| `prod-tv-trinitron` | DE GAVETA (<400h de uso) |
| `prod-megadrive-tectoy` | DE GAVETA (guardado na caixa) |
| `prod-vinil-legiao` | COM PÁTINA |
| `prod-videocassete-gradiente` | RESTAURADO (cabeçotes desmagnetizados) |
| `prod-console-snes` | RESTAURADO (capacitores novos) |
| `prod-telefone-disco` | COM PÁTINA |
| `prod-boombox-cce` | COM PÁTINA |

Nenhum item vira LACRADO: nada no acervo atual sustenta essa afirmação, e afirmar
"lacrado" sem ser é o tipo de promessa que gera devolução.

---

### 3.9 Cabeçalho e âncoras

| Decisão | Alternativa descartada | Por quê |
|---|---|---|
| O `<aside>` do marquee deixa de ser `sticky top-0 z-50` e vira estático; o `<header>` passa de `sticky top-7` para **`sticky top-0`** | Manter e ajustar o `top-7` | O valor `top-7` (28px) não bate com a altura real do marquee (~32px por causa do badge `px-2 py-0.5`), então sobra uma fresta amarela. E, no mobile, marquee + header + campo de busca comem ~150px de uma viewport de 640px. A faixa de plantão não precisa persistir |
| Adicionar `[id] { scroll-margin-top: 6rem; }` no `<style>` | Nada | Com header fixo de 80px e `scroll-smooth` no `<html>`, **toda âncora da nav hoje aterrissa debaixo do cabeçalho**. Uma linha conserta os 5 links |
| Marquee: duplicar o **conjunto completo** de spans (A, B, A, B) | Manter 2 spans diferentes | `.marquee-track` translada -50% assumindo que a segunda metade é cópia da primeira. Como os dois spans têm textos diferentes, **a faixa dá um salto visível a cada volta**. Bug real, correção de 1 linha |

---

### 3.10 Copy — tom e ângulo

- **Voz:** primeira pessoa do plural, seca e específica, com vocabulário técnico de bancada
  (correia, cabeçote, capacitor, desmagnetizar). Nostalgia sai do *detalhe concreto*, nunca
  do adjetivo. "Correia de borracha trocada" vende; "nostalgia inesquecível" não vende.
- **Banir** de todo texto novo: "incrível", "único" como adjetivo vazio, "mergulhe",
  "experiência", "reviva a magia", ponto de exclamação em título.
- **Remover menção a fornecedor na interface:** `"GRAVAR MIXTAPE NO GEMINI"` → `"GRAVAR A FITA"`;
  `"(GEMINI 3 FLASH)"` no selo do Balcão → `"LINHA DIRETA COM O BALCÃO"`. Motivo duplo:
  quebra a ficção de 1994 e amarra a copy a uma dependência que pode estar desligada.
- **Números concretos em vez de superlativo** na barra de confiança (§4.4-A).
- Todo texto novo que afirma fato comercial (prazo, garantia, frete, voltagem) leva
  `<!-- CONFIRMAR COM O RICHARD -->` imediatamente antes.

---

### 3.11 Comportamento de JS — o que pode e o que não pode

**Pode (aditivo):**
- Funções novas: `addComboToCart(ids)`, `tuneCapsuleYear(year)`, `notifyMeAboutBench(nome)`.
- Listener novo de `keydown` para Esc fechar carrinho/modais.
- Campo novo `condition` nos objetos de `PRODUCTS`; array novo `COMBOS`, `BENCH_QUEUE`.

**Não pode:**
- Renomear qualquer `id` ou qualquer função chamada por `onclick` inline.
- Mudar assinatura de `playRetroSound`, `showToast`, `addToCart`, `switchAiTab`,
  `filterCategory`, `changeTvChannel`, `applySorting`, `renderProducts`, `applyCoupon`.
- Trocar `innerHTML` por framework de template, virtual DOM ou biblioteca.
- Introduzir qualquer `<script src>` novo.

**Animação de entrada sem tocar em JS:** carrinho e modais hoje só alternam `hidden`,
o que faz o painel *aparecer estalado*. Animação CSS reinicia sozinha quando um elemento
sai de `display:none` — então basta declarar `animation: drawerIn .18s ease-out` no painel
e `animation: modalIn .16s ease-out` no conteúdo do modal. **Zero linha de JS, entrada
animada de graça.** Só entrada; saída fica instantânea (aceito).

---

## 4. Onde mexer

Arquivo único: **`/home/user/petteste/portal-do-tempo-v2/index.html`**.
Ordem de execução por prioridade — se faltar tempo, o que está no fim cai, não o começo.

### P1 — Sistema visual (§3.1 a §3.6)
- **Âncora:** bloco `<style>` das linhas 44–74. Acrescentar ali (sem apagar nada do que existe):
  `.bevel`, `.key`, `.key:active`, `.divider-dither`, `.colorbars`, `.tex-phosphor`,
  `.tex-halftone`, `.tex-hazard`, `@keyframes drawerIn/modalIn`, `[id]{scroll-margin-top}`,
  `:focus-visible`, `option{background:#101018;color:#f3f4f6}`, bloco
  `@media (prefers-reduced-motion: reduce)`, CSS crítico de fundo.
- **Âncora:** `tailwind.config` (linhas 12–42). **Única alteração permitida:** acrescentar
  `retro-cyan` e `retro-green` em `boxShadow`. `colors` e `fontFamily` ficam **byte a byte iguais**.
- **Âncora:** sprite `<svg>` novo imediatamente após `<body ...>` (linha 76), antes do
  `<div id="crtOverlay">`, com `class="hidden"` e `aria-hidden="true"`.
- Varredura de raio, sombra e fonte em todo o HTML **e** nas strings de template do JS.

### P2 — Hero e cabeçalho
- **Âncora:** `<aside class="bg-neonYellow ...">` (l. 80) e `<header ...>` (l. 100) — §3.9.
- **Âncora:** `<section class="relative pt-10 pb-20 ...">` (l. 154).
  Sai: h1 com `bg-clip-text`; pílula `rounded-full` do kicker; botões `rounded-2xl`.
  Entra: h1 sólido com sombra dura; kicker como tarja OSD em `font-pixel`; CTAs de canto
  vivo com `shadow-retro-pink`; os 4 botões de som viram teclas `.key`.
  A moldura da TV mantém raio pequeno e ganha `.bevel` + `.colorbars` de fundo (§4.6-C).
- **Âncora:** `<input id="searchInput">` (l. 122) e o input mobile sem id (l. 148) —
  dar `id="searchInputMobile"` ao segundo (§5).

### P3 — Cartão de produto e grade
- **Âncora:** `function renderProducts()` (~l. 1152), a template string do `.map()`.
  Sai: `rounded-2xl`, `rounded-xl`, `bg-neonPink text-white`, `line-clamp-1`,
  `hover:shadow-neon-yellow`, `onerror` apontando para `placehold.co`.
  Entra: caixa de fita (§3.7), selo `condition`, linha de parcelamento, `line-clamp-2`,
  `loading="lazy" decoding="async" width height`, `onerror` com fallback SVG local.
- **Âncora:** `const PRODUCTS = [` (~l. 700) — acrescentar `condition` nos 8 objetos.
- **Âncora:** `#productsGrid` (l. 314) — classes de grade.
- **Âncora:** `function renderCartItems()` e `openCheckoutModal()` — mesma varredura de forma.

### P4 — Seções novas (6 blocos)

Ordem final da página depois desta entrega:

```
header → HERO → [A] BARRA DE CONFIANÇA → toca-fitas K7 → corredores →
#garimpos (grade) → [B] ESTADO DE CONSERVAÇÃO → [C] COMBOS DE SALA →
[D] NA BANCADA → [E] LINHA DO TEMPO → #oraculo-ia → garantia → depoimentos →
[F] FAQ → CTA newsletter → footer
```

**[A] Barra de confiança** — nível C, logo após o hero, antes de `#tocador-k7`.
*Por que ali:* é a resposta imediata à objeção que nasce no instante em que o preço de
R$ 890 aparece na cabeça de quem lê o hero. Depois da grade seria tarde.
4 itens em linha, ícone SVG + número em `font-pixel` + rótulo curto:
`TESTADA NA BANCADA` · `90 DIAS DE GARANTIA` · `BOLHA TRIPLO + SEGURO` · `PIX OU ATÉ 12X`.
Fundo `bg-surface` com `.tex-halftone`, `.bevel`, dividido por linhas verticais.
Em 360px vira grade 2×2, nunca rolagem horizontal.

**[B] Estado de conservação** — nível B, imediatamente depois de `#garimpos`.
*Por que ali:* o usuário acabou de ver 8 selos nos cards e ainda não sabe o que significam.
`id="estado-conservacao"`. 4 cartões (§3.8) com: selo, uma frase do que significa, e uma
frase do que o Portal garante naquele nível. Sem ícone decorativo — o selo é o ícone.

**[C] Combos de sala** — nível B, depois de [B]. `id="combos"`.
*Por que ali:* clássico "compre junto" — só funciona depois que a peça individual já foi
compreendida e precificada. É o único bloco desta entrega que sobe ticket médio.
3 combos, cada um com nome, os 2 produtos, a soma dos preços e um botão que chama
`addComboToCart(['id1','id2'])` (função nova que só faz laço sobre o `addToCart` existente):
- **SESSÃO DA TARDE** — TV Trinitron + Videocassete Gradiente
- **DOMINGO DE 16 BITS** — TV Trinitron + Super Nintendo Gradiente
- **SOM DA VIZINHANÇA** — Boombox CCE + Walkman Sony
Sem desconto de combo (exigiria motor de preço). A alavanca é o cupom `TETRA94` que já
existe, citado no rodapé do bloco.
**Obrigatório:** a TV Trinitron aparece em 2 combos e é peça única — cada card leva a
linha "usa a mesma TV Trinitron; é peça única". O `addToCart` já barra duplicata com toast
próprio; não reimplemente essa checagem.

**[D] Na bancada** — nível C, depois de [C]. `id="na-bancada"`.
*Por que ali:* prova que a loja está viva e que o estoque se renova, sem inventar venda.
3–4 peças "em restauro", **sem preço**, com: nome, ano, o que está sendo feito, e uma
barra de progresso com hachura `.tex-hazard` + percentual em `font-retro`.
Botão "AVISE-ME QUANDO CHEGAR" chama `notifyMeAboutBench(nome)`, que rola até o formulário
de newsletter existente, foca o campo e dispara um `showToast`.
**Decisão explícita:** eu descartei a ideia mais óbvia — um mural de "peças já vendidas" —
porque exigiria inventar vendas que não aconteceram, na mesma página que já carrega 3
depoimentos fabricados. Escassez futura é honesta; escassez retroativa inventada é fraude.

**[E] Linha do tempo 1991–1999** — nível C, imediatamente antes de `#oraculo-ia`.
*Por que ali:* é a rampa de entrada narrativa da Máquina de Crônicas — "escolha seu ano"
leva direto para "gere sua crônica".
Faixa horizontal com **exatamente os 6 anos que existem no `<select id="capsuleYear">`**
(1991, 1993, 1994, 1995, 1997, 1999). Estética de contador de videocassete / dial de rádio:
números grandes em `font-pixel`, traços de escala em `font-retro`, agulha destacando o ano
sob o cursor. Cada ano chama `tuneCapsuleYear('1994')` → seta o `select`, chama
`switchAiTab('capsule')` e rola até `#oraculo-ia`.
**Não crie anos que o select não tem** — botão que não muda nada é pior que botão nenhum.
Rolagem horizontal com `snap` no mobile; os 6 chips precisam ser alcançáveis por teclado.

**[F] FAQ — "Manual de Instruções"** — nível A, entre `#depoimentos` e o CTA final.
`id="faq"`. **É o bloco de maior retorno de conversão de toda a entrega:** o comprador de
eletrônico usado de R$ 500+ tem objeções específicas e hoje a página não responde a
nenhuma.
Implementar com **`<details>`/`<summary>` nativos**: acordeão sem uma linha de JS, funciona
com JS desligado, navegável por teclado de fábrica, e o marcador padrão pode ser trocado
por um `<svg>` que gira. Estética de manual de instruções em papel: fundo com
`.tex-halftone`, numeração em `font-pixel`, filete duro entre itens.
8 perguntas, nesta ordem (ângulo definido; o executor escreve a resposta):
1. Vocês testam mesmo antes de enviar? → bancada, o que é checado, quem checa
2. Qual a garantia e o que ela cobre? → **90 dias** `<!-- CONFIRMAR -->`, cobre funcionamento, não cobre pátina
3. É 110V ou 220V? → informado na ficha de cada peça; enviamos configurado `<!-- CONFIRMAR -->`
4. Dá para ligar videocassete/console em TV moderna? → saída RCA/AV, o que acompanha
5. Posso desistir da compra? → **direito de arrependimento de 7 dias, art. 49 do CDC** (é lei, e dizer isso converte)
6. E se chegar danificado no transporte? → embalagem, prazo para abrir chamado `<!-- CONFIRMAR -->`
7. Quanto tempo leva para chegar? → prazo por região `<!-- CONFIRMAR -->`
8. A foto é da peça de verdade? → **depende de §4.6-C**; responder com a verdade que o Richard escolher
Adicionar **JSON-LD `FAQPage`** espelhando exatamente o texto visível (nada além).

### P5 — Acessibilidade e movimento (§5)
### P6 — Correções de risco (§4.6)

### 4.6 Correções de risco (pequenas, cirúrgicas, alto retorno)

**A. Cupom fiscal não pode dizer que foi pago.**
*Âncora:* `#checkoutSuccessModal` (l. ~660) e `openCheckoutModal()`.
Só copy, a estética térmica permanece: `CUPOM FISCAL / NOTA DE BALCÃO` →
`PEDIDO REGISTRADO NO BALCÃO`; `TOTAL PAGO:` → `TOTAL DO PEDIDO:`;
`★ PAGO NO BALCÃO DO SEU WILSON ★` → `★ AGUARDANDO CONFIRMAÇÃO DE PAGAMENTO ★`;
`FORMA DE PAGAMENTO: PIX / CARTÃO` → `PAGAMENTO A COMBINAR NO ATENDIMENTO`.
Acrescentar uma linha dizendo o que acontece a seguir `<!-- CONFIRMAR -->`.
Trocar `C.G.C. 94.199.400/0001-90` por `REGISTRO DE BALCÃO Nº 0199401` — o número com
cara de CNPJ válido some.

**B. Depoimentos.** Manter o bloco e o desenho. Acrescentar, no cabeçalho da seção, a
linha `Depoimentos ilustrativos — em breve substituídos por avaliações reais de clientes.`
em `text-gray-400`. **Não invente um 4º depoimento.** Solução definitiva é do Richard.

**C. Fallback de imagem que funciona nos dois ambientes.**
*Problema:* no preview (Claude Artifacts) a CSP bloqueia `images.unsplash.com` **e**
`placehold.co`, então o `onerror` atual leva de uma imagem quebrada para outra imagem
quebrada — e o Richard não consegue avaliar o resultado.
*Solução:* pôster SVG local, um por categoria (`eletronicos`, `games`, `midia`), desenhado
em pixel-art com os tokens da paleta, embutido como `data:image/svg+xml;utf8,...`.
No `renderProducts()`: `onerror="this.onerror=null; this.src=POSTER[categoria]"`.
O `this.onerror=null` é **obrigatório** — sem ele, um data-URI malformado entra em laço.
*TV do hero:* colocar uma camada `.colorbars` + ruído em `position:absolute; inset:0` **atrás**
do `<img id="tvScreenImage">`; o `<img>` recebe `onerror="this.style.visibility='hidden'"`.
E em `changeTvChannel()`, na linha que já faz `screen.src = data.img`, acrescentar
`screen.style.visibility='visible'` — **uma expressão**, senão a TV fica presa na carta de
teste depois do primeiro erro.
Resultado: no domínio real aparecem as fotos; no preview aparece a carta de teste e os
pôsteres pixel-art. Os dois estados são bonitos.
Todos os `<img>` ganham `width`, `height`, `alt` descritivo, `loading="lazy"`
(exceto o da TV, que é above-the-fold) e `decoding="async"` — hoje **nenhum dos 4 `<img>`
estáticos tem qualquer um desses atributos**, o que produz CLS garantido.

**D. LGPD no formulário de newsletter.** Uma linha abaixo do campo: finalidade do e-mail,
frequência e como sair. Sem checkbox — para alerta de estoque solicitado pelo usuário, o
consentimento é o próprio envio, e checkbox derruba conversão.

**E. `apiKey` vazia — curto-circuito.**
*Âncora:* `callGeminiApi()` (~l. 880).
Duas alterações, ambas dentro da função (nenhum chamador muda):
1. No topo: `if (!apiKey) { await new Promise(r => setTimeout(r, 900)); throw new Error('SEM_CHAVE'); }`
   Os 900ms são deliberados — dão o beat de "linha discada" e caem no fallback, que já é
   bom, em vez de 7 segundos de falso carregamento.
2. No `catch`, **não repetir erro permanente**: só faça retry em `429` e em erro de rede.
   Em `400/401/403`, aborte na hora. Hoje toda falha custa 3 tentativas com backoff.
Acrescentar, logo acima de `const apiKey = ""`, um comentário de 3 linhas: a chave **não**
deve ser colada aí; publicar chave em HTML público expõe cota e cobrança; o caminho certo
é um proxy no servidor. **Não implemente o proxy** — está fora de escopo.

**F. Chat: `insertAdjacentHTML`.** Trocar os 4 `history.innerHTML +=` de `handleChatSubmit()`
por `history.insertAdjacentHTML('beforeend', ...)`. Mesma saída visual, sem re-parse.
**Não toque em `escapeHtml` nem em `formatMarkdown`** — estão corretos.

**G. Botões falsos da janela Win95.** Os três (`_`, `□`, `✕`) são `<button>` sem handler:
o teclado tabula para dentro de três controles mortos. Virar `<span aria-hidden="true">`
com o mesmo desenho. Nenhuma função perdida.

### 4.7 CSS crítico (mitigação do FOUC do CDN)
No topo do `<style>` da linha 44, antes de tudo:
`html,body{background:#07070a;color:#f3f4f6;font-family:Inter,system-ui,sans-serif}`.
Assim, enquanto o Tailwind do CDN não compila, a tela já está escura e não branca.
**Não** use `visibility:hidden` no body com revelação por JS: se o CDN cair, a página fica
permanentemente em branco.

---

## 5. Armadilhas mapeadas

**As 4 funções que reescrevem `className` — leia antes de restilizar qualquer uma delas.**
Se você mudar a classe no HTML e não na string do JS, o estilo se desfaz no primeiro clique
e o bug só aparece em interação (não no screenshot inicial):

| Função | O que ela sobrescreve | Classes que ela conhece |
|---|---|---|
| `changeTvChannel()` | `className` **inteiro** dos 4 botões de canal, nos dois estados | `px-2.5 py-1 bg-surface text-gray-300 font-retro text-sm rounded border border-gray-700 hover:border-neonYellow transition` / versão ativa com `bg-neonYellow text-black border-black` |
| `switchAiTab()` | add/remove em 4 botões de aba | `bg-surface` `text-gray-300` `border-gray-700` `bg-neonYellow` `text-black` `shadow-retro-black` |
| `filterCategory()` | add/remove nos 4 botões de categoria | `border-neonYellow` `shadow-retro-black` `border-gray-800` |
| `renderProducts()` / `renderCartItems()` / `openCheckoutModal()` | geram HTML inteiro por template string | tudo que estiver no card |

**Bug de estado já existente em `filterCategory`:** `#cat-todos` nasce com `border-2` e os
outros três com `border`. A função troca só a *cor* da borda, nunca a espessura — então,
depois do primeiro clique, a categoria ativa tem borda de espessura diferente conforme
qual seja. Padronize os quatro em `border-2` no HTML.

**Outras armadilhas:**
- **Salto do marquee** — os dois spans de `.marquee-track` têm conteúdo diferente e o
  `translateX(-50%)` pressupõe metades idênticas. Duplique o conjunto inteiro (A,B,A,B).
- **`id` duplicado** — hoje não há nenhum (verificado). As seções novas trazem formulários
  e campos; **não** repita `newsletterEmail`, `chatInput`, `searchInput`, `couponInput`.
  Em [D], não crie um segundo formulário de e-mail: reaproveite o da newsletter.
- **Input de busca mobile sem `id`** (l. 148) — `clearSearch()` só limpa o desktop, então o
  campo mobile fica com texto enquanto a grade já foi resetada. Dê `id="searchInputMobile"`
  e limpe os dois em `clearSearch()`.
- **Contraste — os dois números medidos que reprovam:**
  `#ffffff` sobre `#ff007f` = **3.78:1** (badge de raridade, 10px) → usar `text-black` (5.56:1).
  `text-gray-500 #6b7280` sobre `#07070a` = **4.16:1** (rodapé legal, 4 ocorrências) → `text-gray-400` (7.92:1).
  **Nunca** ponha `neonYellow` sobre `winGray` dentro da janela Win95: **1.53:1**.
  Referências aprovadas: gray-400/void 7.92 · gray-300/cardBg 12.26 · neonYellow/void 16.94 ·
  neonCyan/void 14.28 · neonPink/void 5.33 · preto/neonYellow 17.68.
- **`font-pixel` em 360px** — Press Start 2P é ~2× mais larga que Inter no mesmo tamanho.
  Um kicker de 5 palavras a 10px estoura a coluna no celular. Teste **cada** uso em 360px.
- **`font-retro` (VT323) em texto pequeno** — altura-x baixa; a 11px fica ilegível. Regra
  de +3px é obrigatória, não sugestão.
- **`prefers-reduced-motion`** — hoje nada respeita: marquee 32s infinito, `animate-pulse`
  ×5, `animate-ping` ×3, `animate-bounce`, engrenagem da fita. Bloco obrigatório:
  `@media (prefers-reduced-motion: reduce){ *,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important;scroll-behavior:auto!important} }`
  As animações novas de gaveta/modal precisam degradar para aparecer instantaneamente,
  não para não aparecer.
- **`focus:outline-none` nos inputs** — hoje 6 campos removem o outline e só trocam a cor
  da borda, o que é fraco demais para teclado. Adicione
  `:focus-visible{outline:2px solid #fef000; outline-offset:2px}` global.
- **`.crt-scanlines` usa `100vw/100vh`** — `100vw` ignora a barra de rolagem e gera overflow
  horizontal (hoje mascarado pelo `overflow-x-hidden` do body). Troque por `inset:0`.
- **`z-index`** — `.crt-scanlines` é 9999 e cobre modais e toasts (z-50). É intencional
  (a TV cobre o mundo). Nenhum elemento novo pode passar de `z-40`.
- **Peso** — o sprite SVG e as texturas CSS não podem passar de ~8KB somados. Nada de
  `<path>` com centenas de pontos: os símbolos são retângulos em grade de 16×16.
- **`.tex-*` como pseudo-elemento** — precisam de `pointer-events:none` e `z-index` abaixo
  do conteúdo, senão bloqueiam clique nos botões de categoria.
- **`escapeHtml` no `showToast`** — `title` e `message` já são escapados; o parâmetro `icon`
  é interpolado cru. Todos os chamadores passam literal. Se algum bloco novo chamar
  `showToast` com valor dinâmico no `icon`, **não** o faça.
- **`<details>` do FAQ** — só estilize `summary::-webkit-details-marker{display:none}` e
  `summary{list-style:none}`. Não substitua por acordeão em JS: perderíamos teclado grátis.

---

## 6. Critérios de aceite (verificáveis)

**Cor e não-regressão**
1. `git diff` no bloco `tailwind.config`: a chave `colors` é **idêntica**, byte a byte. A única
   diferença permitida no arquivo inteiro são duas entradas novas em `boxShadow`
   (`retro-cyan`, `retro-green`), ambas reusando hex já declarados.
2. `grep -oP '#[0-9a-fA-F]{3,8}'` no arquivo final não retorna nenhum hex fora da lista de §3.
3. Nenhum `id` removido ou renomeado: a lista de `id="..."` do arquivo antigo é subconjunto
   da do novo. Nenhum `id` duplicado (`grep -oP 'id="[^"]+"' | sort | uniq -d` vazio).
4. Toda função citada em `onclick=`/`oninput=`/`onsubmit=`/`onchange=` existe e está definida.

**Funcionalidade (roteiro manual, 12 passos, todos precisam passar)**
5. Buscar "walk" filtra para 1 item; limpar volta para 8 — **e o campo mobile também limpa**.
6. Clicar nas 4 categorias filtra corretamente e a categoria ativa fica visualmente distinta,
   **com a mesma espessura de borda** dos inativos.
7. As 5 opções de ordenação reordenam a grade.
8. Adicionar 2 itens → badge = 2; gaveta lista os 2; remover 1 → badge = 1.
9. Cupom `TETRA94` desconta R$ 30 e a linha de desconto aparece; cupom errado dá toast de erro.
10. Finalizar exibe o cupom térmico com os itens e o total corretos, e zera o carrinho.
11. Modal de produto abre, mostra dados certos, "Colocar no cesto" funciona.
12. Toggle de som muda o rótulo e silencia; toggle CRT some/volta com as scanlines.
13. Os 4 canais de TV trocam rótulo, status e imagem; **e voltam a exibir a imagem depois de
    um erro de carregamento** (testar forçando `src` inválido).
14. Tocar/pausar a fita K7 anima e para as engrenagens; trocar faixa muda os dois rótulos.
15. As 4 abas de IA alternam; cada uma produz resultado (real ou fallback) **em menos de 2s**
    quando `apiKey` está vazia.
16. `addComboToCart` põe os 2 itens do combo no carrinho; repetir cai no toast de peça única
    sem duplicar linha.
17. `tuneCapsuleYear('1994')` seleciona 1994 no `select`, abre a aba de crônica e rola até lá.

**Estética (mensurável, não opinião)**
18. `grep -c 'font-mono'` retorna **0**.
19. `grep -c 'font-pixel'` retorna **≥ 12**.
20. `grep -c 'rounded-3xl'` e `grep -c 'rounded-2xl'` retornam 0 fora das 3 exceções nomeadas em §3.1.
21. `grep -c 'shadow-2xl\|shadow-xl\|shadow-md'` retorna **0**.
22. `grep -c 'bg-clip-text'` retorna **0**.
23. `grep -c 'border-b-2 border-gray-800'` retorna 0 entre seções (substituído por `.divider-dither`).
24. Nenhum emoji nos pontos listados em §3.4 como "trocar". Contagem total de emoji cai de
    122 para **≤ 40** (só chat e argumentos de `showToast`).
25. `<use href="#i-` aparece **≥ 30** vezes.

**Acessibilidade e performance (com número)**
26. Contraste: badge de raridade ≥ 4.5:1; nenhum texto de leitura abaixo de 4.5:1; nenhum
    `text-gray-500` sobre `bg-void` no arquivo final.
27. Com `prefers-reduced-motion: reduce` ativo no DevTools, marquee, engrenagem, `animate-pulse`,
    `animate-ping` e as animações novas de gaveta/modal ficam paradas — e a página continua
    inteiramente utilizável.
28. Tab a partir do topo: todo elemento focável mostra anel amarelo visível; **nenhum foco
    aterrissa nos 3 botões falsos do Win95**.
29. Clicar em cada link da nav posiciona o título da seção **abaixo** do cabeçalho fixo, não atrás.
30. Todo `<img>` tem `alt`, `width`, `height` e `decoding`; todos exceto o da TV têm `loading="lazy"`.
31. Com a rede bloqueada para `images.unsplash.com`: os 8 cards mostram pôster pixel-art e a
    TV mostra a carta de teste. **Nenhum ícone de imagem quebrada em lugar nenhum.**
32. Sem `<script src>` novo; nenhum arquivo novo criado. O arquivo continua único.

**Renderização (obrigatório — não relate como pronto sem isto)**
33. Screenshot em 360×640, 768×1024 e 1440×900. Em 360px: nenhuma barra de rolagem horizontal,
    nenhum texto em `font-pixel` transbordando, grade de produtos em 2 colunas legíveis,
    cabeçalho ocupando no máximo 1/5 da altura da tela.
34. As 6 seções novas existem, com os `id` especificados, na ordem definida em §4-P4.
35. Console do navegador sem erro depois do roteiro completo dos 12 passos.

---

## 7. Escopo negativo — o que esta entrega NÃO faz

1. **Não troca o Tailwind CDN por CSS buildado.** É o follow-up nº 1, não é agora.
2. **Não altera nenhum valor de cor.** Nem "melhora" um hex, nem ajusta luminosidade.
3. **Não implementa proxy de API, backend, gateway de pagamento nem checkout real.**
4. **Não coloca chave de API no arquivo.** Nunca. Em nenhuma variável.
5. **Não substitui as fotos do Unsplash** por fotos reais nem remove as URLs. Só adiciona fallback.
6. **Não cria um segundo formulário de captura de e-mail** ("procura-se"/encomendas). Dois
   formulários de e-mail concorrentes na mesma página derrubam a conversão dos dois.
7. **Não cria mural de "peças vendidas"** — motivo em §4-P4[D].
8. **Não escreve depoimento novo.** Só rotula os existentes como ilustrativos.
9. **Não adiciona produto novo ao `PRODUCTS`** nem inventa preço. 8 continuam sendo 8.
10. **Não refatora `renderProducts`/`renderCartItems`** para `createElement`. `innerHTML` com
    dado interno controlado permanece — o dado de usuário já passa por `escapeHtml`.
11. **Não mexe em `escapeHtml`, `formatMarkdown`, `playRetroSound`, `toggleChiptuneMusic`
    nem em `MELODY_TRACKS`.** O motor de áudio está correto e é gesto-gated.
12. **Não adiciona biblioteca, ícone remoto, fonte nova nem analytics.**
13. **Não remove o toggle CRT nem muda seu padrão** (continua ligado por default).
14. **Não implementa animação de saída** de gaveta/modal (exigiria alterar as funções de toggle).
15. **Não adiciona seção nova ao menu de navegação do topo** — a nav já tem 4 itens e é
    `hidden xl:flex`. FAQ e Combos entram nos links do rodapé.

---

## 8. Skills que o executor deve carregar

| Skill | Motivo |
|---|---|
| `partner-senior` | Postura e roteamento. Sempre |
| `frontend-senior` | A entrega é 90% interface: sistema de forma, tipografia, grade, estados |
| `code-security-senior` | Tem `innerHTML`, chave de API, `data:` URI, `onerror` em `<img>`, dado de formulário. Nenhum desses toques pode abrir buraco |
| `performance-senior` | Sprite SVG, texturas CSS, `loading`/`decoding`/CLS, retry da API, `insertAdjacentHTML`, peso do FOUC |
| `seo-senior` | 6 seções novas com hierarquia de heading, `<details>` semântico, JSON-LD `FAQPage`, `alt` das imagens, meta description ausente |
| `copywriting` | Copy nova em 6 blocos + FAQ + reescrita do cupom fiscal. É texto que precisa vender e ao mesmo tempo não prometer o que o Richard não pode cumprir |

---

## 9. Perguntas bloqueantes

**Uma, e é de verdade:**

> **As fotos são da peça real ou são ilustrativas?**
> Isso muda a resposta 8 do FAQ, muda o texto do card e muda a exposição jurídica. Para peça
> única usada, foto de banco de imagens representando o produto vendido é vício de informação
> (CDC art. 30). Se forem ilustrativas, o site **precisa** dizer isso de forma visível — e aí
> é melhor decidir agora, porque o desenho do card muda.
> **Enquanto não houver resposta:** o executor escreve a resposta 8 do FAQ como
> `"Sim — cada peça é fotografada na bancada antes de ir para o site."` marcada com
> `<!-- CONFIRMAR COM O RICHARD -->`, e o card não recebe selo de "foto real".

**Premissas assumidas (siga sem esperar resposta; cada uma é troca de string em 1–2 lugares):**

1. **Garantia = 90 dias**, cobrindo funcionamento, não cobrindo marcas de uso. Aparece na
   barra de confiança [A] e na resposta 2 do FAQ.
2. **Direito de arrependimento = 7 dias** — não é premissa, é o art. 49 do CDC. Fica no FAQ
   independentemente do que ele decidir.
3. **Pagamento: Pix ou até 12x no cartão**, sem afirmar "sem juros" e sem exibir valor de
   parcela, porque anunciar parcela sem juros que não existe é infração.
4. **Prazo de entrega e prazo para reclamar avaria** ficam como `<!-- CONFIRMAR -->` no FAQ,
   com texto genérico e verificável ("prazo informado no fechamento do pedido").
5. **O checkout continua fictício** nesta entrega — por isso o cupom deixa de dizer "PAGO"
   e passa a dizer "PEDIDO REGISTRADO / AGUARDANDO CONFIRMAÇÃO". Se ele já tiver gateway,
   é outra entrega.
6. **Os depoimentos continuam no ar**, rotulados como ilustrativos, até ele fornecer os reais.
7. **A chave do Gemini não será colada no arquivo.** As 4 funções de IA operam pelo fallback
   local, que é bom e agora responde em ~1s em vez de ~7s. Se ele quiser IA de verdade em
   produção, é proxy no servidor, em outra entrega.
8. **Nenhum ano fora dos 6 do `<select id="capsuleYear">`** aparece na linha do tempo.

# Delivery 360°: Do Zero ao Lucro — Página de Vendas

Landing page de conversão para o curso **Delivery 360°**, de Rodrigo Barros (Grupo 360 Food).

Site estático: **sem build, sem framework, sem dependência externa**. Basta subir os arquivos.

---

## Como rodar localmente

```bash
python3 -m http.server 8080
# abre http://localhost:8080
```

Os caminhos dos assets são absolutos (`/assets/...`), então precisa ser servido a partir da raiz —
abrir o `index.html` com dois cliques não vai carregar as fontes e o logo.

## Versão em arquivo único (para testar sem servidor)

```bash
python3 build-standalone.py     # gera delivery360-standalone.html
```

O script também roda o `sync-fotos.py` antes de gerar: ele lê as dimensões reais
de cada arquivo em `fotos/` e injeta `width`/`height` nas `<img>` do `index.html`.

**Sempre que trocar uma foto, rode o build de novo.** Sem isso a página volta a
"pular" enquanto as imagens carregam (Cumulative Layout Shift), o que incomoda o
visitante e conta contra no ranking do Google.

Esse arquivo tem fontes, logos, ícone e JavaScript embutidos: abre com dois cliques,
de qualquer pasta, sem servidor e sem internet. Serve para revisar, mandar por
WhatsApp/e-mail e testar no PC.

**Não edite o standalone** — ele é derivado. Altere o `index.html` e rode o script
de novo, senão suas mudanças somem na próxima geração. O que vai para o ar é o
`index.html` + `/assets`.

## Prévia rápida (link para o cliente)

```bash
python3 build-preview.py     # gera preview.html
```

Diferente do standalone, aqui **todas** as imagens entram em base64 — inclusive as
de `fotos/` — e o arquivo sai sem `<!doctype>`, `<html>`, `<head>` e `<body>`,
porque o hospedeiro envolve o conteúdo no próprio esqueleto.

Use para mandar link de revisão. O que vai para o ar continua sendo o
`index.html` + `/assets` + `fotos/`.

## Como publicar

| Host | O que fazer |
|---|---|
| **Hostinger / Apache** | Suba o conteúdo da pasta para `public_html/`. O `.htaccess` já vai junto (headers de segurança, cache e compressão). |
| **Netlify / Cloudflare Pages** | Arraste a pasta. O `_headers` já está configurado. |
| **Vercel** | `vercel deploy` na raiz. Sem configuração extra. |

---

## Arquivos

```
index.html                  ← página inteira (HTML + CSS crítico inline + JSON-LD)
assets/js/app.js            ← ~5KB: reveals, contadores, checklist, carrossel, tilt 3D
fotos/                      ← imagens do cliente (ver tabela abaixo)
build-standalone.py         ← gera a versão em arquivo único
build-preview.py            ← gera a versão para link de prévia
sync-fotos.py               ← lê as dimensões reais das fotos e evita CLS
compat-fallbacks.py         ← gera o rgba() equivalente a cada color-mix() (PC antigo)
assets/fonts/               ← Anton + Archivo Variable (woff2, subset latin, auto-hospedadas)
assets/img/                 ← logos em vetor, favicons e imagem de compartilhamento
robots.txt · sitemap.xml · site.webmanifest
.htaccess · _headers        ← headers de segurança e cache (escolha conforme o host)
```

**Por que o CSS está inline no `index.html`?** É uma página só. Inline = 1 request para a
página inteira e zero CSS bloqueando a renderização. Em site de uma página, CSS externo só
adiciona ida e volta de rede sem ganho de cache.

---

## Blocos da página (público: quem já vende no iFood)

1. **Promessa** — "Faturar no iFood não significa lucrar" + capa e CTA
2. **Diagnóstico** — 5 perguntas clicáveis com placar ao vivo
3. **Os 4 Vazamentos** — o mecanismo do método
4. **Demonstração** — `fotos/aula.png` em moldura, com slot pronto para vídeo
5. **O Método** — ciclo Configura → Precifica → Roda → Protege
6. **As 10 aulas** — 5 módulos em acordeão
7. **Provas reais** — números + 3 casos, cada um ligando o print da conversa ao faturamento antes e depois
8. **História e autoridade** — narrativa + foto do Rodrigo
9. **Bônus** — entregáveis e os 2 bônus
10. **Oferta + Garantia** — nova ancoragem, preço e selo de 7 dias
11. **FAQ** — 6 perguntas
12. **Chamada final**

---

## O que trocar antes de publicar

### 1. Link do checkout (feito)
Os cinco CTAs (topo, hero, oferta, chamada final e barra fixa do celular) apontam para
`https://pay.hotmart.com/S106632080Q?checkoutMode=10&bid=1787103675533`.
No HTML o `&` aparece como `&amp;`, que é a forma válida dentro de atributo; o navegador
entrega a URL original.

Cada botão mantém `data-cta="hero|oferta|final|dock|header"`, então dá para saber qual
posição converteu quando plugar o relatório.

### 2. Domínio (obrigatório para o SEO funcionar)
Troque `https://delivery360.com.br/` pela URL real em `index.html` (canonical, Open Graph e
JSON-LD), no `sitemap.xml` e no `robots.txt`:

```bash
sed -i 's|https://delivery360.com.br|https://SEUDOMINIO.com.br|g' index.html sitemap.xml robots.txt
```

### 3. Fotos da pasta `fotos/`

A página usa caminhos relativos, então a pasta `fotos/` precisa ficar ao lado do HTML:

| Arquivo | Onde aparece |
|---|---|
| `produto.png` | Capa no hero |
| `caneta.jpg` | Fundo esmaecido da dobra "Os 4 Vazamentos" |
| `aula.png` | Bloco de demonstração |
| `rodrigo.jpg` | Bloco de autoridade |
| `rodrigoevento.jpg` | Fundo esmaecido do método |
| `dep1.jpg` | Print da conversa do Lucas (caso 01) |
| `acai1.jpg` · `acai2.jpg` | Faturamento do Lucas, antes e depois |
| `dep3.jpg` | Print da conversa do Marcos (caso 02) |
| `madeiro1.jpg` · `madeiro2.jpg` | Faturamento do Marcos, antes e depois |
| `marmita1.jpg` · `marmita2.jpg` | Faturamento da Mermã Marmita, antes e depois |

Os arquivos `dep2`, `dep4` e `dep5` saíram da página. Os nomes acima precisam bater
**exatamente**, extensão inclusive: a página busca `.jpg`.

### 4. Grade do curso (já confirmada)

| Módulo | Aulas |
|---|---|
| 1 · Ponto de Partida | 1 |
| 2 · Configurações Estruturais e Logística | 5 |
| 3 · Construção e Inteligência de Cardápio | 1 |
| 4 · Gestão, Análise de Dados e Crescimento | 2 |
| 5 · Encerramento | 1 |

Os 10 títulos vieram do Rodrigo e estão verbatim em `.grade__list`.

### 5. Medição (já instalada)

| Ferramenta | Identificador | Onde está |
|---|---|---|
| Google Tag Manager | `GTM-KRFC8HWM` | `<head>`, logo abaixo da CSP + `noscript` na abertura do `<body>` |
| Meta Pixel | `1599446431713463` | `<head>`, depois do GTM + `noscript` na abertura do `<body>` |

**Não suba o Meta Pixel também por dentro do GTM.** Ele já está fixo no HTML; publicar
de novo pelo contêiner faz cada PageView contar duas vezes e o custo por conversão sai
pela metade do real, o que leva a decisão errada de verba.

A CSP do `<head>` foi aberta para `www.googletagmanager.com`, `connect.facebook.net`,
`www.facebook.com`, `www.google-analytics.com` e `analytics.google.com`, e ganhou
`'unsafe-inline'` em `script-src`, que o GTM exige para injetar as próprias tags.
Se o modo Preview do GTM não abrir, acrescente `'unsafe-eval'` em `script-src`:
só a depuração precisa dele.

O bloco fica entre os marcadores `<!-- analytics:inicio -->` e `<!-- analytics:fim -->`.
Os builds de prévia e de arquivo único apagam esse trecho de propósito: revisão interna
não pode entrar como visita real no relatório de campanha.

**Pendência de LGPD.** O Pixel e o GTM disparam assim que a página abre, sem pedir
autorização. A ANPD entende que cookie de marketing depende de consentimento. A política
de privacidade já declara isso abertamente, mas falta um banner de consentimento que só
libere as tags depois do aceite.

### 6. Dados das páginas legais
`termos-de-uso.html` e `politica-de-privacidade.html` têm campos marcados como
`[informar ...]` — CNPJ, endereço e cidade/UF. Preencha e apague as caixas laranja.
A plataforma de checkout já está como **Hotmart**, e o cancelamento nos 7 dias aponta
para "Minhas compras" da Hotmart em todos os lugares (FAQ, oferta, termos e política).

## Decisões técnicas

**Cores** — direto do guia da marca: `#c62828`, `#f6f3ec`, `#1c1c1c` e `#e86a1c`.
O vermelho sobre preto dá contraste 3,06:1, o que reprova em texto pequeno pelo WCAG AA. Por isso
o vermelho aparece só em display grande, formas e fundos; o laranja (5,3:1) é o acento de texto
pequeno e o corpo é sempre creme (15,2:1). A marca fica fiel e a página legível no celular sob sol.

**Logos** — extraídos em vetor do PDF da marca, não rasterizados. `logo-horizontal.svg` e
`logo-vertical.svg` usam `currentColor` no lettering (adaptam ao fundo por CSS); as versões
`-cream` e `-ink` têm cor fixa para uso em `<img>`.

**Fontes** — Anton (display) e Archivo Variable (texto), auto-hospedadas em woff2 subset latin
(53KB no total). Sem Google Fonts CDN: economiza uma conexão externa e evita o repasse de IP do
visitante para terceiro, que já rendeu multa por LGPD/GDPR em outros países.

**Performance** — 1 request de HTML (CSS inline), 1 de JS, 2 de fonte. Sem terceiros, sem
jQuery, sem framework. `width`/`height` em todas as imagens (CLS zero) e toda animação
atrás de `prefers-reduced-motion`.

---

## Computador antigo

O dono de restaurante muitas vezes abre a página no PC do balcão, não num aparelho novo.
Quem está no Windows 7/8.1 trava no **Chrome 109** — e é aí que o CSS moderno começa a cair.

| Recurso | Exige | O que fiz |
|---|---|---|
| `color-mix()` | Chrome 111 | `compat-fallbacks.py` gera o `rgba()` equivalente antes de cada uso |
| `translate` / `rotate` (propriedades soltas) | Chrome 104 | bloco `@supports not (translate: 0)` com `transform`, fora de `@layer` |
| `:has()` | Chrome 105 | o JS marca `data-on` no item; regra espelho em CSS |
| `<dialog>` | Safari 15.4 | sem ele, o print abre em outra aba |
| `@layer` | Chrome 99 | **mantido** — ver abaixo |

**Por que `@layer` fica.** Se o navegador não entender, ele descarta o bloco inteiro e a
página fica sem estilo nenhum — a pior falha possível. Mesmo assim eu mantive, por dois
motivos: o teto real de PC velho (Chrome 109) já suporta, e a camada `motion` depende da
ordem de camadas para o `*{animation-duration:.001ms}` vencer regras de especificidade
maior. Sem camadas, o `prefers-reduced-motion` da página inteira deixaria de funcionar.
Trocar uma falha improvável por uma quebra certa de acessibilidade seria um mau negócio.

**Modo leve.** O `app.js` marca `data-lite` no elemento raiz quando o aparelho tem 2 núcleos
ou menos, 2GB ou menos, ou quando 1 segundo de medição de quadros fica abaixo de 30fps
(medido só com a aba visível, 900ms depois do load, e guardado no `sessionStorage`).
Nesse modo saem `backdrop-filter`, `mix-blend-mode`, máscara e o giro dos raios do hero.
O letreiro continua andando de propósito: é animação de `transform`, que a GPU resolve
recompondo a camada sem repintar — dos efeitos mais baratos da página.

**Como testar sem ter um PC velho à mão.** `/tmp/velho.py` (no histórico da sessão) poda do
CSS tudo que o Chrome 109 não entende e mede a página resultante. O que ele verifica:
sem vazamento horizontal, sem erro de JS, `.card` com padding e borda corretos, raios e
setas posicionados via `transform`, letreiro andando e checklist acendendo sem `:has()`.

**Acessibilidade** — HTML semântico, um `<h1>` só, skip link, foco visível, checklist com
`<input>` real, FAQ em `<details>` nativo (funciona sem JS e é indexável), `aria-live` no
contador do checklist.

**SEO** — canonical, Open Graph e Twitter Card com imagem própria, JSON-LD de
`Course` + `Offer` + `FAQPage` + `Person` + `Organization`, sitemap e robots.

**CTA** — verde clássico de compra (`#12873e` → `#0a5f2b`) com texto branco: 4,60:1 no topo do
gradiente e 7,82:1 na base, passa AA no botão inteiro. O verde é exclusivo dos CTAs; se aparecesse
em outro elemento, deixaria de significar ação.

**Sobre as provas** — os depoimentos escritos foram substituídos por um carrossel de prints reais.
Nada é marcado como `Review`/`AggregateRating` no JSON-LD: avaliação estruturada sem verificação
viola a política de rich results do Google e pode gerar penalização manual no domínio.

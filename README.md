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

Esse arquivo tem fontes, logos, ícone e JavaScript embutidos: abre com dois cliques,
de qualquer pasta, sem servidor e sem internet. Serve para revisar, mandar por
WhatsApp/e-mail e testar no PC.

**Não edite o standalone** — ele é derivado. Altere o `index.html` e rode o script
de novo, senão suas mudanças somem na próxima geração. O que vai para o ar é o
`index.html` + `/assets`.

## Como publicar

| Host | O que fazer |
|---|---|
| **Hostinger / Apache** | Suba o conteúdo da pasta para `public_html/`. O `.htaccess` já vai junto (headers de segurança, cache e compressão). |
| **Netlify / Cloudflare Pages** | Arraste a pasta. O `_headers` já está configurado. |
| **Vercel** | `vercel deploy` na raiz. Sem configuração extra. |

---

## Estrutura

```
index.html                  ← página inteira (HTML + CSS crítico inline + JSON-LD)
assets/js/app.js            ← ~5KB: reveals, contadores, tilt 3D, checklist, A/B de headline
assets/fonts/               ← Anton + Archivo Variable (woff2, subset latin, auto-hospedadas)
assets/img/                 ← logos em vetor, favicons e imagem de compartilhamento
robots.txt · sitemap.xml · site.webmanifest
.htaccess · _headers        ← headers de segurança e cache (escolha conforme o host)
```

**Por que o CSS está inline no `index.html`?** É uma página só. Inline = 1 request para a
página inteira e zero CSS bloqueando a renderização. Em site de uma página, CSS externo só
adiciona ida e volta de rede sem ganho de cache.

---

## As 9 dobras

1. **Hero** — headline principal, capa 3D do produto e CTA
2. **O Diagnóstico** — duas situações, uma causa só
3. **O Verdadeiro Vilão** — quebra de objeção + checklist de sintomas (interativo)
4. **A Culpa Não é Sua** — causa raiz e os 4 vazamentos de lucro
5. **O Método Delivery 360°** — ciclo Configura → Precifica → Roda → Protege
6. **A Prova** — números, 3 depoimentos e "Quem sou eu"
7. **O Que Você Leva Hoje** — 10 aulas, 5 módulos, 2 bônus e a garantia
8. **Isso é Para Você? + A Oferta** — ✅/❌, ancoragem de R$1.500 e a caixa de preço
9. **Fechamento** — custo da inação, FAQ e CTA final

---

## O que trocar antes de publicar

### 1. Link do checkout (obrigatório)
Todos os CTAs apontam para `#checkout`. Troque pela URL da plataforma (Hotmart, Kiwify, Eduzz…):

```bash
sed -i 's|href="#checkout"|href="https://pay.suaplataforma.com/xxxxx"|g' index.html
```

Os botões já têm `data-cta="hero|oferta|final|dock|header"`, então dá pra saber qual posição
converteu quando você plugar analytics.

### 2. Domínio (obrigatório para o SEO funcionar)
Troque `https://delivery360.com.br/` pela URL real em `index.html` (canonical, Open Graph e
JSON-LD), no `sitemap.xml` e no `robots.txt`:

```bash
sed -i 's|https://delivery360.com.br|https://SEUDOMINIO.com.br|g' index.html sitemap.xml robots.txt
```

### 3. Foto do Rodrigo
Na dobra 6 existe um slot marcado. Substitua o `<figcaption class="slot">` por:

```html
<img src="/assets/img/rodrigo.webp"
     alt="Rodrigo Barros na cozinha de um dos restaurantes do Grupo 360 Food"
     width="800" height="1000" loading="lazy" decoding="async">
```

Recomendado: WebP, 800×1000, abaixo de 120KB.

### 4. Capa do produto
A capa no hero é composta em CSS/SVG — ela é vetorial, nítida em qualquer tela e não pesa nada.
Se quiser usar a arte final em imagem, coloque o arquivo em
`assets/img/capa-delivery360.png` e troque o bloco `.cover__in` por um `<img>` com
`width`/`height` declarados (para não gerar CLS).

### 5. Pixel / GA4 (opcional)
Adicione antes de `</body>`. Se usar script de terceiro, atualize o `Content-Security-Policy`
no `<head>` incluindo o domínio em `script-src` e `connect-src` — hoje a política é `'self'`
e vai bloquear qualquer script externo.

### 6. E-mail de suporte
A FAQ 4 promete "basta mandar um e-mail". Não existe e-mail na página — inclua-o na resposta
da FAQ 4 e no rodapé antes de publicar, ou a promessa de garantia fica sem endereço.

---

## Teste A/B de headline (sem ferramenta)

As duas variações da copy já estão no HTML, em `data-`atributos do `<h1>`:

| URL | Headline exibida |
|---|---|
| `/` | Principal — "Ninguém te mostrou como isso funciona de verdade" |
| `/?h=a` | Variação A — Escala e autoridade ("12 restaurantes. 1 método. Nenhuma teoria.") |
| `/?h=b` | Variação B — Antes e depois (repasse de quarta-feira) |

Basta rodar tráfego para as três URLs e comparar conversão.

---

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
jQuery, sem framework. `content-visibility` nas dobras longas, `width`/`height` em todas as
imagens (CLS zero) e toda animação atrás de `prefers-reduced-motion`.

**Acessibilidade** — HTML semântico, um `<h1>` só, skip link, foco visível, checklist com
`<input>` real, FAQ em `<details>` nativo (funciona sem JS e é indexável), `aria-live` no
contador do checklist.

**SEO** — canonical, Open Graph e Twitter Card com imagem própria, JSON-LD de
`Course` + `Offer` + `FAQPage` + `Person` + `Organization`, sitemap e robots.

**Sobre os depoimentos:** eles são exibidos como depoimento visual comum e **não** estão marcados
como `Review`/`AggregateRating` no JSON-LD. Marcar avaliação sem verificação viola a política de
rich results do Google e pode gerar penalização manual no domínio.

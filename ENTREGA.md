# Delivery 360°: Do Zero ao Lucro — Documentação da Entrega

Página de vendas do curso **Delivery 360°**, de Rodrigo Barros (Grupo 360 Food).

| | |
|---|---|
| **Repositório** | `richardbarbosa-gif/petteste` |
| **Branch** | `claude/delivery-360-sales-page-fzhdum` |
| **Tipo** | Site estático — sem build, sem framework, sem dependência externa |
| **Arquivo de produção** | `index.html` + `/assets` |
| **Arquivo para teste local** | `delivery360-standalone.html` (tudo embutido, abre com dois cliques) |

---

## 1. Insumos recebidos e o que foi extraído deles

### `GUIDE_RODRIGO_BARROS.pdf` — manual da marca

Paleta oficial, aplicada sem desvio:

| Cor | HEX | Papel na página |
|---|---|---|
| Vermelho (primária) | `#c62828` | Marca, blocos, display grande, formas |
| Off-white (primária) | `#f6f3ec` | Texto sobre fundo escuro, seções claras |
| Preto marca (primária) | `#1c1c1c` | Fundo base — a página é dark-first, como a capa |
| Laranja (secundária) | `#e86a1c` | Acento de conversão: CTA, números, ênfase em texto |

O guia também declara a tipografia da marca: **NewBlack** (Zetafonts, licença paga —
não pode ser embutida em web).

### `LOGO_RODRIGO.pdf` — 8 variações do logo

Extraídas em **vetor puro**, não rasterizadas, direto do PDF, com as cores exatas
do guia. Geradas 6 versões:

| Arquivo | Uso |
|---|---|
| `logo-horizontal.svg` | Lettering em `currentColor` — adapta ao fundo por CSS |
| `logo-horizontal-cream.svg` | Cor fixa creme — para uso em `<img>` sobre fundo escuro |
| `logo-horizontal-ink.svg` | Cor fixa preta — para uso sobre fundo claro |
| `logo-vertical.svg` / `-cream.svg` | Variação vertical (uso secundário) |
| `logo-symbol.svg` | Só o monograma "R" — 600 bytes, usado como favicon e marca d'água |

### Capa do produto

O PNG da capa não chegou entre os arquivos enviados. A capa no hero foi **recomposta
em CSS/SVG**: fundo radial, raios, logo, "DELIVERY 360°" com gradiente metálico, selo
"DO ZERO AO LUCRO" e "5 MÓDULOS · 10 AULAS". Vetorial, nítida em qualquer tela,
com parallax e reflexo que seguem o ponteiro. A ilustração 3D (celular + caixas) é
original, geométrica — o ambiente de desenvolvimento bloqueia bancos de imagem.

---

## 2. Decisões sobre a copy

### Versão escolhida: **Copy 2** (Versão Refinada e Consolidada)

Motivos objetivos:

- A Copy 1 tem dois `[PENDENTE]` que travariam a publicação. A Copy 2 resolve os dois:
  **12x de R$ 9,68** e **acesso vitalício**.
- Nome final do ebook do Bônus #1: **"Gestão de Equipe Descomplicada"** (a Copy 1
  assume nome provisório).
- FAQ completa com 7 perguntas e checklist de sintomas já formatado.

**Nenhuma palavra da copy foi alterada.** Os títulos de seção usados na página
("O diagnóstico", "A causa raiz", "O custo da inação" etc.) são os próprios rótulos
de bloco que já estavam na copy.

### Auditoria automática de cobertura

Foi escrito um script que extrai todo o texto renderizado da página e compara contra
**82 trechos** da copy, normalizando acento, aspas tipográficas e pontuação.

Na primeira rodada faltavam 2 trechos, ambos incluídos depois:

1. `"No nível do miojo (passo a passo ultra-simples):"` — dobra do método
2. `"Depoimentos reais de quem saiu do escuro"` — rótulo antes dos depoimentos

**Resultado final: 82/82 presentes.**

### Ponto levantado e mantido a pedido do cliente

A Copy 1 diz explicitamente *"Ainda não tenho depoimento de aluno pra te mostrar aqui.
Prefiro ser direto com você do que inventar um"*. A Copy 2 traz 3 depoimentos com nome,
cidade e valores. Foi sinalizado o risco (CDC art. 37 — publicidade enganosa, se os
alunos não existirem) e a decisão de usá-los foi do cliente. Os depoimentos estão na
página exatamente como escritos.

**Mitigação técnica aplicada:** eles **não** foram marcados como `Review` ou
`AggregateRating` no JSON-LD. Dado de avaliação estruturado sem verificação viola a
política de rich results do Google e pode gerar penalização manual no domínio inteiro.
Como depoimento visual comum eles funcionam igual e não expõem o site.

---

## 3. As 9 dobras

| # | Dobra | Conteúdo | Tratamento |
|---|---|---|---|
| 1 | **Hero** | Headline, subheadline, CTA | Fundo radial vermelho, raios em rotação lenta, grão, capa 3D com parallax e reflexo, selos de garantia |
| 2 | **O Diagnóstico** | "Duas situações, uma causa só" — já vende / ainda não abriu | Dois cards com tilt 3D no ponteiro, barra de acento lateral, número de fundo em marca d'água |
| 3 | **O Verdadeiro Vilão** | Quebra de objeção + checklist de 6 sintomas | Aspas em display, transição preto→vermelho profundo, **checklist clicável** com placar em selo |
| 4 | **A Culpa Não é Sua** | Causa raiz + 4 vazamentos de lucro | Seção clara (`#f6f3ec`) quebrando o ritmo escuro; vazamentos numerados em cards brancos |
| 5 | **O Método Delivery 360°** | Ciclo Configura → Precifica → Roda → Protege | Diagrama do fluxo, 4 cards com extrusão e barra de acento, mockup do painel do iFood em SVG |
| 6 | **A Prova** | Números, 3 depoimentos, "Quem sou eu" | Contadores animados, cards claros com aspa gráfica, moldura da foto com monograma |
| 7 | **O Que Você Leva Hoje** | 10 aulas, 5 módulos, 2 bônus, garantia | Grid 2×2, bônus destacados em laranja, selo de garantia em SVG |
| 8 | **Isso é Para Você? + A Oferta** | ❌/✅, ancoragem de R$1.500, preço, CTA | Colunas opostas, risco animado sobre o R$1.500, caixa de preço clara sobre fundo escuro, botão 3D |
| 9 | **Fechamento** | Custo da inação, FAQ, CTA final, rodapé | Bloco vermelho-sangue, FAQ em `<details>` nativo, rodapé com avisos legais |

**Fora das dobras:** barra de CTA fixa no mobile que aparece depois do hero, barra de
progresso de leitura no topo e header com logo + CTA.

---

## 4. Decisões técnicas

### Stack: HTML + CSS + JavaScript, sem framework

Uma página de vendas precisa carregar rápido no 4G de quem está na cozinha, não de
um framework. Sem React, sem jQuery, sem build. O cliente sobe a pasta em qualquer
host arrastando os arquivos.

### CSS inline no `index.html`

É uma página só. Inline = **1 request para a página inteira** e **zero CSS bloqueando
a renderização**. CSS externo em site de uma página só adiciona ida e volta de rede
sem ganho de cache.

Organizado em `@layer reset, tokens, base, layout, components, sections, motion, utils`
— cascata previsível, **nenhum `!important` no arquivo**.

### Recursos modernos usados

- CSS Nesting nativo, `@layer`, `color-mix()`, `container queries`
- `clamp()` em toda a tipografia e espaçamento — fluido, sem breakpoint quebrado
- `animation-timeline: scroll()` na barra de progresso, com fallback
- 3D real: `transform-style: preserve-3d` + `perspective` + `rotate3d`
- `content-visibility: auto` nas dobras longas
- `<details name="faq">` — acordeão exclusivo nativo, sem JavaScript
- JavaScript em módulo ES: `IntersectionObserver`, `matchMedia`, `requestAnimationFrame`

### Tipografia

**NewBlack** é licença paga e não pode ser embutida. Par equivalente escolhido:

- **Anton** — display pesado (headlines, números, "DELIVERY 360°"). É o que mais se
  aproxima do peso condensado da capa do produto.
- **Archivo Variable** — títulos de seção e corpo. Grotesca geométrica com
  personalidade, parenta bem com o wordmark do logo, e evita o visual genérico de
  Inter/Poppins.

Auto-hospedadas em `woff2` subset latin, **53KB no total**. Zero request para o
Google Fonts: economiza uma conexão externa e evita repassar o IP do visitante para
terceiro — o que já rendeu multa por GDPR/LGPD em outros países.

### Contraste: a regra que define onde cada cor entra

Medido, não estimado:

| Combinação | Contraste | Veredito |
|---|---|---|
| `#c62828` sobre `#1c1c1c` | **3,06:1** | Reprova AA em texto pequeno |
| `#e86a1c` sobre `#1c1c1c` | **5,3:1** | Passa AA |
| `#f6f3ec` sobre `#1c1c1c` | **15,2:1** | Passa AAA |

Por isso: **vermelho** só em display grande, fundos e formas; **laranja** é o acento
de texto pequeno e CTA; **creme** é sempre o corpo. A marca fica fiel e a página
legível no celular sob sol — que é onde o público lê.

---

## 5. Performance (medida no Chromium, não estimada)

| Métrica | Valor |
|---|---|
| Requests | **6** (HTML, JS, logo, favicon, 2 fontes) |
| Peso real transferido | **~82 KB** com compressão |
| First Contentful Paint | **372 ms** |
| DOMContentLoaded | **149 ms** |
| Load | **152 ms** |
| CLS | **0** — toda imagem com `width`/`height` |
| Overflow horizontal | Nenhum em 390 / 1280 / 1440px |
| Erros de console | Nenhum |
| Requests de terceiros | **Zero** |

Quebra do peso:

```
HTML + CSS inline    91,5 KB → 23,0 KB (gzip)
JavaScript            7,4 KB →  2,6 KB (gzip)
Logo SVG              9,7 KB →  3,6 KB (gzip)
Fonte Anton          18,2 KB (woff2, já comprimida)
Fonte Archivo        34,1 KB (woff2, já comprimida)
Favicon               0,7 KB →  0,4 KB
────────────────────────────────────────────
TOTAL                          ~82 KB
```

---

## 6. SEO

- `lang="pt-BR"`, um único `<h1>`, hierarquia de heading limpa (1 h1 + 10 h2)
- `title` e `meta description` escritos para CTR, não para keyword
- Canonical, Open Graph e Twitter Card
- **Imagem de compartilhamento gerada** (`og-delivery360.png`, 1200×630) usando as
  fontes e cores reais da marca
- **JSON-LD** com `Course`, `Offer` (incluindo `MerchantReturnPolicy` de 7 dias),
  `FAQPage`, `Person`, `Organization` e `WebSite`
- FAQ em `<details>` nativo — indexável e funcional sem JavaScript
- `sitemap.xml`, `robots.txt`, `site.webmanifest` e favicons
- Alt descritivo em todas as imagens

---

## 7. Segurança

- **CSP restritiva** em meta: `script-src 'self'`, `object-src 'none'`,
  `base-uri 'none'`, `form-action 'none'`, `frame-src 'none'`
- Headers de segurança prontos para os dois cenários de host:
  `.htaccess` (Hostinger/Apache) e `_headers` (Netlify/Cloudflare Pages) — com
  `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`,
  `Permissions-Policy`, `Strict-Transport-Security` e cache imutável para assets
- Zero handler inline, zero `innerHTML` com dado externo
- A página não coleta nenhum dado — o checkout é externo, então não há superfície
  de vazamento

---

## 8. Acessibilidade

- HTML semântico com `<section aria-labelledby>` em todas as dobras
- Skip link para o conteúdo
- Foco visível em laranja com `outline-offset`
- Checklist com `<input type="checkbox">` real e `<label>` associado
- `aria-live="polite"` no placar do checklist
- Toda animação atrás de `prefers-reduced-motion: reduce`
- Tilt 3D desativado em tela de toque (`(hover: hover) and (pointer: fine)`)
- CTA da barra fixa sai da ordem de tabulação enquanto está escondida

---

## 9. Funcionalidades interativas

| Recurso | Como funciona |
|---|---|
| **Teste A/B de headline** | As duas variações da copy estão em `data-` no `<h1>`. `/?h=a` = escala e autoridade, `/?h=b` = antes e depois, `/` = principal. Sem ferramenta externa. |
| **Checklist de sintomas** | Micro-compromisso: o visitante marca o que reconhece e um selo mostra o placar ao vivo. |
| **Contadores** | 12 / 150+ / 330 / 10 animam ao entrar na tela. |
| **Tilt 3D** | Cards seguem o ponteiro, no máximo 7° — acima disso vira enjoo, não sofisticação. |
| **Capa com parallax** | Rotação e reflexo acompanham o ponteiro pela página inteira. |
| **CTA fixa no mobile** | Aparece depois do hero, com preço ao lado do botão. |
| **Rastreio de CTA** | Todos os botões têm `data-cta="hero\|header\|oferta\|final\|dock"` para saber qual posição converteu. |

---

## 10. Problemas encontrados e corrigidos durante o processo

Registrados porque valem como aprendizado do projeto:

1. **SVG do logo inválido** — a extração do PDF deixava atributos com prefixo
   `inkscape:` sem o namespace declarado. O XML quebrava e o logo não renderizava em
   `<img>`. Corrigido removendo os atributos órfãos; a validação de XML virou parte
   da geração.

2. **`</style>` dentro de comentário CSS** — no gerador do arquivo único, escrevi a
   tag de fechamento de `style` dentro de um comentário. O parser HTML encerra o bloco
   ali mesmo, sem se importar que esteja comentado: as fontes em base64 vazavam como
   texto na página e o `scrollWidth` ia a 531.000px. Corrigido, com verificação
   automática no gerador para não repetir.

3. **Contadores em zero** — os números da prova social começavam em `0` no HTML e só
   ganhavam valor quando o JavaScript animava. Se o JS falhasse, o visitante leria
   *"0 restaurantes próprios"* exatamente na dobra que existe para provar autoridade.
   Invertido: o número correto vem no HTML e o JS só zera no instante de animar.

4. **256px entre seções** — a borda de dobra estava em 128px em cima e embaixo, o que
   quebra o fluxo de leitura de uma página de vendas. Reduzido para 104px no desktop
   e 52px no mobile. A página caiu de ~13.000px para 11.480px sem cortar uma linha.

5. **Escala de espaço inconsistente** — a distância de título para texto variava entre
   24px e 32px conforme a seção. Unificada em tokens (`--sp-7` borda de dobra,
   `--sp-6` bloco interno, `--sp-head` cabeçalho) e numa classe `.sec-head`.

6. **Aspas invadindo o título** — as aspas em display da dobra 3 subiam e colidiam com
   o h2 acima. Realinhadas à primeira linha de cada citação.

7. **Card do diagnóstico meio vazio** — os dois cards esticavam para a mesma altura, e
   como um tem três parágrafos e o outro tem um, sobrava metade de caixa vazia. Agora
   cada card abraça o próprio conteúdo.

8. **Acentos maiúsculos encostando** — a entrelinha de `.h2` e do bloco de inação
   estava apertada demais para caixa alta acentuada (Ã, Ê, Õ). Corrigida.

---

## 11. Estrutura de arquivos

```
index.html                  Página inteira: HTML + CSS inline + JSON-LD  (1.422 linhas)
assets/js/app.js            Interações, sem dependência                  (184 linhas)
assets/fonts/               Anton + Archivo Variable (woff2, subset latin)
assets/img/                 Logos em vetor, favicons, imagem de compartilhamento
robots.txt                  Indexação + apontador do sitemap
sitemap.xml                 Mapa do site
site.webmanifest            Ícones e cores para instalação no celular
.htaccess                   Headers e cache — Hostinger / Apache
_headers                    Headers e cache — Netlify / Cloudflare Pages
build-standalone.py         Gera a versão em arquivo único               (139 linhas)
delivery360-standalone.html Versão para testar sem servidor              (gerada)
README.md                   Como rodar, publicar e o que trocar
ENTREGA.md                  Este documento
```

### Versão em arquivo único

```bash
python3 build-standalone.py
```

Embute fontes, logos, ícone e JavaScript dentro do próprio HTML. Abre com dois cliques,
de qualquer pasta, sem servidor e sem internet.

As fontes em base64 ficam num `<style>` separado no fim do `<head>`, marcado com
comentário — assim o CSS legível não fica soterrado por 70KB de base64 se o arquivo
for aberto num editor de texto.

**Não edite o standalone**: ele é derivado. Altere o `index.html` e rode o script de
novo, senão as mudanças somem na próxima geração.

---

## 12. Verificação executada

Tudo abaixo foi rodado em Chromium real, não estimado:

- Renderização em **1440px, 1280px e 390px**, sem overflow horizontal em nenhum
- Zero erro de console e zero request com falha
- **Paridade entre o arquivo único e a versão servida**: mesma altura de página
  (11.480px), mesma métrica de H1, 11 seções, 7 FAQs, 5 CTAs, Anton carregada nos dois
- Auditoria de copy: 82/82 trechos presentes
- Auditoria de espaçamento: respiro entre irmãos consecutivos dentro da faixa esperada
- Interações testadas no arquivo entregue: checklist marca, FAQ abre, contadores
  chegam ao número certo, CTA fixa aparece no mobile, A/B responde em `?h=a` e `?h=b`
- Acessibilidade básica: 1 `<h1>`, nenhuma imagem sem dimensão, nenhum link sem texto
  ou `aria-label`

---

## 13. Pendências para publicar

| # | Pendência | Impacto |
|---|---|---|
| 1 | **Link do checkout** | Bloqueia a venda. Os 5 CTAs apontam para `#checkout`. O README tem o comando pronto para trocar. |
| 2 | **Domínio final** | Bloqueia o SEO. Canonical, Open Graph, JSON-LD e sitemap estão com `delivery360.com.br` como marcador. |
| 3 | **E-mail de suporte** | A FAQ 4 promete *"basta mandar um e-mail"* e não existe e-mail em lugar nenhum da página. Promessa de garantia sem endereço é a que mais gera reclamação. |
| 4 | **Foto do Rodrigo** | Slot pronto na dobra 6, troca de uma tag. Uma foto na cozinha vale mais que estúdio. |
| 5 | **Capa oficial em PNG** | A atual é recomposição vetorial fiel ao layout. |
| 6 | **Pixel / GA4** | Se for usar, o domínio do script precisa entrar no `Content-Security-Policy` — hoje a política é `'self'` e bloqueia script externo. |
| 7 | **Confirmar os depoimentos** | Ver seção 2. |

---

## 14. Histórico de commits

```
6b01d2c  refine: auditoria de copy nas 9 dobras e acabamento de design
835d352  refine: escala vertical única e versão em arquivo único
e4cb569  feat: página de vendas Delivery 360° — 9 dobras, estática e sem dependências
```

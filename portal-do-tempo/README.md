# Portal do Tempo

Site institucional/e-commerce de objetos originais dos anos 90.
Arquivo único, sem build, sem dependência: `index.html`.

## Como publicar

Suba `index.html` na raiz do domínio. Nada mais é necessário —
não há bundler, não há node_modules, não há chamada de API.

## Trocar as ilustrações por fotos reais

Toda a arte é SVG inline (nenhuma imagem externa é carregada).
Para usar foto de produto, substitua dentro de cada `.prod__cover`:

```html
<svg class="prod__art" viewBox="0 0 64 64" aria-hidden="true"><use href="#i-tv"></use></svg>
```

por:

```html
<img class="prod__art" src="fotos/tv-tubo-1994.webp"
     alt="Televisão de tubo de 20 polegadas, 1994, revisada"
     width="600" height="450" loading="lazy" decoding="async">
```

Regras para não perder performance nem SEO:
- formato `.webp` (ou `.avif`), largura máxima de 900px;
- `loading="lazy"` em tudo abaixo da primeira dobra;
- `width`/`height` sempre preenchidos, para não causar deslocamento de layout (CLS);
- `alt` descrevendo a peça de verdade — é o que o Google lê e o leitor de tela fala.

## A Mixtape do Portal (playlist do YouTube)

Uma linha só. Procure no `index.html`:

```html
<div class="player" id="player" ... data-playlist="COLE_O_ID_DA_SUA_PLAYLIST"
```

Troque `COLE_O_ID_DA_SUA_PLAYLIST` pelo ID da sua playlist — é o trecho depois de
`list=` na URL do YouTube, começa com `PL`. Exemplo:

`https://www.youtube.com/playlist?list=PLabc123XYZ` → `data-playlist="PLabc123XYZ"`

Três coisas já resolvidas no código:

- **O player só carrega no clique** (padrão *facade*). Sem isso, o iframe do YouTube
  puxaria cerca de 1MB de JavaScript de terceiro em todo mundo que abre a página,
  inclusive quem nunca vai ouvir.
- **Usa `youtube-nocookie.com`**, que não grava cookie de rastreio antes do play.
- **O ID passa por validação de formato** antes de entrar na URL do iframe.

Atualize a lista de faixas na seção `.faixas` para bater com a playlist de verdade —
e se você não for atualizar a fita toda semana, apague a frase
"Atualizada toda quinta". Promessa de recorrência não cumprida custa mais confiança
do que promessa nenhuma.

## O som da TV

O botão "Ligar a TV (com som)" sintetiza a vinheta no próprio navegador com a
Web Audio API: clique do botão, o *thump* grave do tubo desmagnetizando, o apito
agudo do flyback e o chiado da fita. **Nenhum arquivo de áudio é carregado e não há
direito autoral envolvido** — o som é gerado por osciladores e ruído.

Só dispara no clique, de propósito: autoplay com som é bloqueado em todos os
navegadores modernos, e som inesperado é o que mais faz fechar aba.

## Antes de ir para produção

- [ ] Trocar `https://www.portaldotempo.com.br/` no `canonical` e no Open Graph pelo domínio real.
- [ ] Adicionar uma imagem de compartilhamento: `<meta property="og:image" content="...">` (1200x630).
- [ ] Trocar o número de WhatsApp `5511900000000` e o e-mail nos links.
- [ ] Preencher CNPJ e endereço reais no rodapé e no JSON-LD.
- [ ] Plugar o formulário da newsletter num backend com HTTPS e validação **também no servidor**
      (a validação de e-mail no navegador é conveniência, nunca segurança).
- [ ] Plugar os botões "Quero essa" no carrinho/checkout real.
- [ ] Criar `robots.txt` e `sitemap.xml` na raiz.

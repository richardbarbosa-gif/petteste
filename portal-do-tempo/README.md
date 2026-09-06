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

## Antes de ir para produção

- [ ] Trocar `https://www.portaldotempo.com.br/` no `canonical` e no Open Graph pelo domínio real.
- [ ] Adicionar uma imagem de compartilhamento: `<meta property="og:image" content="...">` (1200x630).
- [ ] Trocar o número de WhatsApp `5511900000000` e o e-mail nos links.
- [ ] Preencher CNPJ e endereço reais no rodapé e no JSON-LD.
- [ ] Plugar o formulário da newsletter num backend com HTTPS e validação **também no servidor**
      (a validação de e-mail no navegador é conveniência, nunca segurança).
- [ ] Plugar os botões "Quero essa" no carrinho/checkout real.
- [ ] Criar `robots.txt` e `sitemap.xml` na raiz.

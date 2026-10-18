# UX Mobile — a página é usada com um polegar

Para o público do Richard (serviço local, tráfego de anúncio e Instagram), a maioria absoluta chega
pelo celular. "Responsivo" resolve o layout; isto resolve o **uso**. São coisas diferentes: uma
página pode ser perfeitamente responsiva e insuportável de operar com uma mão.

---

## Zona do polegar

Com o celular numa mão, o polegar alcança confortavelmente a **metade inferior** da tela. O topo
exige reposicionar o aparelho — um micro-esforço que a pessoa não faz por qualquer coisa.

- **Fácil:** terço inferior e centro-baixo. É onde ação repetida e CTA de rolagem longa devem morar.
- **Médio:** meio da tela.
- **Difícil:** cantos superiores. Cabem logo e menu (que a pessoa procura conscientemente), não a
  ação principal.

Consequências:
- CTA fixo no rodapé (não no topo) em página longa.
- Botão de fechar de modal: se estiver no canto superior direito, adicione também toque fora do
  modal e gesto de deslizar. Modal que não fecha com facilidade é a forma mais rápida de perder
  alguém.
- Ação destrutiva não fica onde o polegar descansa.

## CTA fixo (barra inferior)

Em página longa, resolve o "onde eu clico agora" sem obrigar a rolar de volta.

Regras pra não virar praga:
- **Uma** ação, altura discreta (~56–64px), não cobre conteúdo essencial.
- Aparece **depois** do hero (antes é redundante — o CTA do hero já está na tela).
- Respeita a área segura do aparelho (`padding-bottom: env(safe-area-inset-bottom)`), senão fica sob
  a barra de gestos do iPhone.
- Some quando o formulário está em foco (senão briga com o teclado e cobre campo).
- Nunca duas barras fixas somadas (topo + rodapé) comendo a tela.

## Alvos de toque

- Mínimo **44×44px** de área tocável — mesmo que o visual seja menor, aumente a área com padding.
- **8px de espaço** entre alvos adjacentes. Links de rodapé colados são a causa nº 1 de toque errado.
- Ícone sozinho como alvo precisa de rótulo textual ou `aria-label`. Ícone ambíguo faz a pessoa
  hesitar, e hesitação no mobile vira saída.

## Teclado

O teclado ocupa metade da tela. Isso muda a página quando um campo recebe foco:

- Campo em foco não pode ficar escondido atrás do teclado. Teste rolando até o último campo.
- Botão de envio deve ser alcançável sem fechar o teclado (ou o formulário rola junto).
- Tipo certo de teclado por campo (`inputmode`, `type`) — ver `friccao-formularios.md`.
- Fonte de campo ≥ 16px pra evitar o zoom automático do iOS, que desloca todo o layout.
- Evite `100vh` em contêiner de formulário: em navegador móvel o `vh` não considera a barra do
  navegador e o conteúdo salta. Prefira `100dvh` ou altura mínima com conteúdo fluido.

## O que não existe no celular

- **Hover.** Nada essencial pode depender dele: menu suspenso, tooltip com informação crítica,
  imagem que só revela o preço no hover. Tudo isso precisa de equivalente por toque.
- **Precisão de mouse.** Não existe alvo de 12px.
- **Paciência.** Cada segundo de espera e cada rolagem extra tem custo real.
- **Tela larga.** Tabela com 6 colunas vira rolagem horizontal — reorganize em cartões.

## Orçamento de rolagem e primeira tela

Em ~3 rolagens a pessoa decide ficar ou sair. Na primeira tela precisam existir: **promessa
compreensível + uma pista de confiança + ação alcançável**.

- Hero de tela cheia com só um título gigante desperdiça essa tela. Deixe a próxima seção "espiar"
  pra sinalizar continuidade.
- Menu hambúrguer é aceitável, mas o que estiver dentro dele praticamente não é usado por tráfego
  frio. Não esconda a ação principal ali.
- Carrossel: a esmagadora maioria não passa do primeiro slide. Se a informação importa, não a
  coloque no slide 3. Prefira empilhar.

## Percepção de velocidade (é UX, não só performance)

A pessoa não mede milissegundos — mede se **a promessa apareceu**. Isso muda a prioridade técnica:

- O elemento que carrega primeiro deve ser o que comunica a promessa (título + imagem do hero).
  Nunca lazy-load na imagem do hero.
- Reserve o espaço de imagens (`width`/`height` ou `aspect-ratio`) pra evitar o salto de layout —
  layout que pula faz a pessoa clicar no lugar errado e é a principal causa de irritação silenciosa.
- Fonte customizada com `font-display: swap` pra o texto não ficar invisível esperando o download.
- Esqueleto (skeleton) comunica progresso melhor que um spinner girando sem fim.

Execução e medição são de `performance-senior` — aqui só o critério de UX: **primeiro pinta a
promessa, depois o resto.**

## Checagem rápida (faça sempre antes de entregar)

- [ ] Testado a 360px de largura, com uma mão mentalmente.
- [ ] CTA principal alcançável sem rolar, e de novo ao longo da página.
- [ ] Nenhum alvo < 44px; nada colado.
- [ ] Teclado certo em cada campo; nenhum campo escondido pelo teclado.
- [ ] Nada essencial atrás de hover.
- [ ] Sem rolagem horizontal em nenhuma seção.
- [ ] Barra fixa respeita a área segura e não cobre conteúdo.
- [ ] A promessa aparece antes de qualquer coisa carregar por completo.

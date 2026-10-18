# ux-senior — instalação e integração

Skill de **UX e conversão** (a camada de decisão). Irmã da `frontend-senior`, que cuida da estética
e do código. As duas rodam juntas em toda página; nenhuma substitui a outra.

## Onde ela está ativa

Neste repositório ela já funciona como **skill de projeto** (`.claude/skills/ux-senior/`) — qualquer
sessão do Claude Code aberta aqui a enxerga.

## Como usar em TODOS os seus projetos

Escolha um dos caminhos:

**A) Global na máquina (vale pra qualquer pasta local)**

```bash
cp -r .claude/skills/ux-senior ~/.claude/skills/ux-senior
```

**B) Sincronizada na conta (vale também no Claude na web/app, junto das outras `-senior`)**

Suba a pasta em claude.ai → Configurações → Capacidades/Skills, como você fez com as demais. É o
caminho recomendado, porque é onde `frontend-senior`, `copywriting` e as outras já vivem — e é o
único que funciona em sessão remota como esta.

## Ajuste necessário na `partner-senior` (1 linha)

A `partner-senior` é a camada de roteamento: é ela que decide quais skills disparam juntas. Ela ainda
não conhece a `ux-senior`. Edite a tabela de roteamento, na linha de página:

> | Página, landing page, site, componente React/HTML/CSS, hero, seção nova | `ux-senior` + `frontend-senior` + `seo-senior` + `performance-senior` + `code-security-senior` (sempre as cinco — página nasce convertendo, bonita, rankeável, rápida e segura ao mesmo tempo; `ux-senior` define a estrutura de decisão antes de `frontend-senior` desenhar) |

E acrescente uma linha nova, para auditoria:

> | Página existente que "não converte", pedido de revisão/auditoria, formulário abandonando, CTA fraco | `ux-senior` (Modo B — auditar antes de redesenhar; chama `frontend-senior` só depois do diagnóstico) |

Vale também citar `ux-senior` na lista de skills do primeiro parágrafo da descrição dela.

## Ajuste opcional na `frontend-senior`

No bloco "Roda junto com a família", acrescente:

> `ux-senior` define a estrutura de decisão (o que a página precisa fazer com a cabeça do visitante)
> antes de você desenhar; não refaça esse trabalho, execute-o com beleza.

## Divisão de trabalho (resumo)

| | `ux-senior` | `frontend-senior` |
|---|---|---|
| Pergunta | O que a página precisa fazer com quem lê? | Como isso fica lindo e vira código? |
| Entrega | Blueprint de conversão / auditoria priorizada | Tela e código de produção |
| Domínio | Público, objeções, fricção, CTA, formulário, mobile, confiança, ética, medição | Paleta, tipografia, espaço, grid, motion, assinatura, HTML/CSS/JS |

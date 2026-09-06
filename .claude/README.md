# Esteira do Portal do Tempo

Dois agentes e um comando que os encadeia.

| Peça | Arquivo | O que faz |
|---|---|---|
| `portal-arquiteto` | `agents/portal-arquiteto.md` | Lê o pedido, investiga o código, questiona a premissa, decide a abordagem e escreve uma spec em `specs/`. **Não escreve código.** |
| `portal-dev` | `agents/portal-dev.md` | Lê a spec, carrega as skills sênior obrigatórias, implementa e verifica contra os critérios de aceite. **Não redesenha o plano.** |
| `/portal` | `commands/portal.md` | Roda a esteira inteira e devolve só o resultado final. |

## Como chamar

```
/portal cria a página de produto individual
```

Ou os agentes soltos, quando você quiser só uma das metades:

```
usa o portal-arquiteto pra planejar a página de produto individual
usa o portal-dev pra executar a spec em .claude/specs/pagina-produto.md
```

## Quando NÃO usar

Ajuste pontual (texto, cor, link), bug que já se sabe onde está, ou pergunta sobre
o projeto: peça direto. A esteira custa duas partidas do zero — só vale quando existe
decisão de verdade a tomar.

## Como conferir se estão carregados

O antigo assistente `/agents` **foi removido** do Claude Code. E `/list-agents` mostra
agentes **em execução no momento**, não o catálogo do que existe — por isso ele
responde "No subagents" mesmo com tudo instalado. Não use nenhum dos dois para
verificar instalação.

O que funciona, em ordem de confiança:

1. **Pedir para o Claude chamar** — é o único teste que prova de ponta a ponta:
   ```
   usa o portal-arquiteto: PROBE — não leia arquivo, não crie spec.
   Responda em 3 linhas: seu nome, a regra da cor --laranja, e a
   restrição sobre imagem externa.
   ```
   Se ele citar "--laranja é exclusivo de CTA" e a CSP bloqueando imagem externa,
   o briefing carregou. Se responder genérico, o frontmatter está quebrado.

2. **Perguntar ao Claude** quais subagentes ele enxerga — a lista está no contexto dele.

3. **Conferir os arquivos**: `ls -la .claude/agents/`. Prova que existem no disco,
   não que o Claude os carregou.

Arquivo novo costuma ser carregado sem reiniciar. Se o probe falhar, aí sim abra
uma sessão nova.

## Em outra máquina

Estes arquivos vivem no repositório. Em outro computador, só existem depois de
`git pull` da branch que os contém. Sem isso, o Claude Code local não tem o que carregar.

Para usar em qualquer projeto, e não só neste repositório, copie os `.md` de `agents/`
para `~/.claude/agents/` — mas troque o briefing embutido, que é 100% Portal do Tempo.

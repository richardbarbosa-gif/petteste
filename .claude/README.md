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

## Importante

Arquivo de agente e de comando é lido **na abertura da sessão**. Depois de criar ou
editar qualquer um deles, abra uma sessão nova para o Claude Code enxergar.
Confira com `/agents`.

Para usar em qualquer projeto, e não só neste repositório, copie os `.md` de `agents/`
para `~/.claude/agents/`.

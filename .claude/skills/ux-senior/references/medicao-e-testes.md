# Medição e Testes — saber se funcionou, sem se enganar

Página sem medição é aposta com dinheiro do cliente. Mas medição mal feita é pior que nenhuma:
gera confiança em conclusão errada. Este documento cobre o mínimo viável e, principalmente, **quando
não testar**.

---

## Instrumentação mínima (toda página, sempre)

Não precisa de stack de dados. Precisa de quatro coisas:

1. **Conversão principal como evento** — envio de formulário bem-sucedido, clique no WhatsApp,
   agendamento concluído. Sem isso não existe conversa possível sobre resultado.
2. **Origem do lead** — de onde veio (anúncio, orgânico, indicação) e de qual seção da página.
   No WhatsApp isso sai de graça na mensagem pré-preenchida (ver `friccao-formularios.md`).
3. **Gravação de sessão e mapa de rolagem** (Microsoft Clarity é gratuito e suficiente). Vale mais
   que qualquer dashboard: **você vê a pessoa desistir**, e normalmente descobre o problema em 20
   minutos de gravação.
4. **Página/estado de sucesso separado** após conversão — dá evento confiável e não depende de
   parsing.

O que **não** medir a fundo em site de serviço local: taxa de rejeição isolada (interpretação
ambígua), tempo na página como meta (mais tempo pode ser confusão, não interesse), pageviews.
Servem de contexto, nunca de objetivo.

## Métricas que importam, em ordem

1. **Conversões absolutas** por semana. O número que o cliente sente.
2. **Taxa de conversão por origem.** Média geral esconde tudo: orgânico converte diferente de pago.
3. **Taxa de conclusão do formulário** (quantos começaram × quantos enviaram). Se cair muito aqui, o
   problema é o formulário, não a página.
4. **Profundidade de rolagem até o CTA.** Diz se a estrutura está entregando gente no lugar certo.
5. **Conversão por dispositivo.** Se mobile converte muito abaixo de desktop, o problema é
   ergonomia (ver `ux-mobile.md`), não copy.

## Quando A/B teste NÃO faz sentido (a maioria dos casos do Richard)

Teste A/B precisa de volume. Regra prática de tamanho de amostra por variante:

```
n ≈ 16 × p × (1 − p) ÷ δ²
p = taxa atual (ex: 0,02) · δ = ganho absoluto que você quer detectar (ex: 0,01)
```

Traduzindo pra realidade:

| Conversão atual | Ganho a detectar | Visitantes por variante | Com 30 visitas/dia |
|---|---|---|---|
| 2% → 4% (dobrar) | +2 p.p. | ~1.200 | ~2,5 meses |
| 2% → 3% (+50%) | +1 p.p. | ~3.900 | ~8,5 meses |
| 2% → 2,4% (+20%) | +0,4 p.p. | ~24.000 | inviável |

Ou seja: com o tráfego típico de um cliente local, **só ganho enorme é detectável, e mesmo assim
leva meses.** Rodar teste abaixo disso e "ver o resultado no terceiro dia" é ler ruído — e o pior
resultado possível é decidir errado com confiança.

**O que fazer nesse volume, em vez de A/B:**

- Aplicar as heurísticas deste conjunto de skills (é para isso que elas existem).
- **Gravação de sessão**: 20–30 sessões reais mostram mais que um mês de teste mal dimensionado.
- **Teste com 5 pessoas** (ver abaixo): encontra a maior parte dos problemas graves de usabilidade.
- **Mudança em bloco**: implemente o pacote das melhorias de alto impacto de uma vez e compare
  período contra período, ciente de que é indicativo, não prova. Diga isso ao cliente — comparar
  março com abril tem sazonalidade, campanha e sorte dentro.

Quando A/B **faz** sentido: infoproduto com tráfego pago pesado, e-commerce, página recebendo
milhares de visitas por semana. Aí sim: uma variável por vez, tamanho definido antes, e não pare o
teste no dia em que ele está ganhando.

## Teste dos 5 segundos

O mais barato e mais revelador que existe. Mostre a primeira tela por 5 segundos a alguém de fora do
projeto, feche e pergunte:

- O que essa empresa faz?
- Pra quem é?
- O que eles querem que você faça?
- (Bônus) Que sensação passou?

Se três pessoas erram a primeira pergunta, o hero está errado — não importa quão bonito esteja.
Funciona no WhatsApp com print, em 10 minutos.

## Teste com 5 usuários

Cinco pessoas do perfil real, uma tarefa clara ("descubra quanto custa e agende uma avaliação"), e
você **calado** olhando. A maior parte dos problemas graves de usabilidade aparece nas primeiras
cinco pessoas; a partir daí, os achados começam a se repetir.

Regras:
- Não explique nada, não ajude, não defenda a página. O silêncio é a técnica.
- Peça pra narrar o que está pensando.
- Observe onde ela **hesita**, não só onde erra. Hesitação é fricção que a pessoa não sabe nomear.
- 15 minutos por pessoa é suficiente.

Isso é vendável como serviço e é o tipo de entrega que faz o cliente perceber valor além do "site
bonito".

## Antes de comemorar

- **Correlação não é causa.** Conversão subiu no mês em que a página mudou *e* a campanha aumentou o
  orçamento? Você não sabe qual dos dois foi.
- **Sazonalidade existe** — dezembro não se compara com janeiro em quase nenhum setor.
- **Lead ≠ venda.** Se você dobrou os leads e o cliente diz que "não vem cliente", a mudança pode ter
  aumentado volume e derrubado qualidade. Meça o que acontece **depois** do lead sempre que houver
  acesso a esse dado — é a única métrica que o cliente realmente paga.

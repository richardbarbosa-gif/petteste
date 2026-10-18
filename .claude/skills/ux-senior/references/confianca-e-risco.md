# Confiança e Risco — o que realmente trava a conversão

O visitante não pergunta "isso é bom?". Pergunta **"e se eu me arrepender?"**. Conversão é o ponto
em que o desejo supera o risco percebido — e reduzir risco costuma ser mais barato e mais rápido que
aumentar desejo.

---

## Os quatro riscos que a pessoa calcula

1. **Risco financeiro** — "vou perder dinheiro?" → transparência de preço, garantia, parcelamento
   claro, ausência de custo escondido.
2. **Risco de resultado** — "vai funcionar pra mim?" → caso de alguém parecido, método explicado,
   critério honesto de quem não é indicado.
3. **Risco social** — "vou passar vergonha por ter escolhido isso?" → prova social, autoridade,
   reconhecimento local.
4. **Risco de tempo/esforço** — "vou me enrolar?" → processo em 3 passos, prazo declarado,
   facilidade de cancelar/remarcar.

Método: pra cada uma das 5 objeções do mapa (ver `descoberta-brief-ux.md`), identifique qual risco
ela representa e **qual elemento da página o reduz**. Objeção sem elemento correspondente é
conversão perdida silenciosamente.

## Sinais de confiança que funcionam

Em ordem de força real, não de facilidade:

1. **Especificidade verificável.** "312 cirurgias em 2024", "CRM-SP 123456", endereço com foto real
   do consultório. Número específico é lido como verdade; adjetivo é lido como marketing.
2. **Rosto e nome reais.** Foto da profissional > foto de banco de imagem, sempre — mesmo quando a
   foto de banco é "mais bonita". Autenticidade vence produção.
3. **Prova de terceiro.** Avaliação do Google com link, matéria na imprensa, certificação, selo de
   entidade.
4. **Transparência do processo.** O que acontece depois do clique, quem responde, em quanto tempo.
5. **Contato humano visível.** Endereço, telefone, CNPJ no rodapé. A ausência disso é lida como
   risco, mesmo inconscientemente.
6. **Sinais técnicos.** HTTPS, política de privacidade acessível, formulário que não parece
   improvisado. Não somam confiança quando presentes — mas destroem quando ausentes.

## Reversão de risco

Transferir o risco de volta pra quem vende é o movimento de conversão mais forte que existe — e o
mais subutilizado por serviço local:

- **Garantia explícita** quando existir ("7 dias pra pedir reembolso, sem pergunta").
- **Primeira etapa sem compromisso** ("avaliação inicial sem custo", "orçamento não obriga a nada").
- **Sem cartão / sem cadastro** pra dar o primeiro passo.
- **Cancelamento fácil e declarado.**
- Nunca prometa o que o cliente não vai honrar. Garantia que não é cumprida é problema jurídico, não
  problema de copy — e o Richard leva a fama junto.

## Transparência de preço

"Sob consulta" é uma decisão de UX, não um detalhe:

- **Mostrar preço** filtra desqualificado, aumenta confiança e reduz volume de lead. Bom quando o
  atendimento é o gargalo.
- **Esconder preço** aumenta volume e reduz qualidade, e faz parte do público sair procurando o
  preço em outro lugar (ou seja, no concorrente).
- Meio-termo honesto: **faixa** ("a partir de R$ X" / "projetos entre R$ X e R$ Y") ou o critério
  de precificação. Faixa converte melhor que silêncio na maioria dos serviços locais.

Decida com o cliente e diga o tradeoff — não deixe acontecer por omissão.

## Anti-padrões escuros (nunca use, e explique por quê)

Convertem no curto prazo e cobram caro depois — em reputação, em reclamação e, no Brasil, em
enquadramento no Código de Defesa do Consumidor como publicidade enganosa.

- Contador regressivo que reseta ao recarregar a página.
- "Restam 3 vagas" fixo no HTML.
- Notificação falsa de "alguém acabou de comprar".
- Depoimento inventado, foto de banco de imagem como cliente real, número de resultado sem lastro.
- Confirmshaming — "Não, prefiro continuar perdendo dinheiro" no botão de recusa.
- Checkbox de consentimento pré-marcado, ou opt-out escondido.
- Preço que só aparece no checkout; taxa surpresa no final.
- Cancelamento difícil de propósito.

Se o cliente pedir um desses, diga o custo com clareza: **um contador falso descoberto apaga toda a
confiança que a página construiu**, e a pessoa que descobre conta pra outras. Ofereça a alternativa
verdadeira: urgência real (turma que fecha, agenda que enche), escassez real (capacidade de
atendimento), prova real (as avaliações que ele já tem no Google e nunca usou).

## Profissões reguladas — sinalize ANTES de escrever a página

Boa parte dos clientes do Richard exerce profissão com conselho de classe, e o conselho restringe
publicidade. **O profissional é quem responde pelo processo ético — mas a página saiu das mãos do
Richard.** Levante isso no início do projeto, por escrito.

Padrões que costumam ser restritos ou vedados (confirme sempre a norma vigente do conselho
específico — as regras mudam e variam por profissão):

- **Promessa ou garantia de resultado** — comum em saúde e direito.
- **Imagens de antes/depois** e exibição de resultado de procedimento — fortemente restrito na área
  médica e odontológica.
- **Tom sensacionalista, superlativo e autopromoção** ("o melhor da região", "resultado garantido").
- **Preço, desconto, promoção e "condições imperdíveis"** — mercantilização do serviço, restrita em
  medicina, odontologia e advocacia.
- **Depoimento de paciente/cliente** — restrito em várias áreas de saúde e na advocacia.
- **Captação ativa de clientela** — vedada na advocacia; muda o que a página pode fazer.
- Exigência de **identificação profissional** (registro, número de inscrição, responsável técnico) em
  material publicitário.

Como agir na prática:
1. Pergunte no início: "qual o conselho e há restrição de publicidade a observar?".
2. Na dúvida, **projete a página no formato conservador** — autoridade, método, credencial e
   conteúdo informativo em vez de promessa e antes/depois. Converte bem e não cria risco.
3. Recomende que o profissional (ou o jurídico dele) valide o texto final. Isso protege o cliente e
   protege o Richard. Você não é o consultor jurídico — mas o sênior é quem levanta a bandeira antes,
   não depois da notificação.

## LGPD no básico da página

- Política de privacidade acessível do rodapé **e** do formulário.
- Microcopy de finalidade sob o botão de envio: pra que os dados serão usados.
- Consentimento explícito e desmarcado quando o uso extrapola o contato pedido (newsletter,
  remarketing).
- Não peça dado sensível sem necessidade real (CPF, dado de saúde num formulário de contato não
  tem por que existir).
- Aviso de cookies só quando há rastreamento além do essencial — e sem banner que bloqueia a leitura
  inteira da página. Implementação segura é de `code-security-senior`.

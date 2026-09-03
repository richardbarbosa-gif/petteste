# Fricção e Formulários — onde a conversão morre

O formulário é o ponto de maior perda da maioria das páginas e, ao mesmo tempo, o mais barato de
consertar. Antes de reescrever headline, conserte o formulário.

---

## Quantos campos?

Regra: **peça só o que é necessário pro próximo passo acontecer.** Não pro CRM ficar bonito, não
pro cliente "já saber tudo", não porque o formulário anterior tinha.

- Captação simples: **nome + WhatsApp**. Muitas vezes só o WhatsApp basta.
- Agendamento: nome, WhatsApp, e o dado que realmente muda o atendimento (procedimento, cidade).
- Orçamento B2B: nome, WhatsApp/e-mail, empresa, e **uma** pergunta de qualificação.

Cada campo adicional é um motivo pra desistir. Se o cliente insiste em 10 campos "pra qualificar",
faça o cálculo com ele: **é melhor 40 leads e qualificar no WhatsApp, ou 12 leads pré-qualificados?**
Na prática do serviço local, quase sempre o primeiro — e a qualificação vira automação
(`automation-senior`), não campo.

Campo que existe pra estatística interna ("como nos conheceu?") custa conversão. Se for
indispensável, deixe **depois** do envio, na tela de agradecimento — aí é grátis.

## Rótulos e microcopy

- **Rótulo sempre visível.** Placeholder como rótulo é anti-padrão consolidado: some quando a pessoa
  digita, some pra quem usa leitor de tela, e some justamente na hora da revisão.
- Rótulo acima do campo (mais rápido de ler no mobile que rótulo ao lado).
- Ajude com o formato **antes** do erro: "WhatsApp com DDD" resolve mais que uma mensagem de erro.
- Marque o **opcional**, não o obrigatório — na prática quase tudo é obrigatório, e um mar de
  asteriscos vira ruído.

## Validação e erros

- **Valide ao sair do campo** (blur), não a cada tecla. Erro vermelho enquanto a pessoa ainda digita
  o segundo caractere é hostil.
- Erro **junto do campo**, não num resumo no topo. E nunca só por cor: cor + texto + ícone, pra quem
  não distingue vermelho de verde.
- Erro que **ensina o conserto**: "Faltou o DDD — ex: (14) 99999-9999" em vez de "Campo inválido".
- Não limpe o formulário no erro. Perder o que já foi digitado é abandono garantido.
- Aceite o que o humano digita: telefone com ou sem parênteses, espaço, traço. Normalize no código,
  não exija do usuário.

## Mobile: teclado e autopreenchimento

É o detalhe que quase todo formulário erra e que muda a experiência inteira. Custa 10 minutos.

```html
<input type="tel"   name="whatsapp" inputmode="numeric" autocomplete="tel-national">
<input type="email" name="email"    inputmode="email"   autocomplete="email">
<input type="text"  name="nome"     autocomplete="name" autocapitalize="words">
<input type="text"  name="cep"      inputmode="numeric" autocomplete="postal-code">
```

- `inputmode` abre o teclado certo (numérico pra telefone e CEP) — menos toques, menos erro.
- `autocomplete` com token correto deixa o navegador preencher sozinho. Um formulário que
  autopreenche em dois toques converte melhor que qualquer texto de botão.
- Fonte do campo **≥ 16px**: abaixo disso o iOS dá zoom ao focar e desloca o layout inteiro.
- Verifique se o teclado não cobre o campo ativo nem o botão de envio. Isso trava gente de verdade.
- Ordem lógica de foco e `enterkeyhint` coerente (`next` / `send`) no fluxo de digitação.

## Botão de envio

- Diga o **resultado**, em primeira pessoa quando couber: "Quero minha avaliação", "Agendar
  consulta", "Receber orçamento". Nunca "Enviar" — não promete nada.
- **Estado de carregamento** obrigatório: sem ele a pessoa clica três vezes e gera três leads, ou
  acha que quebrou e sai. Desabilite durante o envio e mostre "Enviando...".
- Nada de "Limpar formulário" ao lado do envio. Só serve pra destruir o trabalho de quem errou o
  alvo.

## Depois do envio

O envio não é o fim — é o começo do relacionamento, e o momento de maior atenção da jornada.

- Confirmação **explícita e específica**: "Recebemos! A Dra. Ana responde no WhatsApp em até 2h
  úteis." Genérico ("Obrigado pelo contato") desperdiça o único momento em que a pessoa está 100%
  atenta.
- Diga **o que fazer agora**: salvar o número, olhar o WhatsApp, ver um conteúdo enquanto espera.
- É aqui que entram as perguntas opcionais, se houver.
- Página/estado de sucesso separado também é o que permite medir conversão direito (ver
  `medicao-e-testes.md`).

## WhatsApp: o caminho de menor fricção no Brasil

Pro público do Richard, o WhatsApp costuma converter melhor que formulário — pula o preenchimento e
já começa a conversa no canal onde o cliente responde.

```html
<a href="https://wa.me/5514999999999?text=Ol%C3%A1!%20Vim%20pelo%20site%20e%20quero%20agendar%20uma%20avalia%C3%A7%C3%A3o%20de%20harmoniza%C3%A7%C3%A3o%20facial.">
  Falar no WhatsApp
</a>
```

- **Mensagem pré-preenchida sempre** — e específica por origem/seção. Ela faz três coisas: elimina o
  "não sei o que escrever" (a maior barreira real), qualifica o lead na primeira linha, e diz de
  onde ele veio (rastreio grátis, sem parâmetro).
- Varie o texto por seção ("...vi a página de botox", "...quero orçamento de energia solar") pra
  saber o que gerou o contato.
- Deixe claro o horário de resposta. Expectativa alinhada evita o "ninguém me respondeu".
- **Alinhe com o atendimento.** WhatsApp que ninguém responde em 4 horas converte pior que
  formulário — a página não é o gargalo, e vale dizer isso ao cliente antes de otimizar pixel.
- Fallback: mantenha um formulário curto para quem está no desktop sem WhatsApp Web.

## Privacidade, consentimento e spam

- Uma linha de microcopy sob o botão: **"Seus dados são usados só para este contato. Não enviamos
  spam."** Reduz hesitação de forma mensurável e é o mínimo de transparência exigido pela LGPD.
- Link para a política de privacidade acessível a partir do formulário.
- Consentimento explícito **só quando o uso vai além do contato solicitado** (lista de e-mails,
  remarketing). Checkbox pré-marcado não é consentimento válido — e é anti-padrão escuro.
- Proteção anti-spam **invisível de preferência** (honeypot, rate limit no servidor). CAPTCHA de
  imagem é fricção pesada: use só se o spam estiver realmente inviabilizando o atendimento, e
  prefira as versões invisíveis. Implementação e validação server-side são de `code-security-senior`
  — nunca confie só na validação do navegador.

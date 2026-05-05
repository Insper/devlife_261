---
title: Django
subtitle: Conceitos do Django
---

Como [dissemos anteriormente](index.md#aprendendo-a-aprender), o Django possui **muitas** funcionalidades. Isso é comum em praticamente qualquer framework que você for utilizar e pode fazer com que o primeiro contato seja um pouco intimidador. Ao longo da sua carreira, você terá que aprender novos frameworks. Assim, mais do que aprender a utilizar um framework, queremos que você **aprenda a aprender a utilizar novos frameworks**. Um passo inicial importante é reconhecer que **você não entenderá todos os detalhes de uma vez**.

## Primeiros passos

Um bom começo é entender a estrutura geral do framework. No [handout anterior](conceitos.md), vimos que o navegador faz uma requisição para um servidor web e recebe uma resposta com a página. Agora abordaremos o que acontece dentro do servidor, ou seja, depois que a requisição chega até a devolução da resposta. Esses detalhes dependem das ferramentas escolhidas, então a partir de agora, trataremos o caso específico do Django. Considere a imagem a seguir:

![Fluxo da requisição no Django](django-flow.png)

À primeira vista, pode parecer muita coisa, mas vamos trabalhar cada uma das etapas desse fluxograma. Note que já tratamos as duas primeiras setas (requisição HTTP e porta) e a última (resposta HTTP) na [página anterior](conceitos.md). Ao final dessa série de handouts, você deve ser capaz de explicar brevemente o que ocorre em cada uma das etapas apresentadas na imagem acima.

Como ainda não nos aprofundamos em nenhuma das partes, apresentaremos apenas uma explicação inicial, para que você possa se guiar ao longo dos próximos handouts.

1. O navegador faz uma requisição para o servidor no endereço `192.123.234.1` na porta `8000` com o caminho `/caminho/escolhido`;
2. A requisição chega no servidor e é encaminhada para o Django, que está rodando na porta `8000`;
3. O Django compara o caminho (`/caminho/escolhido`) com os padrões disponíveis no arquivo `urls.py` para descobrir qual função deve ser executada;
4. A função a ser executada está definida no arquivo `views.py`. Essa função recebe a requisição como argumento e devolve uma resposta;
   1. A função de `view` pode acessar dados armazenados em um banco de dados através das classes de modelo, definidas no arquivo `models.py`;
   2. A função de `view` deve retornar um conteúdo, em geral no formato HTML. Para ajudar na construção do HTML, utilizamos arquivos de template. A `view` pode enviar dados para o template através de um dicionário de contexto.
5. A resposta da função é enviada de volta para o navegador, que renderiza a página.

Não se preocupe se não entender todos os itens acima. **Siga para os próximos handouts e retorne para ler novamente ao final de cada um deles** - a explicação abaixo se tornará gradativamente mais clara.

!!! exercise parsons no-indent id_ordem-dos-acontecimentos
    Para ajudar na fixação da ordem acima, arraste as linhas para o bloco da direita e ordene os eventos a seguir:

    ```text
    Requisição chega no servidor
    Caminho recebido é mapeado por urls.py para uma função
    Função do arquivo views.py é chamada
    View usa models.py para interagir com o banco de dados
    View usa templates para gerar a resposta HTML
    View devolve a resposta
    ```

    !!! answer
        <p class="wrong-answer">Todas as linhas devem ser movidas para o bloco da direita. Caso já tenha feito isso, alguma das linhas está na ordem errada.</p>
        <p class="correct-answer">Muito bem! É importante manter esta ordem em mente. Assim, quando for estudar partes específicas, você saberá em que parte do processo ela se encaixa. Isso também será muito útil quando precisar corrigir bugs, pois será mais fácil localizar a parte do programa que não está funcionando.</p>

Agora que tivemos uma visão geral do fluxo do framework, vamos [preparar o ambiente](../configuracao/index.md) para desenvolver nosso primeiro projeto com Django.

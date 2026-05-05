---
title: Django
subtitle: Conceitos gerais
---

O que acontece depois que você digita o endereço de uma página no seu navegador? Quais são os passos necessários para que a página chegue até a sua tela? Uma discussão muito mais aprofundada será realizada no terceiro semestre, mas vamos apresentar alguns conceitos iniciais.

A internet é essencialmente uma enorme rede de computadores (aqui consideramos "computadores" como um termo genérico que engloba celulares, tablets, notebooks, desktops, etc.) que se comunicam entre si. Cada computador nessa rede recebe um endereço único, chamado **endereço IP (Internet Protocol)**, que normalmente tem um formato parecido com este: "192.168.0.1" (4 números separados por ponto).

Um computador pode ter vários programas utilizando a internet. Por isso, além de um endereço, também é necessário definir uma **porta**, representada por um número inteiro. Algumas portas possuem significados específicos, outras podem ser utilizadas por qualquer programa. O que você deve saber por enquanto é que cada programa que se conecta à rede recebe uma porta diferente. Assim, para um programa se comunicar com outro entre computadores da rede, é necessário especificarmos **tanto o endereço IP quanto a porta**. Por exemplo: `192.168.0.1:8080` indica a porta `8080` do dispositivo no endereço `192.168.0.1`.

!!! exercise choice id_definicao-ip-e-porta
    Baseado no texto acima, indique a alternativa correta:

    - [ ] Um endereço IP identifica uma página da internet e uma porta identifica o tipo de dispositivo na rede
    - [ ] Uma porta identifica uma página da internet e um endereço IP identifica o tipo de dispositivo na rede
    - [x] Um endereço IP identifica um computador em uma rede e uma porta identifica um programa nesse computador
    - [ ] Uma porta identifica um computador em uma rede e um endereço IP identifica um programa nesse computador
    
    !!! answer
        Cada dispositivo conectado em uma rede é identificado por um endereço IP. Como é possível que diversos programas utilizem a rede, cada programa é identificado por uma porta diferente. Assim, os dados enviados para um programa chegam no destino desejado e não são enviados para o programa errado.

## O que acontece depois que você digita o endereço de uma página no seu navegador?

Agora sim, vamos responder as perguntas iniciais. Depois que você digita um endereço no seu navegador, o navegador envia uma mensagem para o computador localizado no endereço desejado, indicando que ele deseja receber uma página web. Essa mensagem de pedido é chamada **requisição** (ou *request*, em inglês). Um programa (no nosso caso, o Django) rodando nesse computador recebe a requisição e devolve o conteúdo solicitado (por exemplo: uma página no formato HTML). Essa mensagem devolvida pelo programa (servidor) é chamada **resposta** (ou *response*, em inglês). A página HTML contida na resposta é então renderizada (gera a representação visual a partir da string HTML) pelo navegador.

### E os arquivos CSS? E as imagens?

O processo é muito semelhante. Ao identificar no HTML que uma imagem deve ser inserida, o endereço definido no atributo `#!html src` é utilizado para realizar uma nova requisição, que dessa vez recebe uma nova resposta contendo a imagem. Por exemplo: para o elemento `#!html <img src="http://192.168.0.1:8080/imagem.png">`, o navegador realizará uma requisição para o computador no endereço `192.168.0.1`, para o programa rodando na porta `8080` solicitando o arquivo `imagem.png`.

O mesmo ocorre com os arquivos CSS e outros arquivos estáticos (ex: javascript).

### Mas como o programa sabe qual deve ser a resposta?

Até agora utilizamos a palavra "endereço" de forma geral para nos referirmos ao texto que digitamos no navegador. Entretanto, para não criarmos confusão com o endereço IP, utilizaremos o nome correto: Uniform Resource Locator (URL). Uma URL é composta por diversas partes. Por enquanto vamos nos focar nas principais. Considere o exemplo de URL a seguir: `http://192.168.0.1:8080/caminho/do/recurso`. Essa URL é composta por:

- **Protocolo:** a primeira parte da URL. Por enquanto não vamos nos preocupar com isso, pois neste primeiro momento sempre utilizaremos o HTTP. Você vai aprender mais sobre protocolos no terceiro semestre, então vamos nos focar nas outras partes.
- **Endereço:** no caso do exemplo é `192.168.0.1`.
- **Porta:** no caso do exemplo é a porta `8080`.
- **Caminho:** é análogo ao caminho de um arquivo. Ele indica qual recurso (ex: arquivo HTML, CSS ou imagem) queremos receber de volta na resposta.

O caminho define qual é a resposta esperada. Essa parte final da string é recebida pelo programa (Django), que então decide qual informação devolver para o cliente (navegador).

### Eu nunca vi uma URL com esse monte de números

Realmente, não é muito comum vermos URLs com endereço IP e porta no nosso dia a dia. É mais comum encontrarmos URLs como: `https://insper.edu.br` ou `https://google.com`. O que acontece por baixo dos panos é que o navegador solicita o endereço a um serviço chamado servidor DNS (Domain Name System), que devolve o endereço IP no formato que vimos neste handout. O servidor DNS também é uma preocupação para o terceiro semestre, portanto não entraremos em muitos detalhes por enquanto.

### Revisão

!!! exercise choice id_partes-da-url
    Considere a URL a seguir:

    ```
    http://192.168.32.18:8000/imagens/logotipo.png
    ```

    Qual é o endereço, caminho, porta e protocolo, respectivamente?

    - [ ] `http`, `192.168.32.18`, `8000`, `/imagens/logotipo.png`
    - [x] `192.168.32.18`, `/imagens/logotipo.png`, `8000`, `http`
    - [ ] `/imagens/logotipo.png`, `192.168.32.18`, `http`, `8000`
    - [ ] `192.168.32.18`, `http`, `/imagens/logotipo.png`, `8000`

    !!! answer
        Existem outras partes que podem ocorrer em uma URL. Essas outras partes serão apresentadas conforme a necessidade ao longo dos handouts.

Agora que sabemos os conceitos básicos do funcionamento da internet, vamos introduzir alguns [conceitos específicos do Django](conceitos-django.md).

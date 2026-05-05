---
title: URLs e Views
subtitle: Revisão
---

Retomando o nosso diagrama:

![Fluxo da requisição no Django](../introducao/django-flow.png)

Acabamos de implementar a view para o caminho (rota) vazio que devolve uma string com o conteúdo do "hello world". 

No diagrama acima, o fluxo percorrido passaria por:

1. Requisição HTTP;
2. Servidor;
3. Porta;
4. Django;
5. Caminho;
6. `urls.py`;
7. `views.py`;
8. Resposta HTTP.

Como dissemos anteriormente, toda a integração com o banco de dados ainda está em aguardo. Já chegaremos lá.

!!! exercise parsons no-indent id_ordem-dos-acontecimentos
    Mova as linhas para o bloco da direita, colocando-as em ordem de acontecimento (suponha que o caminho `ola/` está associado à view `#!python views.diga_oi`).

    ```text
    Navegador faz requisição para a URL http://localhost:8000/ola/
    Django procura o padrão "ola/" no arquivo urls.py
    Django chama a função views.diga_oi
    Valor devolvido pela função é enviado como resposta ao navegador
    ```

    !!! answer
        <p class="wrong-answer">Todas as linhas devem ser movidas para o bloco da direita. Caso já tenha feito isso, alguma das linhas está na ordem errada.</p>
        <p class="correct-answer">Muito bem! É importante manter esta ordem em mente. Assim, quando for estudar partes específicas, você saberá em que parte do processo ela se encaixa. Isso também será muito útil quando precisar corrigir bugs, pois será mais fácil localizar a parte do programa que não está funcionando.</p>

!!! exercise id_check-3
    Agora você pode implementar o Check 3. Leia o que deve ser feito na [lista de checks](../checks.md).

Agora sim, vamos [juntar o que aprendemos sobre views e urls com o que vimos anteriormente sobre modelos](../models-views-urls/index.md).

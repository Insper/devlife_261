---
title: Models, Views e URLs
subtitle: Revisão
---

Voltando ao nosso diagrama:

![Fluxo da requisição no Django](../introducao/django-flow.png)

!!! exercise parsons no-indent id_ordem-dos-acontecimentos
    Mova as linhas para o bloco da direita, colocando-as em ordem de acontecimento (suponha que o caminho `''` está associado à view `#!python views.index`).

    ```text
    Navegador faz requisição para a URL http://localhost:8000/
    Django procura o padrão "" no arquivo urls.py
    Django chama a função views.index
    Dados do banco de dados são carregados pela classe de modelos
    Dados dos modelos são utilizados para construir uma string HTML
    Valor devolvido pela função é enviado como resposta ao navegador
    ```

    !!! answer
        <p class="wrong-answer">Todas as linhas devem ser movidas para o bloco da direita. Caso já tenha feito isso, alguma das linhas está na ordem errada.</p>
        <p class="correct-answer">Muito bem! É importante manter esta ordem em mente. Assim, quando for estudar partes específicas, você saberá em que parte do processo ela se encaixa. Isso também será muito útil quando precisar corrigir bugs, pois será mais fácil localizar a parte do programa que não está funcionando.</p>

!!! exercise id_check-4
    Agora você pode implementar o Check 4. Leia o que deve ser feito na [lista de checks](../checks.md).

No [próximo handout](../templates/index.md) veremos como utilizar templates para separar a criação do HTML do resto do código da view.

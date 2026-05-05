---
title: Models, Views e URLs
subtitle: Interagindo com o banco de dados
---

Vimos que todas as classes de modelo do Django possuem um atributo `#!python objects` que nos permite interagir com a sua respectiva tabela no banco de dados. Vamos explorar algumas das possibilidades através da documentação. O objetivo é que você tenha alguma ideia do que é possível fazer. Você não precisa (talvez nem deva) decorar os nomes das funções. Quando precisar você pode procurar na internet, mas já fica mais fácil se você souber que existe uma funcionalidade que resolve o problema.

!!! exercise short id_l2l-docs-all
    Leia a [documentação do método `#!python all`](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#all). Explique em uma frase o que esse método faz.

    !!! answer
        Devolve uma cópia da lista (`#!python QuerySet`) de objetos atual.


!!! exercise short id_l2l-docs-filter
    Leia a [documentação do método `#!python filter`](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#filter). Explique em uma frase o que esse método faz.

    !!! answer
        Filtra os resultados deixando apenas os que correspondem aos valores de colunas/campos definidos nos argumentos.

!!! exercise short id_l2l-docs-exclude
    Leia a [documentação do método `#!python exclude`](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#exclude). Explique em uma frase o que esse método faz.

    !!! answer
        Filtra os resultados deixando apenas os que **não** correspondem aos valores de colunas/campos definidos nos argumentos.

!!! exercise short id_l2l-docs-order-by
    Leia a [documentação do método `#!python order_by`](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#order-by). Explique em uma frase o que esse método faz.

    !!! answer
        Devolve um novo `#!python QuerySet` com os elementos ordenados pela coluna definida nos argumentos.

!!! exercise short id_l2l-docs-reverse
    Leia a [documentação do método `#!python reverse`](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#reverse). Explique em uma frase o que esse método faz.

    !!! answer
        Inverte a ordem em que os elementos são retornados.

!!! exercise short id_l2l-docs-distinct
    Leia a [documentação do método `#!python distinct`](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#distinct). Explique em uma frase o que esse método faz.

    !!! answer
        Elimina duplicações no `#!python QuerySet`.

Muito bem, agora vamos para [mais uma revisão](revisao.md).

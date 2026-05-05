---
title: Relacionamentos Entre Modelos
subtitle: Filtrando através de relacionamentos
---

Ao chegar neste handout você já deve ter concluido o Check 4, para o qual era necessário ordenar as anotações por data de criação. Você também deve ter [lido a documentação de alguns outros métodos disponíveis](../models-views-urls/querysets.md), em especial, o `#!python filter`. Se você não se lembra ou não entendeu o que ele faz, não se preocupe. Vamos utilizá-lo neste handout e isso pode ajudar a esclarecer algumas coisas.

O método `#!python filter` pode ser usado para selecionar apenas os objetos que atendem a um determinado critério, removendo os que não cumprem esse critério. Por exemplo, poderíamos filtrar as anotações criadas depois de uma determinada data, para considerarmos apenas anotações recentes. Agora veremos que também é possível usar critérios de filtro baseados nos relacionamentos entre modelos.

Os argumentos do método `#!python filter` são utilizados para definir os critérios de filtro. No nosso caso, queremos apenas as anotações que foram criadas por um determinado usuário. Assim, podemos usar o código:

```python
usuario_selecionado = # COLOQUE AQUI O CÓDIGO QUE PEGA O USUÁRIO LOGADO
anotacoes_do_usuario = Note.objects.filter(author=usuario_selecionado)
```

!!! exercise short id_filter-order-by
    Você provavelmente já tem um `#!python Note.objects.order_by(argumentos_do_order_by)` no seu código. Nós podemos encadear esses resultados com:

    ```python
    anotacoes_do_usuario_ordenadas = Note.objects.filter(author=usuario_selecionado).order_by(argumentos_do_order_by)
    ```
    
    ou

    ```python
    anotacoes_do_usuario_ordenadas = Note.objects.order_by(argumentos_do_order_by).filter(author=usuario_selecionado)
    ```

    Ambas as versões funcionam, mas fazem processos ligeiramente diferentes. Qual você acha que será mais eficiente. Por que?

    !!! answer
        Para ordenar anotações é necessário fazer comparações duas a duas de suas datas de criação. Para decidir se um usuário é autor de uma anotação ou não, basta olhar o campo `#!python author`. Se fizermos a ordenação primeiro, faremos comparações entre muitas anotações que nem aparecerão no resultado final, por não terem sido criadas pelo usuário selecionado. Se aplicarmos primeiro o filtro por autor, sobram muito menos anotações para serem ordenadas e comparadas duas a duas. Assim, a primeira versão é provavelmente mais eficiente.

!!! exercise id_check-10
    Agora você pode implementar o Check 10. Leia o que deve ser feito na [lista de checks](../checks.md).

Parabéns!!! Você concluiu os handouts de Django básico!

Se quiser continuar estudando, tente resolver [este desafio](../desafio.md).

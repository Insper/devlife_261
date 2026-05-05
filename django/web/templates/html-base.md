---
title: Templates
subtitle: HTML base
---

No handout sobre a [estrutura do HTML](../../design/introducao-ao-html/estrutura/index.md) vimos que existem alguns elementos obrigatórios em qualquer documento HTML. Além desses elementos, vimos nos [princípios CRAP](../../design/crap/repeticao.md) e na [heurística 04](../../design/heuristicas-de-nielsen/04-consistencia.md) que é importante repetirmos elementos visuais entre as páginas do nosso sistema para criarmos uma consistência interna. Por exemplo, todas as páginas podem ter o mesmo menu na parte superior e o mesmo rodapé no final de todas as páginas.

Uma possível implementação é repetirmos esses elementos em todos os nossos templates. Porém, há uma maneira de evitar essa repetição de código:

!!! exercise id_templates
    Crie as pastas `notes/templates/notes` (sim, o `notes` é repetido mesmo) e então crie os dois arquivos a seguir

    === "notes/templates/notes/base.html"
        ```html
        --8<-- "aulas/web/templates/template-base.html"
        ```

    === "notes/templates/notes/index.html"
        ```html
        --8<-- "aulas/web/templates/template-index.html"
        ```

Mas por que dois arquivos? Para que eles servem?

O arquivo `base.html` possui o código HTML que vai se repetir em todas as páginas. No `index.html` nós usamos o {% raw %}`{% extends "notes/base.html" %}`{% endraw %} para indicar para o Django que nós queremos usar o `base.html` como base. Então modificamos apenas os blocos necessários. O que está entre o {% raw %}`{% block content %}`{% endraw %} e {% raw %}`{% endblock %}`{% endraw %} no `index.html` **substituirá** esse mesmo bloco no `base.html`. Você pode dar o nome que quiser para os seus blocos.

## Ok, mas como eu uso isso?

Vamos lá!

!!! exercise id_render
    Modifique o seu arquivo `notes/views.py` substituindo o seu conteúdo por:

    ```python
    from django.shortcuts import render
    from .models import Note

    def index(request):
        all_notes = # COLOQUE AQUI O CÓDIGO QUE LISTA TODAS AS ANOTAÇÕES ORDENADAS POR DATA DE CRIAÇÃO
        return render(request, 'notes/index.html', {'notes': all_notes})
    ```

    A função `render` recebe um `request`, o nome de um arquivo de template, um dicionário de contexto e gera um HTML a partir desses valores. Os itens do dicionário se tornam variáveis no template.

    Teste sua página.

!!! exercise choice id_variaveis-do-contexto
    Suponha que seu código possui a seguinte view:

    ```python
    from django.shortcuts import render

    def mostra_primeiro_semestre(request):
        todos_os_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
        return render(request, 'app/primeiro_semestre.html', {'meses': todos_os_meses})
    ```

    Qual deveria ser o conteúdo do arquivo `app/templates/app/primeiro_semestre.html` para mostrar uma lista com os meses do primeiro semestre corretamente?

    - [x] *
    ```html
    --8<-- "aulas/web/templates/ex-variaveis-do-contexto/a.html"
    ```
    - [ ] *
    ```html
    --8<-- "aulas/web/templates/ex-variaveis-do-contexto/b.html"
    ```
    - [ ] *
    ```html
    --8<-- "aulas/web/templates/ex-variaveis-do-contexto/c.html"
    ```
    - [ ] *
    ```html
    --8<-- "aulas/web/templates/ex-variaveis-do-contexto/d.html"
    ```

    !!! answer
        Os itens do dicionário de contexto são disponibilizados como variáveis para o template. A chave é o nome da variável (portanto não devemos usar as aspas) e o valor é o valor da variável.

Como sempre, antes de continuar, vamos para [mais uma revisão](revisao.md)!

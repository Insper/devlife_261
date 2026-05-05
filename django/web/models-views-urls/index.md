---
title: Models, Views e URLs
subtitle: Juntando tudo
---

Até o momento, ao acessar `http://localhost:8000/`, obtemos uma página de "hello world". Nós já adicionamos algumas anotações no banco de dados através do Django Admin. Agora aprenderemos a buscar esses dados no código da view.

Os acessos ao banco de dados no Django são realizados através das classes de modelo. Mais especificamente, o Django cria um atributo *em cada classe de modelo* chamado `#!python objects`, que nos permite interagir com o banco de dados. Por exemplo, você pode listar todas as anotações com `#!python Note.objects.all()`. Esse método devolverá algo [semelhante a uma lista]()[^1] de objetos do tipo `#!python Note`. Você pode percorrer essa lista com um `#!python for` para obter cada anotação separadamente.

[^1]: Seria mais preciso dizer que o método `#!python Note.objects.all()` devolve um objeto do tipo `#!python QuerySet`. Você pode consultar a [documentação desse tipo aqui](https://docs.djangoproject.com/en/4.2/ref/models/querysets/), mas neste primeiro momento, basta saber que ele funciona de maneira análoga a uma lista do Python.

!!! exercise id_objects-all
    Vamos alterar o arquivo `notes/views.py` para buscar a lista de todas as anotações do banco de dados. Adicione as funções abaixo no arquivo `notes/views.py`:

    ```python
    from django.http import HttpResponse
    from .models import Note

    def index(request):
        all_notes = Note.objects.all()
        for note in all_notes:
            print(note.title)

        return HttpResponse("<h1>Olá mundo!</h1><p>Este é o app notes de <em>DevLife do Insper</em>.</p>")
    ```

    Acesse a página novamente. Os títulos das suas anotações devem aparecer impressos **no terminal**.

!!! exercise id_objects-all-html
    Modifique novamente a função `#!python index` no arquivo `notes/views.py`. A função deve retornar um HTML de resposta como o abaixo. Note que o código abaixo é um exemplo. Os textos entre as tags `#!html <li>` e `#!html </li>` devem ser substituídos pelos títulos das anotações que estão no banco de dados.

    ```html
    <h1>Get-it</h1>

    <ul>
      <li>Lista de compras</li>
      <li>Recomendação de livro</li>
      <li>Recomendação de filme</li>
      <li>Lembrete</li>
      <li>Página de DevLife</li>
    </ul>
    ```

    O conteúdo acima será uma string. Você deve usar seus conhecimentos de Python para construir essa string a partir da variável `#!python all_notes` do exercício anterior. Além disso, você provavelmente não vai mais precisar do `#!python print`, ele estava lá só para você entender melhor o que está acontecendo.

    Teste novamente sua página. Agora ela deve mostrar uma lista com os títulos das anotações encontradas no banco de dados.

Antes de seguir, vamos explorar a documentação para conhecermos algumas das [possibilidades de interação com o banco de dados usando os modelos](querysets.md).

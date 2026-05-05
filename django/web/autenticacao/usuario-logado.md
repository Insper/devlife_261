---
title: Autenticação
subtitle: Mostrando usuário autenticado
---

Toda função de view recebe pelo menos um argumento, um objeto `#!python request`. Caso haja um usuário autenticado, o Django preenche o atributo `user` com os dados desse usuário (carregados do banco de dados através de uma classe de modelo).

!!! exercise request-user
    Adicione o seguinte `#!python print` na função `#!python index` do arquivo `notes/views.py` (a primeira linha já está no seu código):

    ```python
    def index(request):
        print(request.user, request.user.first_name, request.user.last_name)
    ```

    Recarregue a página inicial e veja a saída no terminal. Os dados do seu usuário devem aparecer no terminal. Caso não apareçam, certifique-se de que você adicionou um nome e sobrenome para ele pelo Django Admin.

!!! exercise context-user
    O usuário também está disponível no contexto do template. Apague o `#!python print` do exercício anterior e modifique o elemento `#!html <body>` do seu template `notes/templates/notes/base.html` para mostrar o primeiro nome do usuário autenticado:

    ```html
    --8<-- "aulas/web/autenticacao/template-base-usuario.html"
    ```

    Recarregue a página. O nome deve aparecer no topo.

Agora que já conseguimos mostrar os dados do usuário, vamos implementar o [logout](logout.md).

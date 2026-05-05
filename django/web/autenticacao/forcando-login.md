---
title: Autenticação
subtitle: Forçando o login
---

Suponha que para alguma de suas views é essencial que o usuário esteja logado. Uma forma de implementar essa funcionalidade seria com uma lógica semelhante a esta:

```python
def sua_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Resto do código da view, já sabendo que existe um usuário logado.
```

Entretanto, esse é um requisito tão comum, que o Django já tem uma funcionalidade pronta para isso. É o [decorator]()[^1] `#!python login_required`.

[^1]: Você não precisa saber o que é um decorator. Esse é um conceito avançado de Python. Para o nosso momento de estudo, basta saber como utilizá-lo. Se você tiver muita curiosidade, um bom começo é [este tutorial](https://realpython.com/primer-on-python-decorators/).

No caso da view acima, teríamos:

```python
from django.contrib.auth.decorators import login_required

@login_required
def sua_view(request):
    # Resto do código da view, já sabendo que existe um usuário logado.
```

Esse `#!python @login_required` antes da definição da função faz com que o usuário seja redirecionado automaticamente para a página de login se não estiver logado. Vamos fazer o teste no exercício abaixo.

!!! exercise id_login-required
    Adicione o `#!python @login_required` na sua view `index` no arquivo `notes/views.py`.

    Teste o fluxo completo novamente: faça o login, depois o logout. Você deve ser redirecionado automaticamente para a página de login ao invés de ver a página inicial após o logout.

!!! exercise id_check-9
    Agora o Check 9 deve estar quase completo. Verifique o que [falta implementar e conclua o check](../checks.md).

Estamos caminhando para o final desta série de handouts! Nosso último passo é aprendermos a [criar relacionamentos entre modelos](../relacionamentos/index.md).

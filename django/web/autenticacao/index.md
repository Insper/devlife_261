---
title: Autenticação
subtitle: Implementando o login
---

O Django já possui um app responsável pela autenticação de usuários. Inclusive, já utilizamos esse app para criar o usuário administrador, que usamos para criar anotações pelo Django Admin. Ele está listado nos `#!python INSTALLED_APPS` (no arquivo `getit/settings.py`): `#!python 'django.contrib.auth'`. Esse app já possui um modelo de usuário (além de outros, como permissões e grupos de usuários) e uma série de funcionalidades para aumentar a segurança do processo de autenticação.

Nosso objetivo agora é criar uma página de login, que utilize a infraestrutura existente do app `#!python 'django.contrib.auth'`, mas com o nosso próprio template (HTML) e estilo (CSS). Você pode consultar a [documentação das views de autenticação do Django aqui](https://docs.djangoproject.com/en/4.2/topics/auth/default/#module-django.contrib.auth.views) para mais detalhes.

## Configurando os padrões de URL

O app `#!python 'django.contrib.auth'` tem seus próprios padrões de urls e views já implementados. Para utilizá-los, podemos incluir o arquivo `urls.py` desse app no nosso arquivo de urls.

!!! exercise id_auth-urls
    Adicione na lista de padrões de url (`#!python urlpatterns`) do arquivo `getit/urls.py` o seguinte padrão:

    ```python
    path("accounts/", include("django.contrib.auth.urls"))
    ```

    Lembre-se que a ordem é importante. Coloque essa linha antes do `include` do seu app, pois ele corresponde à string vazia.

Ao incluir os padrões do app de autenticação, todo o trabalho dos arquivos `urls.py`, `views.py` e `models.py` já está incluso. O que precisamos fazer é definir os templates.

## Definindo o template de login

De acordo com a [documentação](https://docs.djangoproject.com/en/4.2/topics/auth/default/#django.contrib.auth.views.LoginView.template_name), o nome do arquivo de template da view de login é `registration/login.html`. Seguindo na documentação, vemos que o dicionário de contexto desse template contém 4 variáveis, das quais precisamos por enquanto apenas de uma: `#!python form`, que já possui os dados do formulário de login. Na sequência, há um exemplo de template. No exercício abaixo, simplificamos e traduzimos o template para o mínimo necessário.

!!! exercise id_login-form
    Crie o arquivo `notes/templates/registration/login.html` com o seguinte conteúdo:

    ```html
    --8<-- "aulas/web/autenticacao/template-login.html"
    ```

    Fique à vontade para adicionar classes e/ou elementos HTML para ajustar o seu estilo CSS.

    Acesse a URL `http://localhost:8000/accounts/login/` para testar as suas modificações até agora. Já deve ser possível fazer o login, mas a página seguinte resultará em um erro.

Já conseguimos fazer o login, mas ocorreu um erro, pois o login redireciona para a URL `http://localhost:8000/accounts/profile/`. Na [documentação](https://docs.djangoproject.com/en/4.2/topics/auth/default/#django.contrib.auth.views.LoginView.get_default_redirect_url) vemos que existe uma configuração `#!python LOGIN_REDIRECT_URL` para definirmos para qual URL o Django deve redirecionar no caso do login ser bem sucedido.

!!! exercise id_login-redirect-url
    Abra o arquivo `getit/settings.py` e adicione a linha abaixo (pode ser em qualquer lugar, mas para manter a organização, coloque no bloco do comentário `#!python # Password validation`):

    ```python
    LOGIN_REDIRECT_URL = '/'
    ```

    Volte para a página de login e tente fazer o login novamente.

O próximo passo é [mostrar a informação do usuário autenticado](usuario-logado.md) nas páginas.

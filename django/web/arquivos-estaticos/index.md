---
title: Arquivos estáticos
subtitle: Servindo arquivos estáticos com o Django
---

Além do HTML gerado pelo servidor, aplicações web normalmente precisam servir outros arquivos – como imagens, JavaScript, ou CSS – necessário para renderizar a página web completa. No Django, nós chamamos estes arquivos de "arquivos estáticos".

Para projetos pequenos isto não é tão relevante porque você pode manter os arquivos estáticos em qualquer lugar do seu servidor web. No entanto, em projetos grandes - especialmente aqueles compostos por múltiplas aplicações - trabalhar com múltiplos conjuntos de arquivos estáticos pode ser complicado.

É para isto que o app `django.contrib.staticfiles` serve: ele coleciona os arquivos estáticos de cada uma de suas aplicações (e qualquer outro lugar que você especifique) em um único local que pode ser facilmente servido em produção. Esse app já está na lista de `#!python INSTALLED_APPS` no seu arquivo `getit/settings.py`.

!!! exercise id_download-img
    Crie as pastas `notes/static/notes/img` e salve [esta imagem](logo-getit.png) em `notes/static/notes/img/logo-getit.png`.

!!! exercise id_template-com-estaticos
    {% raw %}
    No arquivo `notes/templates/notes/index.html`, modifique o começo do arquivo para que ele fique com as seguintes linhas (a primeira já está lá):

    ```
    {% extends "notes/base.html" %}
    {% load static %}
    ```

    Adicione também a linha abaixo, logo no começo do bloco `content`:

    ```html
    <img src="{% static 'notes/img/logo-getit.png' %}" width="100" height="60"/>
    ```
    {% endraw %}

    Nessas linhas nós indicamos para a engine de template do Django que queremos usar a [template tag `static`](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#static) e depois a utilizamos para carregar o caminho completo do arquivo estático `notes/img/logo-getit.png`.

    Agora sim, a imagem [deve ser carregada]()[^1].

[^1]: **Se a imagem não carregar...**

    Se você fez as modificações pedidas no exercício e a imagem não carregar, tente parar a execução do servidor e inicializar novamente.

## Outros arquivos estáticos
        
Assim como acabamos de fazer com a imagem, você pode adicionar outros arquivos estáticos (css, javascript, etc.) na pasta `notes/static/notes` e eles serão disponibilizados pelo servidor. Para manter a organização, você pode criar uma pasta `notes/static/notes/style` para colocar os arquivos css, um `notes/static/notes/scripts` para os arquivos javascript, e assim por diante.

!!! exercise id_check-8
    Agora você pode implementar o Check 8. Leia o que deve ser feito na [lista de checks](../checks.md).

Nosso próximo passo é implementar a [view de autenticação (login)](../autenticacao/index.md)

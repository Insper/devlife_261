---
title: URLs e Views
subtitle: Views com resposta HTML
---

Já sabemos fazer views que devolvem strings de texto. Em outros momentos do semestre também aprendemos a trabalhar com HTML para construir páginas web (por enquanto não vamos nos preocupar com o CSS). Agora chegou o momento de unir esses conhecimentos, pois na verdade, a string devolvida pela view **é uma string HTML**!

!!! exercise id_resposta-html
    Modifique sua view (função `#!python index` do arquivo `notes/views.py`) para que ela devolva uma resposta HTML:

    ```python
    def index(request):
        return HttpResponse("<h1>Olá mundo!</h1><p>Este é o app notes de <em>DevLife do Insper</em>.</p>")
    ```

    Verifique o resultado executando o servidor e acessando a página.

Agora sim isso está começando a se parecer com uma página! Antes de continuarmos, vamos [revisar o que vimos neste handout](revisao.md).

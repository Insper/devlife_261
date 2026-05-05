---
title: Modelagem inicial
subtitle: Revisão
---

No handout de [introdução aos conceitos do Django](../introducao/conceitos-django.md), apresentamos o seguinte diagrama:

![Fluxo da requisição no Django](../introducao/django-flow.png)

Ele representa o fluxo de trabalho do Django de forma geral. Vamos fazer uma breve pausa para refletir onde o que acabamos de aprender se encaixa.

!!! exercise choice id_revisao-migracoes
    Nossa classe de modelo foi adicionada no arquivo `models.py` e depois disso precisamos realizar alguns passos de criação e aplicação de migrações. Se depois de criar a classe no arquivo `models.py` nós não tivéssemos criado e aplicado as migrações, qual dos componentes abaixo não seria atualizado?

    - [ ] `urls.py`
    - [ ] `views.py`
    - [ ] templates
    - [ ] `models.py`
    - [x] banco de dados

    !!! answer
        Para atualizar as tabelas do banco de dados é necessário aplicar as migrações criadas a partir do código atualizado do arquivo `models.py`.

Agora sim, vamos seguir para as [urls e views](../urls-views/index.md).

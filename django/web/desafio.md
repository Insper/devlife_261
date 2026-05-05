---
title: Desafio
subtitle: Relacionamentos de muitos para muitos
---

Implemente um sistema de tags. Para isso, você deve criar uma nova classe de modelo chamada `#!python Tag` e adicionar em `#!python Note` um atributo `#!python tags`, que deve ser um `ManyToManyField`. Leia mais na documentação: https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_many/

Algumas restrições:

- Deve ser possível criar/adicionar tags no formulário de criação de anotações (não pode ser em um formulário separado - deve ser um campo de texto e as tags são separadas por vírgula ou ponto e vírgula);
- A visualização das anotações deve mostrar as tags de cada uma;
- Ao clicar em uma tag, deve-se abrir uma outra página com a lista de anotações do usuário que possuem aquela tag.

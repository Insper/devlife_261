---
title: Templates
subtitle: Introdução
---

Nas aulas sobre HTML você desenvolveu estruturas bem mais complexas e completas do que as que estamos utilizando até o momendo no Django. Por enquanto precisamos construir toda a string HTML dentro da função da view. Isso possui diversas desvantagens.

!!! exercise long id_desvantagens-string-html
    Comparado a criar um arquivo .html separado, quais desvantagens você identifica na nossa abordagem de construir o HTML como uma string no código da view?

    !!! answer
        Não existe apenas uma resposta correta. Alguns exemplos são:

        - Não temos *syntax highlighting* do HTML, então é mais difícil separar visualmente as tags e atributos do restante do conteúdo;
        - Não temos *auto complete*: no VS Code e outros editores de código, é possível habilitar a funcionalidade de auto completar código, que costuma facilitar o desenvolvimento;
        - O código da função fica mais longo e difícil de entender.

Apesar das desvantagens listadas acima, existe uma vantagem bastante significativa que obtemos ao construir a string HTML: podemos modificar a página de acordo com os dados mais atualizados do banco de dados. Assim, deixamos de ter apenas páginas que serão sempre iguais (estáticas) e passamos a ter páginas cujo conteúdo pode ser diferente (dinâmica) para cada usuário ou momento de acesso automaticamente.

Os templates HTML do Django unem a possibilidade de criação de páginas dinâmicas com as vantagens de utilizarmos um arquivo .html separado. Um template do Django é basicamente um arquivo HTML com algumas **funcionalidades extras**: ele é capaz de executar um código parecido com Python. Existem 4 elementos adicionais disponíveis nos templates Django:

- [Variáveis](https://docs.djangoproject.com/en/4.2/topics/templates/#variables): usadas pelo Django para substituir por um valor do contexto atual (explicaremos em breve o que é o contexto);
- [Tags](https://docs.djangoproject.com/en/4.2/topics/templates/#tags): adiciona lógica (ex: `#!python if`, `#!python for`) ao template;
- [Filtros](https://docs.djangoproject.com/en/4.2/topics/templates/#filters): podem modificar os valores das variáveis;
- [Comentários](https://docs.djangoproject.com/en/4.2/topics/templates/#comments): análogo aos comentários do Python, são trechos de código que serão ignorados pelo Django ao gerar o HTML.

O processo resumido do uso de templates é:

- Função de view chama a função de renderização de templates (função `#!python render`) passando o *nome do arquivo de template* e *um dicionário de contexto*. As chaves do dicionário de contexto estarão disponíveis no template como nomes de variáveis e os seus valores serão os valores vindos do dicionário. Por exemplo, se a função `#!python render` for chamada com o dicionário de contexto `#!python {"nome": "Maria", "idade": 19}`, o template poderá utilizar as variáveis `nome` (com valor `Maria`) e `idade` (com valor `19`).
- Django gera um HTML puro a partir do template e devolve para a view.
- A view retorna a resposta HTTP com o HTML gerado.

Abaixo apresentamos um exemplo de template com o mesmo conteúdo das strings que estávamos usando até o momento:

```html
--8<-- "aulas/web/templates/primeiro-template.html"
```

O exemplo acima possui 3 comentários, uma tag `for` e uma variável {% raw %}`{{ note.title }}`{% endraw %}, que será substituida pelo título da anotação atual. 

Note que a template tag {% raw %}`{% for %}{% endfor %}`{% endraw %} funciona de forma muito parecida com o `#!python for` do Python. O seu conteúdo é executado para cada elemento na lista fornecida. Uma das principais diferenças é a necessidade do {% raw %}`{% endfor %}`{% endraw %} ao final. Isso acontece porque no HTML as indentações não podem ser utilizadas para definir blocos como no Python. Além disso, existe uma tag intermediária {% raw %}`{% empty %}`{% endraw %}. Tudo o que vier depois dessa tag e antes do fim da tag `for` é adicionado apenas se o `for` não percorrer nenhum elemento. Isso é útil, por exemplo, para mostrar uma mensagem para o usuário em casos de listas vazias.

Note também que as variáveis são utilizadas de forma semelhante ao que fazemos para substituir o valor de variáveis em uma string usando f-strings: `#!python f'{ note.title }'`.

Esse HTML, entretanto, está incompleto. Nosso [próximo passo](html-base.md) é completá-lo com a estrutura básica de um arquivo HTML.

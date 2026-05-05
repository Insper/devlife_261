---
title: Acompanhamento do estudo
subtitle: Checks do estudo de Django
---

Você pode ganhar **até 1.0 ponto extra nas provas de Django** ao realizar os checks de estudo (cada check realizado e validado antes da prova vale 0.1 pontos).

**Data Limite: 14/05/2026 até às 18h30**

Os checks devem ser realizados no repositório do [GitHub classroom](https://classroom.github.com/a/cBmvoGyG) e validados com algum professor. Caso não sejam validados por um professor, os checks não contarão para a nota.

Cada um dos checks abaixo deve ser feito após a conclusão de um handout específico. **Faça o handout antes** de tentar implementar o check.

1. Criar estrutura básica do projeto Django e executar o servidor localmente. Para validar este check, o professor acessará o endereço `localhost:8000` e não pode ocorrer um erro (exemplo: página não encontrada ou algum erro do servidor). *Será feito durante o handout ["Configuração"](configuracao/index.md)*.

2. Implementação do modelo de anotações:
    1. Criar o app `notes`;
    2. Adicioná-lo ao `INSTALLED_APPS`;
    3. Criar a classe de modelo `#!python Note` com os campos `title`, `content` e `created_at` usando os tipos adequados;
    4. Criar as migrações;
    5. Executar as migrações;
    6. Criar um usuário admin;
    7. Adicionar o modelo ao Django Admin;
    8. Adicionar 5 anotações pelo Django Admin;
    9. Implementar o método `#!python __str__` da classe `#!python Note`.

    *Será feito durante o handout ["Modelagem inicial"](primeiro-modelo/index.md)*.

3. Além da view de "hello world", implemente o código necessário para que ao acessar a URL `#!python http://localhost:8000/creditos/` o navegador mostre o HTML: 
    ```html
    <h1>Créditos</h1>

    <p>Sistema web desenvolvido por SEU_NOME</p>
    ```

    *Pode ser feito após a conclusão do handout ["URLs e Views"](urls-views/index.md)*.

4. Mostre as anotações guardadas no banco de dados (que você criou pelo Django Admin) na página principal (você não deve mais mostrar o "hello world"). Você deve mostrar uma lista não ordenada (`#!html <ul>`) com o título de uma anotação por item (`#!html <li>`). Você não precisa mostrar o conteúdo das anotações por enquanto. **Importante:** as anotações devem ser apresentadas em ordem descrescente de data de criação, ou seja, as mais recentes devem aparecer primeiro (o método `#!python order_by` pode ser útil - consulte a [documentação aqui](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by)).

    *Pode ser feito após a conclusão do handout ["Models, views e URLs"](models-views-urls/index.md)*.

5. Utilize um template HTML para separar o conteúdo do check anterior em outro arquivo. Nesta versão, inclua também o conteúdo de cada anotação.

    *Pode ser feito após a conclusão do handout ["Templates"](templates/index.md)*.

6. Adicione na página inicial um formulário para a criação de novas anotações. Ao clicar no botão de enviar, uma nova anotação deve ser criada e incluida na lista de anotações mostrada na página. A view deve redirecionar para si mesma no caso do método POST.

    *Será feito durante o handout ["O método POST"](metodo-post/index.md)*.

7. **(Implemente a opção de deletar anotações)** Adicione um link para `/anotacoes/ID_DA_ANOTACAO/apagar` (onde `ID_DA_ANOTACAO` é um número inteiro representando o id da anotação selecionada) em cada anotação disponível. A view associada a essa URL deve apagar a anotação com o id selecionado do banco de dados e **redirecionar para a página principal**. Dica: utilize o método `#!python delete` disponível em cada objeto de modelo (consulte a [documentação aqui](https://docs.djangoproject.com/en/4.2/ref/models/instances/#deleting-objects)).

    - **(Implemente a opção de editar anotações)** Adicione também um link para `/anotacoes/ID_DA_ANOTACAO` em cada anotação. A view associada a essa URL deve mostrar uma página com os dados da anotação selecionada preenchidos em um formulário. Ao submeter o formulário, a anotação deve ser editada (título e conteúdo), mantendo o mesmo id, e a página deve ser **redirecionada para a página principal**. 

    - Deve haver dois links para cada anotação: um para apagar e outro para editar. 

    - Você pode editar um objeto no banco de dados [carregando-o](https://docs.djangoproject.com/en/4.2/topics/db/queries/#retrieving-a-single-object-with-get), modificando os atributos que desejar e então [salvando-o novamente](https://docs.djangoproject.com/en/4.2/topics/db/queries/#saving-changes-to-objects).

    *Pode ser feito após a conclusão do handout ["Parâmetros de URL"](parametros-de-url/index.md)*.

8. Adicione um estilo básico à sua página. Você deve criar um arquivo CSS separado e então carregá-lo como um arquivo estático em todas as páginas (você deve usar o template base para isso). Você não precisa se preocupar com a estética neste item. Ele apenas deve mostrar que você é capaz de carregar um arquivo CSS no seu HTML. Assim, é suficiente mudar a cor de fundo ou do texto para cumprir o check. Caso tenha interesse, você pode caprichar mais no estilo, mas sugerimos que você deixe isso para depois de terminar os outros checks.

    *Pode ser feito após a conclusão do handout ["Arquivos estáticos"](arquivos-estaticos/index.md)*.

9.  Implemente a autenticação (login e logout):
    1. Adicione uma página de login na rota `accounts/login/`. Ela deve permitir o login de um usuário com nome de usuário e senha. O usuário deve ter sido cadastrado pelo Django Admin, ou seja, você não precisa criar uma página de cadastro. 
    2. Mostre o nome e sobrenome do usuário logado em todas as páginas (adicione essa informação no template base). Para isso, abra os dados dos usuários no Django Admin e adicione nome e sobrenome nos seus usuários para fazer o teste.
    3. Ao lado do nome e sobrenome, adicione um botão que envia um POST para `accounts/logout/` (para isso será necessário criar um formulário). Esse link deve deslogar o usuário e redirecionar para a página de login.
    4. Force o login na página principal usando `@login_required`. Caso o usuário não esteja logado ele deve ser redirecionado para a página de login.

    *Pode ser feito após a conclusão do handout ["Autenticação"](autenticacao/index.md)*.

10. Limite as anotações ao usuário que a criou:
    1. Adicione um campo `#!python owner` do tipo [`#!python ForeignKey`](https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models.ForeignKey), representando o dono/criador da anotação, no modelo `#!python Note`.
    2. Crie e aplique as migrações (você deve informar um usuário padrão durante a criação da migração).
    3. Modifique o código de criação de anotações (em `notes/views.py`) para adicionar o usuário logado (`request.user`) como dono da nova anotação.
    4. Filtre as anotações mostradas na página principal para que apenas as anotações criadas pelo usuário logado sejam mostradas.
    5. Crie anotações de usuários diferentes para testar a funcionalidade acima.

    *Pode ser feito após a conclusão do handout ["Relacionamentos Entre Modelos"](relacionamentos/index.md)*.

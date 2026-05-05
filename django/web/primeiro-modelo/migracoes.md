---
title: Modelagem inicial
subtitle: Criando e aplicando migrações
---

Nós acabamos de criar nossa primeira classe de modelo do Django. O que falta é pedirmos para o Django criar a tabela que representa essa classe no banco de dados. Para isso precisaremos aprender sobre **migrações**. Uma migração é a forma do Django armazenar modificações no banco de dados (criação ou modificação de tabelas, por exemplo). Uma sequência de migrações define as instruções a serem executadas em um banco de dados para que tenhamos todas as tabelas que precisamos no nosso sistema.

Imagine que ao longo do desenvolvimento do projeto você descobre que precisa armazenar uma informação adicional nas anotações. Ao modificar o modelo `#!python Note` será necessário adicionar essa coluna no banco de dados. O problema é que o banco de dados pode já possuir valores armazenados. O que fazer com eles? Como atualizá-los? Qual deve ser o valor padrão utilizado nessa nova coluna para as linhas já existentes no banco? As migrações se responsabilizam por esse processo, facilitando a evolução do banco de dados em produção (ou seja, já está sendo utilizado por usuários reais).

!!! exercise id_makemigrations
    No seu projeto, execute o comando abaixo para o Django criar a migração da sua classe `#!python Note`:

    ```
    python manage.py makemigrations
    ```

!!! exercise id_migrate
    Agora vamos aplicar as migrações. Execute no terminal:

    ```
    python manage.py migrate
    ```

## Apareceram várias coisas no terminal!

Ao executar as migrações, o Django deve ter mostrado uma mensagem parecida com esta:

```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, notes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying notes.0001_initial... OK
  Applying sessions.0001_initial... OK
```

Note que uma das últimas é `Applying notes.0001_initial... OK`. Todas as outras são outros apps que já vêm instalados no Django por padrão. Quando executamos o comando `python manage.py migrate`, o Django procura pelas migrações de todos os apps instalados e aplica todas as que ainda não tiverem sido aplicadas.

!!! exercise id_reaplica_migracoes
    Execute **novamente** o comando

    ```
    python manage.py migrate
    ```

A saída deve ter sido muito mais curta desta vez:

```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, notes, sessions
Running migrations:
  No migrations to apply.
```

Isso acontece porque cada migração é aplicada apenas uma vez. O Django mantém o controle de quais migrações já foram aplicadas e quais não.

Por enquanto você está testando o servidor na sua máquina local. Em algum momento você pode querer disponibilizá-lo em um computador que fique sempre disponível na internet. Para configurar esse novo servidor, você deverá executar as migrações novamente, mas não será mais necessário criá-las. Ou seja, o comando `makemigrations` cria as instruções e por isso só precisa ser executado novamente se algum dos modelos mudar. O comando `migrate` aplica essas instruções no banco de dados e por isso deve ser executado novamente sempre que houver novas migrações, ou quando o servidor for disponibilizado em um novo computador.

Ok, agora nós criamos o banco de dados, mas como eu adiciono dados nele e vejo o que está armazenado? Boa pergunta! Siga para a [próxima etapa](admin.md)!


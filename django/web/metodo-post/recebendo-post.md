---
title: O método POST
subtitle: Recebendo um POST na view
---

Quando acessamos a página na URL `http://localhost:8000/`, o navegador faz uma requisição GET para o servidor. Quando preenchemos o formulário de criação de anotações e apertamos o botão de submissão, o navegador faz uma requisição POST **para a mesma URL**, enviando as informações do formulário. Como podemos saber a diferença?

O objeto `#!python request` recebido como argumento nas suas views possui um [atributo `method`](https://docs.djangoproject.com/en/4.2/ref/request-response/#django.http.HttpRequest.method). Esse atributo é uma string contendo o nome do método em letras maiúsculas (`#!python 'GET'` ou `#!python 'POST'`). Além disso, caso seja uma requisição do tipo POST, haverá também um [atributo `POST`](https://docs.djangoproject.com/en/4.2/ref/request-response/#django.http.HttpRequest.POST) com um dicionário (na verdade um *dictionary-like*) cujas chaves são os nomes (atributo `#!html name` dos inputs do formulário) dos inputs e os valores são os valores preenchidos pelo usuário.

!!! exercise id_recebe-post
    Modifique o arquivo `notes/views.py` com o seguinte conteúdo:

    ```python
    from django.shortcuts import render
    from .models import Note


    def index(request):
        if request.method == 'POST':
            title = request.POST.get('titulo')
            content = request.POST.get('detalhes')

            print(f'Titulo={title}\nConteudo={content}\n')
            
            # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
    
        all_notes = # COLOQUE AQUI O CÓDIGO QUE LISTA TODAS AS ANOTAÇÕES ORDENADAS POR DATA DE CRIAÇÃO
        return render(request, 'notes/index.html', {'notes': all_notes})
    ```

    Como você pode ver no comentário, sua tarefa é criar um novo `Note` no banco de dados com o título e conteúdo recebidos pela requisição. Esta página da documentação pode ser útil: https://docs.djangoproject.com/en/4.2/topics/db/queries/#creating-objects

!!! exercise short id_testa-recarregar-post
    Adicione uma anotação usando o formulário e recarregue a página algumas vezes (talvez o seu navegador pergunte se você quer ressubmeter o formulário - aceite a ressubmissão). A mesma anotação deve ser adicionada novamente a cada vez que você recarrega a página. Escreva abaixo por que você acha que isso está acontecendo.

    !!! answer
        Quando recarregamos a página, o navegador repete a requisição feita. Como a requisição que resultou nessa página foi um POST com os dados da nova anotação no formulário, uma nova anotação é criada.

## Redirecionando a resposta

Assim como existem diferentes tipos de requisição (GET e POST - existem outros, mas não vamos nos preocupar com eles por enquanto), existem também diferentes tipos de resposta. Toda resposta HTTP possui um código de status. São números entre 100 e 599. O mais comum de todos é o status 200, que significa que a requisição foi bem sucedida. Você já deve ter se deparado com pelo menos outros 2 ao longo de sua vida: o status 500 (erro do servidor - internal server error) e o status 404 (não encontrado). Na página anterior, tivemos também o erro 403 (acesso proibido). Cada código possui um significado, mas conhecê-los [não é o nosso objetivo no momento]()[^1].

[^1]: Caso tenha curiosidade, os códigos são organizados em famílias: de 100 a 199 são respostas de informação, de 200 a 299, respostas de sucesso, de 300 a 399, respostas de redirecionamento, de 400 a 499, respostas de erro do cliente, de 500 a 599, respostas de erro do servidor. Você pode ler este [documento da Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) que explica os códigos existentes. Ou você pode consultar as versões com gatinhos, que são muito melhores: https://httpcats.com/ e https://http.cat/.

Você não precisa saber todos os códigos de cor, mas acabará decorando os principais depois de usar algumas vezes. O que importa para nós desta discussão é que existe um código específico que indica um redirecionamento. A resposta com redirecionamento faz com que o navegador faça uma nova requisição para um novo endereço. É mais ou menos como se fosse uma placa na frente de uma loja dizendo "estamos temporariamente atendendo neste outro endereço".

Fizemos esta digressão para apresentarmos uma solução muito comum para o problema que encontramos em nosso último exercício. Sempre que recebermos uma requisição POST, fazemos o que foi solicitado e, ao invés de devolvermos a página HTML, devolvemos uma resposta de redirecionamento para o mesmo endereço. Assim, o navegador fará uma nova requisição GET para esse endereço. Veja o exercício abaixo:

!!! exercise id_adiciona-redirecionamento
    Modifique o código da sua view para adicionar o redirecionamento:

    ```python
    from django.shortcuts import render, redirect
    from .models import Note


    def index(request):
        if request.method == 'POST':
            title = request.POST.get('titulo')
            content = request.POST.get('detalhes')

            print(f'Titulo={title}\nConteudo={content}\n')
            
            # AQUI DEVE CONTINUAR O SEU CÓDIGO QUE CRIA A NOVA ANOTAÇÃO

            return redirect('index')
        else:  # GET
            all_notes = # COLOQUE AQUI O CÓDIGO QUE LISTA TODAS AS ANOTAÇÕES ORDENADAS POR DATA DE CRIAÇÃO
            return render(request, 'notes/index.html', {'notes': all_notes})
    ```

    Repita o teste do exercício anterior.

O que significa o `#!python 'index'` usado como argumento da função `#!python redirect`?

Por acaso é o mesmo nome da função, mas o Django procura pelo nome na lista de padrões de url no arquivo `urls.py`.

!!! exercise choice id_nome-url
    Suponha que ao invés de `#!python redirect('index')` quiséssemos usar o código `#!python redirect('inicial')`. Qual seria a modificação correta no arquivo `urls.py`?

    - [ ] `#!python path('', views.inicial, name='index')`
    - [x] `#!python path('', views.index, name='inicial')`

    !!! answer
        A `#!python redirect` usa o argumento para encontrar um padrão de url com o mesmo nome.

!!! exercise id_check-6
    Agora você pode implementar o Check 6 (na verdade, ele já deve estar pronto depois do último exercício - faça os testes, o commit e mostre para um professor). Leia o que deve ser feito na [lista de checks](../checks.md).

Nosso próximo passo é [receber parâmetros no caminho da URL](../parametros-de-url/index.md).

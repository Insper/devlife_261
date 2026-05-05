# Criando alguns modelos

Ao abrir este exercício no VS Code, você receberá um projeto Django já criado. O sistema a ser implementado é uma loja online que vende diversos tipos de produtos. Modifique o arquivo `produtos/models.py` adicionando uma classe `#!python Produto` com os atributos listados abaixo. Pesquise na [documentação](https://docs.djangoproject.com/en/4.2/ref/models/fields/#field-types) quais são os tipos adequados para cada um dos atributos.

- `#!python nome`: o nome do produto (com no máximo 100 caracteres);
- `#!python descricao`: um texto descrevendo o produto (sem limite de caracteres - pode ser um texto longo, mas também pode ser deixado em branco);
- `#!python preco`: deve armazenar o valor em reais com **exatamente duas casas decimais** (nenhum produto da loja excede o custo de R\$ 10.000,00);
- `#!python foto`: uma imagem do produto (a imagem deve ser salva na pasta `#!python 'uploads/imgs/'`);
- `#!python ultima_modificacao`: a data e hora da última modificação realizada neste objeto (deve ser atualizada automaticamente toda vez que o objeto é salvo).

!!! python-exercise-button

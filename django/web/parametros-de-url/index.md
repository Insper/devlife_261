---
title: Parâmetros de URL
subtitle: Passando mais argumentos para a view
---

Para o Check 7, precisamos receber parâmetros no caminho da URL. Por exemplo, quando recebermos uma requisição ao caminho `/anotacoes/ID_DA_ANOTACAO/apagar`, precisamos extrair a informação do `ID_DA_ANOTACAO` para apagarmos a anotação selecionada. Ou seja, se o caminho for `/anotacoes/2/apagar`, devemos apagar a anotação com id 2.

Felizmente, o Django já possui a funcionalidade de extração de parâmetros da URL. Apresentaremos apenas o que é necessário para o Check 7, mas você pode ler mais a respeito na documentação: https://docs.djangoproject.com/en/4.2/topics/http/urls/

Queremos receber um número inteiro representando o `ID_DA_ANOTACAO`. Assim, podemos usar o seguinte formato para o caminho:

```python
path('anotacoes/<int:note_id>/apagar', views.delete_note, name='delete-note')
```

Quando o Django encontra uma substring no formato `<TIPO:NOME_DE_VARIAVEL>`, ele tentará transformar essa parte do caminho no tipo selecionado e passará como argumento com o nome `NOME_DE_VARIAVEL` para a função da view. Por exemplo, se o caminho for `/anotacoes/15/apagar`, o Django fará a chamada da função `#!python views.delete_note(request, note_id=15)`. Assim, a sua função deve receber 2 argumentos: 

```python
def delete_note(request, note_id):
    # Usar o note_id para encontrar a anotação e apagar
```

!!! exercise id_parametros
    Antes de prosseguir, faça o exercício ["Parâmetros de URL"](../exercises/parametros_de_url/index.md).

!!! exercise id_check-7
    Agora você pode implementar o Check 7. Leia o que deve ser feito na [lista de checks](../checks.md).

Nosso sistema pode até estar funcional, mas por enquanto contém apenas HTML. Você já sabe escrever código CSS, mas ainda não sabemos como integrar esse tipo de arquivos ao Django. Esse é o nosso [próximo passo](../arquivos-estaticos/index.md).

---
title: O método POST
subtitle: Criando um formulário
---

O primeiro passo para podermos criar novas anotações é permitir que o usuário preencha essas informações em algum lugar da nossa página. Para isso utilizaremos as tags `#!html <form>` e `#!html <input>`.

!!! exercise id_adiciona-form
    Adicione o elemento a seguir no seu `notes/templates/notes/index.html`:

    ```html
    <form>
      <label for="titulo">Título</label>
      <input id="titulo" type="text" name="titulo" />
      
      <label for="detalhes">Detalhes</label>
      <textarea id="detalhes" name="detalhes"></textarea>
      
      <input type="submit" />
    </form>
    ```

    Recarregue a página para ver o resultado.

No código acima temos um formulário com 3 blocos de elementos. As tags `#!html <label>` são utilizadas para adicionar um texto relacionado a cada `#!html <input>`. Se quiser saber mais, consulte [esta página](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label). Uma característica útil dos `label`s é que ao ser clicado, o seu `input` recebe o foco da interação.

Ambas as tags de input de texto (`#!html <input>` e `#!html <textarea>`) possuem os atributos `id` e `name`. O `id` é utilizado pela página para associar o `for` do `#!html <label>` com o `input` correto. O `name` é utilizado como a chave de um dicionário que é enviado para o servidor (veremos mais detalhes em breve).

Finalmente, o último `#!html <input>` é o botão de submissão do formulário, que faz com que o navegador envie essas informações para o servidor. Agora, precisamos entender melhor [como as informações são enviadas ao servidor](verbos-http.md).

---
title: Django
subtitle: Introdução
---

O [Django](https://www.djangoproject.com/) é um framework de desenvolvimento web em Python utilizado por grandes projetos, como o Instagram(há alguns anos, o time de engenharia do Instagram fez uma [série de posts](https://instagram-engineering.com/static-analysis-at-scale-an-instagram-story-8f498ab71a0c) discutindo aspectos técnicos que são importantes para manter um projeto desse porte - talvez você ainda não tenha o conhecimento técnico suficiente para entender esses posts, mas guarde a referência para ler em 1 ou 2 anos). Mas antes de começarmos, precisamos ter uma breve discussão sobre essa palavra que já apareceu algumas vezes no texto: o que queremos dizer quando falamos que o Django é um "framework"?

## O que é um framework?

Essa é uma discussão para nos aprofundarmos mais no futuro. Por enquanto ficaremos com uma definição simplificada. Por enquanto, no nosso desenvolvimento de programas com Python, utilizamos algumas bibliotecas. A mais recente foi o Pygame.

A biblioteca Pygame, disponibiliza diversas funções que nos permitem criar janelas, desenhar na tela, receber eventos do usuário, etc. Cada uma dessas funções **é chamada pelo nosso programa na ordem que queremos, de acordo com a nossa necessidade**.

Em programação, um *framework* (ou *arcabouço* caso prefira uma palavra em português) é um conjunto de bibliotecas, ferramentas e padrões utilizados para facilitar o desenvolvimento. Ok, isso foi um pouco genérico. Simplificadamente, um framework já possui uma **estrutura de código pronta que chama as suas funções, de acordo com um padrão definido**.

Esse aspecto é bastante importante, pois será uma grande mudança na forma como programamos. Ao invés de escrever um programa que chama as funções que queremos, apenas definimos as funções e classes, e o framework chama cada uma delas no momento apropriado. O primeiro contato com essa outra forma de programar pode ser confusa a princípio, mas ficará mais fácil com a prática. Você utilizará diversos outros frameworks ao longo da graduação (e da sua vida profissional), portanto, a habilidade de aprender a utilizar um novo framework é bastante importante.

## Aprendendo a aprender

O Django possui **muitas** funcionalidades. O nosso objetivo com estes handouts é oferecer apenas uma introdução ao Django. Você provavelmente vai precisar ler outros tutoriais, a documentação do Django e fazer pesquisas para conseguir desenvolver seus projetos. Lembre-se que essa é uma habilidade essencial para a sua carreira. Portanto, sempre que encontrar uma solução na internet, **consulte a documentação** para garantir que as funções realmente fazem o que você acha que elas fazem. Conte com os professores para te ajudar com as dúvidas, mas é esperado que ao longo do curso você desenvolva a maturidade para pesquisar e aprender o que falta por conta própria.

!!! danger "Importante"
    Nesta disciplina nós utilizaremos o Django 5.X. É importante levar isso em conta quando for procurar respostas no Google. O [Django 5.1](https://docs.djangoproject.com/en/5.1/releases/5.1/) foi lançado em agosto de 2024, então será comum você encontrar respostas desatualizadas. **Sempre** que encontrar alguma função/método que não conhece, consulte a documentação da biblioteca para verificar se essa é a forma mais atualizada de se resolver o problema (essa dica vale para qualquer biblioteca/framework que for utilizar).

Agora sim, vamos introduzir alguns [conceitos importantes sobre o funcionamento da internet](conceitos.md).
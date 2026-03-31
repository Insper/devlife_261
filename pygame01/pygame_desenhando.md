# Resumo: Desenhando na Tela (Pygame)

## 1. Revisão da Estrutura do Jogo
Para desenhar elementos visuais na tela, atuamos principalmente na função `desenha` do loop principal do jogo.
A estrutura típica do nosso jogo se divide nestas 3 funções:
- **`inicializa`**: Inicializa o *pygame* e é o local correto para carregarmos todos os recursos (*assets*), como imagens e fontes.
- **`desenha`**: É aqui onde efetivamente pintamos coisas na janela.
- **`recebe_eventos`**: Lida com interação (teclado, mouse, etc).

## 2. Sistema de Coordenadas
O sistema do *Pygame* trata os pixels de forma específica:
- A origem `(0, 0)` fica no **canto superior esquerdo** da janela.
- O eixo **x** (horizontal) cresce para a **direita**.
- O eixo **y** (vertical) cresce para **baixo**.

## 3. Desenhando Polígonos e Cores
Cores no Pygame são representadas por tuplas **RGB** (Red, Green, Blue), onde cada canal varia de `0` a `255`. Exemplo: `(255, 0, 0)` é vermelho.
Podemos desenhar polígonos passando a superfície (`window`), a cor e os vértices originais.

```python
# Definimos a cor
cor = (255, 0, 0)
# Fornecemos a lista de vértices em sequência de coordenadas (x, y)
vertices = [(250, 0), (500, 200), (250, 400), (0, 200)]

# Desenha o polígono na nossa janela Surface
pygame.draw.polygon(window, cor, vertices)
```

## 4. Desenhando Imagens
O processo para utilização de imagens precisa de dois passos para garantir bom desempenho. 
**Passo 1: Carregar imagens (Em `inicializa`)**
Para carregar imagens utilizamos a função `pygame.image.load`. Guardar todas as variáveis em um dicionário de `assets` é uma excelente prática.

```python
def inicializa():
    # Inicializações gerais
    # ...
    assets = {}
    assets['img_sol'] = pygame.image.load('img/sol.png')
    
    return window, assets
```

**Passo 2: Desenhar na Tela (Em `desenha`)**
Tanto as imagens quanto nossa `window` são objetos `pygame.Surface`. Usamos a função `blit` para "colar" uma superfície na outra.

```python
def desenha(window, assets):
    # window.blit(imagem, (coordenada_x, coordenada_y))
    window.blit(assets['img_sol'], (150, 100))
```

## 5. Desenhando Texto
Assim como as imagens, textos precisam se transformar em objetos `pygame.Surface` na memória do computador.

**Passo 1: Carregar Fonte (Em `inicializa`)**
Nós carregamos os arquivos de fonte pelo caminho, ou podemos buscar a fonte padrão do sistema.
```python
fonte_padrao = pygame.font.get_default_font()
fonte = pygame.font.Font(fonte_padrao, 48) # Arquivo da fonte, e tamanho (= 48)
assets['fonte_padrao'] = fonte
```

**Passo 2: Renderizar Textos**
Usamos o `.render()` na fonte carregada para criar a superfície gráfica (imagem) do texto e, em seguida, desenhamos com `blit`.

```python
# render(texto_string, usar_antialiasing, cor_rgb)
imagem_texto = assets['fonte_padrao'].render('HELLO WORLD!', True, (0, 0, 255))

# Como qualquer outra imagem, enviamos para a tela usando blit:
window.blit(imagem_texto, (50, 30))
```

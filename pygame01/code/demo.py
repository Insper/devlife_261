import pygame

# Inicialização de constantes do jogo
WIDTH = 800
HEIGHT = 600
FPS = 60

# Cores em RGB (Vermelho, Verde, Azul)
BLACK = (0, 0, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)

def inicializa():
    """Inicializa o pygame, a janela e estabelece o estado inicial."""
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Demo: Pong, Bolas, Capivara")

    # Dicionário de recursos (assets)
    assets = {}
    fonte_padrao = pygame.font.get_default_font()
    assets['fonte_score'] = pygame.font.Font(fonte_padrao, 32)
    assets['capy'] = pygame.image.load('capy_fly.png')

    # Estado Inicial
    state = {
        'jogador_x': WIDTH // 2 - 50,  # Posição X inicial (no meio da tela)
        'jogador_y': HEIGHT - 40,      # Constante na base
        'jogador_largura': 100,
        'jogador_altura': 20,
        'vel_x': 0,                    # Velocidade de movimento
        'bolas': [],                   # Lista para guardar posições (x,y) de cada bola
        'vel_bola': 2,                 # Velocidade leve da gravidade
        'pontuacao': 0,
        'capy_x': -150,                # Posição X original da capivara (fora da tela)
        'capy_y': 50,                  # Altura do voo
        'vel_capy': 3                  # Velocidade de voo da capivara
    }

    return window, assets, state

def recebe_eventos(state):
    """Lida com a interação do usuário do Pygame, alterando o 'state'."""
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False

        # CLIQUE DO MOUSE: cria uma nova bola
        if evento.type == pygame.MOUSEBUTTONDOWN:
            # Pega as posições X e Y do clique e adiciona na lista de bolas
            x, y = evento.pos
            state['bolas'].append([x, y])

        # APERTAR TECLA DO TECLADO: Move jogador
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                state['vel_x'] = -7     # Define a velocidade de recuo
            elif evento.key == pygame.K_RIGHT:
                state['vel_x'] = 7      # Define a velocidade de avanço

        # SOLTAR TECLA DO TECLADO: Parar de mover
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT and state['vel_x'] < 0:
                state['vel_x'] = 0
            if evento.key == pygame.K_RIGHT and state['vel_x'] > 0:
                state['vel_x'] = 0

    return True

def desenha(window, assets, state):
    """Desenha a tela usando o estado com cores e primitivas."""
    # 1. Pinta todo o fundo de preto
    window.fill(BLACK)

    # 2. Desenha o paddle (Retângulo)
    jogador_rect = (
        state['jogador_x'], state['jogador_y'],
        state['jogador_largura'], state['jogador_altura']
    )
    pygame.draw.rect(window, AZUL, jogador_rect)

    # 3. Desenha todas as bolas armazenadas no estado
    for bola in state['bolas']:
        centro = (int(bola[0]), int(bola[1]))
        pygame.draw.circle(window, VERMELHO, centro, 10) # 10 é o raio

    # 4. Desenha a capivara voadora
    window.blit(assets['capy'], (state['capy_x'], state['capy_y']))

    # 5. Desenha a pontuação no canto superior direito
    texto_pontuacao = f"Pontos: {state['pontuacao']}"
    imagem_texto = assets['fonte_score'].render(texto_pontuacao, True, (255, 255, 255))
    largura_texto = imagem_texto.get_width()
    window.blit(imagem_texto, (WIDTH - largura_texto - 20, 20))

    # 6. Atualiza tudo que desenhamos acima
    pygame.display.update()

def atualiza_estado(state):
    """Atualiza a posição de acordo com a velocidade (chamada por frame)"""
    # Aplica velocidade ao jogador
    state['jogador_x'] += state['vel_x']

    # Movimenta e faz o wrap-around da capivara
    state['capy_x'] += state['vel_capy']
    if state['capy_x'] > WIDTH:
        state['capy_x'] = -150

    # Previne que o jogador saia da tela
    if state['jogador_x'] < 0:
        state['jogador_x'] = 0
    elif state['jogador_x'] + state['jogador_largura'] > WIDTH:
        state['jogador_x'] = WIDTH - state['jogador_largura']

    # Cria o retângulo do jogador para checar colisão
    jogador_rect = pygame.Rect(
        state['jogador_x'], state['jogador_y'],
        state['jogador_largura'], state['jogador_altura']
    )

    bolas_restantes = []
    # Bolas caem de forma constante e checam colisões
    for bola in state['bolas']:
        bola[1] += state['vel_bola']
        
        # Cria retângulo da bola (raio 10, centro = x,y)
        bola_rect = pygame.Rect(bola[0] - 10, bola[1] - 10, 20, 20)

        # Checa colisão
        if jogador_rect.colliderect(bola_rect):
            state['pontuacao'] += 1
            # Bola atingiu o jogador, não entra em 'bolas_restantes' (é apagada)
        elif bola[1] < HEIGHT + 20: 
            # Mantém a bola se não tiver saído totalmente da tela
            bolas_restantes.append(bola)
            
    state['bolas'] = bolas_restantes

def game_loop(window, assets, state):
    clock = pygame.time.Clock()
    rodando = True

    while rodando:
        clock.tick(FPS) # Roda a 60 vezes por segundo, garantindo velocidade contínua do jogador

        # Recebe a interação
        rodando = recebe_eventos(state)

        # Atualiza a física/posições independentemente do usuário interagir
        atualiza_estado(state)

        # Re-desenha quadro a quadro
        desenha(window, assets, state)

if __name__ == '__main__':
    window, assets, state = inicializa()
    game_loop(window, assets, state)
    pygame.quit()

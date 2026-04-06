import pygame
import math

# Inicialização de constantes do jogo
WIDTH = 800
HEIGHT = 600
FPS = 60

# Cores em RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 80)
RED = (220, 40, 40)
BLUE = (60, 120, 255)
GRAY = (180, 180, 180)

# Constantes de física
RAIO = 25
VX_PADRAO = 20
VY_PADRAO = 20
GRAVIDADE = 60

# Modos de criação de bola
MODO_MRU = 'mru'
MODO_MRUV = 'mruv'
MODO_PLAYER = 'player'

# Aceleração aplicada pelas teclas WASD na bola controlável
ACELERACAO_PLAYER = 200


def inicializa():
    """Inicializa o pygame, a janela e estabelece o estado inicial."""
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Demo: Física – MRU, MRUV e Controle")

    # Dicionário de recursos (assets)
    assets = {}
    assets['fonte_info'] = pygame.font.Font(pygame.font.get_default_font(), 20)
    assets['fonte_modo'] = pygame.font.Font(pygame.font.get_default_font(), 28)

    # Estado Inicial
    state = {
        'modo': MODO_MRU,          # Modo atual de criação de bolas
        'bolas': [],               # Lista de dicionários de bolas
        'last_updated': pygame.time.get_ticks(),  # Para cálculo de delta_t
    }

    return window, assets, state


def cria_bola(x, y, modo):
    """Cria e devolve um dicionário representando uma bola."""
    if modo == MODO_MRU:
        return {
            'tipo': MODO_MRU,
            'x': x,
            'y': y,
            'vx': VX_PADRAO,
            'vy': VY_PADRAO,
            'ax': 0,
            'ay': 0,
            'cor': GREEN,
        }
    elif modo == MODO_MRUV:
        return {
            'tipo': MODO_MRUV,
            'x': x,
            'y': y,
            'vx': VX_PADRAO,
            'vy': VY_PADRAO,
            'ax': 0,
            'ay': GRAVIDADE,   # Gravidade puxa para baixo
            'cor': RED,
        }
    elif modo == MODO_PLAYER:
        return {
            'tipo': MODO_PLAYER,
            'x': x,
            'y': y,
            'vx': 0,
            'vy': 0,
            'ax': 0,
            'ay': 0,
            'cor': BLUE,
        }


def recebe_eventos(state):
    """Lida com a interação do usuário, alterando o 'state'."""
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False

        # Troca de modo
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_u:
                state['modo'] = MODO_MRU
            elif evento.key == pygame.K_v:
                state['modo'] = MODO_MRUV
            elif evento.key == pygame.K_p:
                state['modo'] = MODO_PLAYER

        # Clique do mouse: cria bola no modo atual
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            bola = cria_bola(x, y, state['modo'])
            state['bolas'].append(bola)

    # ----- Controle contínuo WASD sobre a última bola criada -----
    keys = pygame.key.get_pressed()

    # Procura a última bola na lista (qualquer tipo pode ser pilotada)
    if state['bolas']:
        ultima = state['bolas'][-1]

        # Aceleração controlada pelo jogador
        ax_input = 0
        ay_input = 0
        if keys[pygame.K_a]:
            ax_input -= ACELERACAO_PLAYER
        if keys[pygame.K_d]:
            ax_input += ACELERACAO_PLAYER
        if keys[pygame.K_w]:
            ay_input -= ACELERACAO_PLAYER
        if keys[pygame.K_s]:
            ay_input += ACELERACAO_PLAYER

        if ultima['tipo'] == MODO_PLAYER:
            # Bola controlável: WASD define a aceleração
            ultima['ax'] = ax_input
            ultima['ay'] = ay_input
        else:
            # Para bolas MRU/MRUV, WASD altera a velocidade diretamente
            ultima['vx'] += ax_input * (1 / FPS)
            ultima['vy'] += ay_input * (1 / FPS)

    return True


def atualiza_estado(state):
    """Atualiza posições e velocidades de todas as bolas usando delta_t real."""
    # ---- Cálculo de delta_t (conforme slides/fisica.md) ----
    t1 = pygame.time.get_ticks()
    dt = (t1 - state['last_updated']) / 1000  # delta_t em segundos
    state['last_updated'] = t1

    for bola in state['bolas']:
        # ---- MRUV: atualiza velocidade pela aceleração ----
        # prox_velocidade = velocidade_atual + aceleracao * delta_t
        bola['vx'] = bola['vx'] + bola['ax'] * dt
        bola['vy'] = bola['vy'] + bola['ay'] * dt

        # ---- MRU (e MRUV após ajuste de velocidade): atualiza posição ----
        # prox_posicao = posicao_atual + velocidade * delta_t
        bola['x'] = bola['x'] + bola['vx'] * dt
        bola['y'] = bola['y'] + bola['vy'] * dt

        # ---- Colisões com as bordas (rebatimento) ----
        # Horizontal
        if bola['x'] - RAIO < 0:
            bola['x'] = RAIO
            bola['vx'] *= -1
        elif bola['x'] + RAIO > WIDTH:
            bola['x'] = WIDTH - RAIO
            bola['vx'] *= -1

        # Vertical
        if bola['y'] - RAIO < 0:
            bola['y'] = RAIO
            bola['vy'] *= -1
        elif bola['y'] + RAIO > HEIGHT:
            bola['y'] = HEIGHT - RAIO
            bola['vy'] *= -1

    # ---- Colisões entre bolas (colisão elástica, massas iguais) ----
    bolas = state['bolas']
    for i in range(len(bolas)):
        for j in range(i + 1, len(bolas)):
            a = bolas[i]
            b = bolas[j]

            dx = b['x'] - a['x']
            dy = b['y'] - a['y']
            dist = math.hypot(dx, dy)

            if dist < 2 * RAIO and dist > 0:
                # Vetor normal unitário (de a para b)
                nx = dx / dist
                ny = dy / dist

                # Separar as bolas para que não se sobreponham
                sobreposicao = 2 * RAIO - dist
                a['x'] -= nx * sobreposicao / 2
                a['y'] -= ny * sobreposicao / 2
                b['x'] += nx * sobreposicao / 2
                b['y'] += ny * sobreposicao / 2

                # Velocidades relativas projetadas na normal
                dvx = a['vx'] - b['vx']
                dvy = a['vy'] - b['vy']
                dot = dvx * nx + dvy * ny

                # Só colide se as bolas estão se aproximando
                if dot > 0:
                    # Para massas iguais, troca as componentes na normal
                    a['vx'] -= dot * nx
                    a['vy'] -= dot * ny
                    b['vx'] += dot * nx
                    b['vy'] += dot * ny


def desenha(window, assets, state):
    """Desenha a tela: bolas, indicadores de modo e texto de ajuda."""
    window.fill(BLACK)

    # 1. Desenha todas as bolas
    for bola in state['bolas']:
        centro = (int(bola['x']), int(bola['y']))
        pygame.draw.circle(window, bola['cor'], centro, RAIO)

    # 2. Destaca a última bola (a que é pilotada) com um anel branco
    if state['bolas']:
        ultima = state['bolas'][-1]
        centro = (int(ultima['x']), int(ultima['y']))
        pygame.draw.circle(window, WHITE, centro, RAIO + 3, 2)

    # 3. Texto indicador do modo atual no canto superior esquerdo
    nomes_modo = {
        MODO_MRU: 'MRU (verde)',
        MODO_MRUV: 'MRUV (vermelha)',
        MODO_PLAYER: 'Player (azul)',
    }
    texto_modo = f"Modo: {nomes_modo[state['modo']]}"
    img_modo = assets['fonte_modo'].render(texto_modo, True, WHITE)
    window.blit(img_modo, (20, 15))

    # 4. Texto de ajuda na parte inferior
    linha1 = "U para movimento uniforme, V para movimento uniformemente variável"
    linha2 = "P para bola controlável | WASD para pilotar a última bola"
    img1 = assets['fonte_info'].render(linha1, True, GRAY)
    img2 = assets['fonte_info'].render(linha2, True, GRAY)
    window.blit(img1, (WIDTH // 2 - img1.get_width() // 2, HEIGHT - 55))
    window.blit(img2, (WIDTH // 2 - img2.get_width() // 2, HEIGHT - 30))

    # 5. Atualiza a tela
    pygame.display.update()


def game_loop(window, assets, state):
    clock = pygame.time.Clock()
    rodando = True

    while rodando:
        clock.tick(FPS)

        # Recebe a interação
        rodando = recebe_eventos(state)

        # Atualiza a física/posições
        atualiza_estado(state)

        # Re-desenha quadro a quadro
        desenha(window, assets, state)


if __name__ == '__main__':
    window, assets, state = inicializa()
    game_loop(window, assets, state)
    pygame.quit()

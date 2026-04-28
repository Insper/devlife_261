import pygame
import pymunk
import math

# Constantes de Janela e Jogo
WIDTH = 1000
HEIGHT = 600
FPS = 60

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SKY_BLUE = (11, 138, 143)      # Um azul esverdeado agradável
BRICK_COLOR = (200, 100, 50)  # Cor de tijolo
DARK_BROWN = (60, 40, 20)
PLAYER_COLOR = (50, 200, 80)
POWER_COLOR = (255, 180, 0)
AIM_COLOR = (255, 255, 255)
UI_BG = (40, 40, 60)

# Física Pymunk
GRAVIDADE = 900
RAIO_EXPLOSAO = 150
FORCA_EXPLOSAO = 1500

# Projétil
RAIO_PROJETIL = 5
VELOCIDADE_MAXIMA_TIRO = 1200


def inicializa():
    """Inicializa o pygame, a janela e estabelece o estado inicial."""
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Worms Armageddon - Demo Pymunk")

    assets = {
        'fonte_ui': pygame.font.Font(pygame.font.get_default_font(), 22),
        'fonte_pequena': pygame.font.Font(pygame.font.get_default_font(), 16)
    }

    state = cria_estado_inicial()
    return window, assets, state



def cria_estado_inicial():
    """Cria e recria o mundo (espaço), blocos e jogador."""
    space = pymunk.Space()
    space.gravity = (0, GRAVIDADE)
    

    # Chão estático
    piso_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    piso_shape = pymunk.Segment(piso_body, (0, HEIGHT - 50), (WIDTH, HEIGHT - 50), 10)
    piso_shape.friction = 1.0
    piso_shape.elasticity = 0.0
    piso_shape.collision_type = 0
    space.add(piso_body, piso_shape)
    
    # Paredes laterais invisíveis para segurar os blocos
    wall_esq = pymunk.Segment(piso_body, (0, 0), (0, HEIGHT), 20)
    wall_dir = pymunk.Segment(piso_body, (WIDTH, 0), (WIDTH, HEIGHT), 20)
    wall_esq.friction = 1.0
    wall_dir.friction = 1.0
    space.add(wall_esq, wall_dir)

    # Criação do cenário: Montes de Tijolos
    largura_tijolo, altura_tijolo = 24, 12
    massa_tijolo = 2.0
    momento_tijolo = pymunk.moment_for_box(massa_tijolo, (largura_tijolo, altura_tijolo))

    # Construindo "morros" de blocos
    for i in range(16):
        for j in range(16 - i):
            x = 250 + j * largura_tijolo + (i * largura_tijolo / 2)
            y = HEIGHT - 65 - altura_tijolo/2 - i * altura_tijolo
            body = pymunk.Body(massa_tijolo, momento_tijolo)
            body.position = (x, y)
            shape = pymunk.Poly.create_box(body, (largura_tijolo, altura_tijolo))
            shape.friction = 0.8
            shape.elasticity = 0.0
            shape.collision_type = 0
            space.add(body, shape)
            
    # Segundo bloco mais "quadrado"
    for i in range(25):
        for j in range(18):
            # Empilhando colunas juntas
            x = 650 + j * (largura_tijolo + 1)
            y = HEIGHT - 65 - altura_tijolo/2 - i * (altura_tijolo + 1)
            body = pymunk.Body(massa_tijolo, momento_tijolo)
            body.position = (x, y)
            shape = pymunk.Poly.create_box(body, (largura_tijolo, altura_tijolo))
            shape.friction = 0.9  # Mais atrito pra não escorregarem sozinhos
            shape.elasticity = 0.0
            shape.collision_type = 0
            space.add(body, shape)

    # Estado isolado do Jogador
    jogador = {
        'x': 100,
        'y': HEIGHT - 65, # Em cima do chão
        'angulo': 45,     # Angulo de mira (0 a 180 graus)
        'forca': 0,       # Pct de força de 0 a 100
        'carregando': False
    }

    state = {
        'space': space,
        'jogador': jogador,
        'projetil_shape': None,   # Shape atual do projetil viajando
        'projetil_body': None,
        'explosao_pendente': None, # Posição em caso de explosão
        'pedir_reset': False,
        'btn_reset': pygame.Rect(WIDTH - 130, 20, 110, 40)
    }
    
    def trata_colisao(arbiter, space_inst, data):
        if state['explosao_pendente'] is None:
            pontos = arbiter.contact_point_set
            if len(pontos.points) > 0:
                pos = pontos.points[0].point_a
                state['explosao_pendente'] = (pos.x, pos.y)
        return False

    space.on_collision(1, 0, begin=trata_colisao)
    
    return state


def aplica_explosao(space, posicao_x, posicao_y):
    """
    Quando ocorre a explosão, varre os corpos no raio e aplica um
    impulso violento neles, empurrando para longe do centro.
    """
    for body in space.bodies:
        # Apenas afeta corpos dinâmicos (ignoramos o chão estático)
        if body.body_type == pymunk.Body.DYNAMIC:
            dx = body.position.x - posicao_x
            dy = body.position.y - posicao_y
            dist = math.hypot(dx, dy)
            
            if 0 < dist < RAIO_EXPLOSAO:
                # O impulso decai de forma linear baseado na distância 
                # (blocos mais longe sofrem menos efeito)
                fator_forca = 1.0 - (dist / RAIO_EXPLOSAO)
                impulso_base = FORCA_EXPLOSAO * fator_forca
                
                # Normalizando as componentes e aplicando a força
                nx = dx / dist
                ny = dy / dist
                
                impulse = (nx * impulso_base, ny * impulso_base)
                
                # Empurrão extra para "cima" para dar mais sensação dramática de desmoronamento
                impulse_y_extra = impulso_base * 0.15
                impulse = (impulse[0], impulse[1] - impulse_y_extra)
                
                # Applica na origem real do mundo onde o objeto se encontra
                body.apply_impulse_at_world_point(impulse, body.position)


def atira_projetil(state):
    """Lê os parâmetros de mira do jogador, cria o corpo do projétil e joga no Pymunk."""
    jogador = state['jogador']
    space = state['space']
    
    # Conversões e Trigonometria
    rad = math.radians(jogador['angulo'])
    velocidade = (jogador['forca'] / 100.0) * VELOCIDADE_MAXIMA_TIRO
    
    vx = velocidade * math.cos(rad)
    vy = -velocidade * math.sin(rad) # Y no pygame inverte
    
    massa = 5.0
    momento = pymunk.moment_for_circle(massa, 0, RAIO_PROJETIL)
    
    body = pymunk.Body(massa, momento)
    
    # Boca do canhão
    pos_x = jogador['x'] + 35 * math.cos(rad)
    pos_y = jogador['y'] - 35 * math.sin(rad)
    body.position = (pos_x, pos_y)
    body.velocity = (vx, vy)
    
    shape = pymunk.Circle(body, RAIO_PROJETIL)
    shape.collision_type = 1 # Define esse grupo específico para o handler de colisao
    shape.friction = 0.5
    shape.elasticity = 0.5
    
    space.add(body, shape)
    
    state['projetil_body'] = body
    state['projetil_shape'] = shape
    jogador['forca'] = 0 # Reinicia barra


def recebe_eventos(state):
    """Lida com inputs de interface e de jogo."""
    jogador = state['jogador']
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False
            
        # Botão Reset na UI
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if state['btn_reset'].collidepoint(evento.pos):
                state['pedir_reset'] = True

        if evento.type == pygame.KEYDOWN:
            # Carregamento do tiro no espaço (apenas se não houver tiro ativo)
            if evento.key == pygame.K_SPACE:
                if state['projetil_body'] is None:
                    jogador['carregando'] = True
                    jogador['forca'] = 0
            
            # Atalho de reset
            if evento.key == pygame.K_r:
                state['pedir_reset'] = True
                
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_SPACE:
                if jogador['carregando']:
                    jogador['carregando'] = False
                    atira_projetil(state)

    # Teclas mantidas pressionadas para mirar
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        jogador['angulo'] += 1.5
        if jogador['angulo'] > 180: jogador['angulo'] = 180
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        jogador['angulo'] -= 1.5
        if jogador['angulo'] < 0: jogador['angulo'] = 0
        
    return True


def atualiza_estado(state, dt):
    """Atualização central da física."""
    jogador = state['jogador']
    space = state['space']
    
    # Carregamento da barra de força
    if jogador['carregando']:
        jogador['forca'] += 90 * dt  # Leva pouco mais de 1s para encher ao maximo
        if jogador['forca'] > 100:
            jogador['forca'] = 100
            
    # Executa os steps da engine de física. Dividimos o dt em pequenos pedaços
    # sub-steps garantem que os blocos fiquem estáveis e colidam bem (melhor precisão)
    passos = 4
    for _ in range(passos):
        space.step(dt / passos)
        
    # Verifica se explodiu via nosso handler
    if state['explosao_pendente'] is not None:
        px, py = state['explosao_pendente']
        aplica_explosao(space, px, py)
        
        # Limpa da tela o missil
        space.remove(state['projetil_body'], state['projetil_shape'])
        state['projetil_body'] = None
        state['projetil_shape'] = None
        
        state['explosao_pendente'] = None
        
    # Também destrói sumariamente o tiro se ele escapar para o infinito ou afundar muito
    if state['projetil_body'] is not None:
        pos = state['projetil_body'].position
        if pos.y > HEIGHT + 100 or pos.x < -200 or pos.x > WIDTH + 200:
            space.remove(state['projetil_body'], state['projetil_shape'])
            state['projetil_body'] = None
            state['projetil_shape'] = None


def desenha(window, assets, state):
    """Pinta Pygame inteiro a cada frame baseando nos Shapes lógicos do Pymunk"""
    window.fill(SKY_BLUE)
    space = state['space']
    jogador = state['jogador']
    
    # --- RENDERIZAÇÃO DA FISICA ---
    for shape in space.shapes:
        if isinstance(shape, pymunk.Segment):
            p1 = shape.body.local_to_world(shape.a)
            p2 = shape.body.local_to_world(shape.b)
            pygame.draw.line(window, DARK_BROWN, (p1.x, p1.y), (p2.x, p2.y), int(shape.radius)*2)
            
        elif isinstance(shape, pymunk.Poly):
            # Obtem a localização atualizada (rotação e traslação) de todos os vertices do retangulo
            vertices = [shape.body.local_to_world(v) for v in shape.get_vertices()]
            pontos_poly = [(v.x, v.y) for v in vertices]
            
            # Pinta interior e depois borda
            pygame.draw.polygon(window, BRICK_COLOR, pontos_poly)
            pygame.draw.polygon(window, BLACK, pontos_poly, 1) 
            
        elif isinstance(shape, pymunk.Circle):
            pos = shape.body.position
            pygame.draw.circle(window, BLACK, (int(pos.x), int(pos.y)), int(shape.radius))

    # --- JOGADOR E CANHÃO ---
    jx, jy = int(jogador['x']), int(jogador['y'])
    
    # Desenha sprite basico do jogador
    pygame.draw.rect(window, PLAYER_COLOR, (jx - 15, jy - 20, 30, 20), border_radius=8)
    # Olho de verme kkk
    pygame.draw.circle(window, WHITE, (jx + 5, jy - 12), 4)
    pygame.draw.circle(window, BLACK, (jx + 6, jy - 12), 1)

    # Canhao simples direcional
    rad = math.radians(jogador['angulo'])
    fim_canhao_x = jx + 35 * math.cos(rad)
    fim_canhao_y = jy - 35 * math.sin(rad)
    pygame.draw.line(window, BLACK, (jx, jy - 5), (fim_canhao_x, fim_canhao_y), 6)
    
    # === Mira parabólica (Avançada) ===
    # Apenas pinta o preview balístico caso nao esteja rolando nenhum tiro no momento
    if state['projetil_body'] is None:
        # Pega forca, mas mantemos um minimo de pontinhos senao fica invisivel
        vel_preview = VELOCIDADE_MAXIMA_TIRO * max((jogador['forca'] / 100.0), 0.15) 
        vx_mira = vel_preview * math.cos(rad)
        vy_mira = -vel_preview * math.sin(rad)
        px, py = fim_canhao_x, fim_canhao_y
        
        t = 0
        passo_tempo = 0.05
        # Plota ate 40 bolinhas da trajetória
        for _ in range(40):
            # Posicoes classicas da equacao M.R.U (x) e M.R.U.V (y)
            px_futuro = px + (vx_mira * t)
            py_futuro = py + (vy_mira * t) + (0.5 * GRAVIDADE * t**2)
            
            if py_futuro > HEIGHT - 30: # Evita desenhar mira que fura muito o chão estético
                break
                
            pygame.draw.circle(window, AIM_COLOR, (int(px_futuro), int(py_futuro)), 2)
            t += passo_tempo

    # --- UI DA INTERFACE DOS STATUS ---
    
    # Background Box no topo
    pygame.draw.rect(window, UI_BG, (15, 15, 330, 85), border_radius=10)
    pygame.draw.rect(window, WHITE, (15, 15, 330, 85), 2, border_radius=10)
    
    # Angulo
    text_angulo = assets['fonte_ui'].render(f"Ângulo (Setas): {int(jogador['angulo'])}°", True, WHITE)
    window.blit(text_angulo, (30, 25))
    
    # Força
    text_forca = assets['fonte_ui'].render("Força (Espaço):", True, WHITE)
    window.blit(text_forca, (30, 60))
    
    # Trackpad escuro
    base_barra = pygame.Rect(180, 64, 140, 20)
    pygame.draw.rect(window, BLACK, base_barra)
    
    # Progress barra ligth (laranja)
    largura_fill = int(140 * (jogador['forca'] / 100.0))
    if largura_fill > 0:
        fill_barra = pygame.Rect(180, 64, largura_fill, 20)
        pygame.draw.rect(window, POWER_COLOR, fill_barra)
    
    # Botão Reseta Cenário
    pygame.draw.rect(window, UI_BG, state['btn_reset'], border_radius=5)
    pygame.draw.rect(window, WHITE, state['btn_reset'], 2, border_radius=5)
    text_reset = assets['fonte_ui'].render("RESET [R]", True, WHITE)
    window.blit(text_reset, (state['btn_reset'].x + 8, state['btn_reset'].y + 8))

    pygame.display.update()


def game_loop(window, assets, state):
    clock = pygame.time.Clock()
    rodando = True

    while rodando:
        # FPS em 60 e Time Delta em segundos para simulacao perfeita de Pymunk
        dt = clock.tick(FPS) / 1000.0
        
        rodando = recebe_eventos(state)
        
        # Interceptação Global: Realiza o Reset destruindo state antigo e criando novo
        if state.get('pedir_reset', False):
            state = cria_estado_inicial()
            continue

        atualiza_estado(state, dt)
        desenha(window, assets, state)


if __name__ == '__main__':
    window, assets, state = inicializa()
    game_loop(window, assets, state)
    pygame.quit()

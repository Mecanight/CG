import pygame
import sys
import random

pygame.init()

preto = (0, 0, 0)
branco = (255, 255, 255)

largura = 800
altura = 600
screen = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("Pong")

# Definição da Raquete
largura_raquete = 10
altura_raquete = 60
tamanho_bola = 10

# Posição da Raquete do PC
pc_x = 10
pc_y = altura // 2 - altura_raquete // 2

# Posição da raquete do Player
player_1_x = largura - 20
player_1_y = altura // 2 - altura_raquete // 2

# Posição da bola
bola_x = largura // 2 - tamanho_bola // 2
bola_y = altura // 2 - tamanho_bola // 2

# Velocidade das raquetes
raquete_player_1_dy = 10
raquete_pc_dy = 10

# Velocidade da bola
velocidade_bola_x = 5
velocidade_bola_y = 5

# Gerar 02 números aleatórios
aleat1 = random.randint(-31, 31)
aleat2 = random.randint(-31, 31)

# Inicializando a pontuação dos jogadores
score_player_1 = 0
score_pc = 0

font_file = "Pong-Maluco/font/PressStart2P-Regular.ttf"
font = pygame.font.Font(font_file, 36)

clock = pygame.time.Clock()

rodando = False


def menu_principal():
    global rodando
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    rodando = True
                    return

        # Renderiza o texto do menu
        screen.fill(preto)
        texto_menu = font.render("Pong", True, branco)
        text_menu_rect = texto_menu.get_rect(center=(largura // 2, altura // 2))
        screen.blit(texto_menu, text_menu_rect)

        tempo = pygame.time.get_ticks()
        # Pressionou Space para jogar:
        if tempo % 2000 < 1000:
            texto_iniciar = font.render("Pressione Espaço", True, branco)
            texto_iniciar_rect = texto_iniciar.get_rect(center=(largura // 2, 450))
            screen.blit(texto_iniciar, texto_iniciar_rect)

        pygame.display.flip()


menu_principal()

while rodando:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            rodando = False

    screen.fill(preto)

    # Movendo a bola
    bola_x += velocidade_bola_x
    bola_y += velocidade_bola_y

    # Retangulos de colisão
    bola_rect = pygame.Rect(bola_x, bola_y, tamanho_bola, tamanho_bola)
    raquete_pc_rect = pygame.Rect(pc_x, pc_y, largura_raquete, altura_raquete)
    raquete_player_1_rect = pygame.Rect(
        player_1_x, player_1_y, largura_raquete, altura_raquete
    )

    # Colisão da bola com a raquete do player_1 e a raquete do pc
    if bola_rect.colliderect(raquete_pc_rect) or bola_rect.colliderect(
        raquete_player_1_rect
    ):
        # TO DO aperfeiçoar isso
        raquete_pc_rect.y += aleat1

        # TO DO aperfeiçoar isso
        raquete_player_1_rect.y += aleat2

        velocidade_bola_x = -velocidade_bola_x

    # Colisão da bola com as paredes inferior e superior
    if bola_y <= 0 or bola_y >= (altura - tamanho_bola):
        velocidade_bola_y = -velocidade_bola_y

    # Reposivionar a bola quando ela passar/sair as bordas laterais
    if bola_x > largura:
        bola_x = largura // 2 - tamanho_bola // 2
        bola_y = altura // 2 - tamanho_bola
        velocidade_bola_x = -velocidade_bola_x
        score_pc += 1
        print(f"Score PC: {score_pc}")

    if bola_x < 0:
        bola_x = largura // 2 - tamanho_bola // 2
        bola_y = altura // 2 - tamanho_bola
        velocidade_bola_x = -velocidade_bola_x
        score_player_1 += 1
        print(f"Score Player 1: {score_player_1}")

    # Movendo a raquete do pc pra seguir a bola
    if bola_x <= largura // 2:
        if pc_y + altura_raquete // 2 < bola_y:
            pc_y += raquete_pc_dy
        elif pc_y + altura_raquete // 2 > bola_y:
            pc_y -= raquete_pc_dy

    # Movendo a raquete do player_1 pra seguir a bola
    # if player_1_y + altura_raquete // 2 < bola_y:
    #     player_1_y += raquete_pc_dy
    # elif player_1_y + altura_raquete // 2 > bola_y:
    #     player_1_y -= raquete_pc_dy

    # Evitar que a raquete do pc saia da área da tela
    if pc_y < 0:
        pc_y = 0
    elif pc_y > altura - altura_raquete:
        pc_y = altura - altura_raquete

    # Mostrando Score do jogo
    fonte_score = pygame.font.Font(font_file, 16)

    score_texto_pc = fonte_score.render(f"Score PC: {score_pc}", True, branco)
    score_texto_py = fonte_score.render(f"Score Player: {score_player_1}", True, branco)

    score_rect_pc = score_texto_pc.get_rect(center=(200, 18))
    score_rect_py = score_texto_py.get_rect(center=(600, 18))

    screen.blit(score_texto_pc, score_rect_pc)
    screen.blit(score_texto_py, score_rect_py)

    pygame.draw.rect(screen, branco, (pc_x, pc_y, largura_raquete, altura_raquete))

    pygame.draw.rect(
        screen, branco, (player_1_x, player_1_y, largura_raquete, altura_raquete)
    )

    pygame.draw.ellipse(screen, branco, (bola_x, bola_y, tamanho_bola, tamanho_bola))
    pygame.draw.aaline(screen, branco, (largura // 2, 0), (largura // 2, altura))

    # Para mover a raquete do player com o teclado
    keys = pygame.key.get_pressed()
    if keys[pygame.K_KP_8] and player_1_y > 0:
        player_1_y -= raquete_player_1_dy
    if keys[pygame.K_KP_2] and player_1_y < (altura - altura_raquete):
        player_1_y += raquete_player_1_dy

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
sys.exit()

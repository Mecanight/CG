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

raquete_player_1_dy = 5
raquete_pc_dy = 5

# velocidade da bola
velocidade_bola_x = 5
velocidade_bola_y = 5

ponto_player = 0
ponto_pc = 0

clock = pygame.time.Clock()

aleat1 = random.randint(-31, 31)
aleat2 = random.randint(-31, 31)

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
        ponto_pc += 1
        bola_x = largura // 2 - tamanho_bola // 2
        bola_y = altura // 2 - tamanho_bola
        velocidade_bola_x = -velocidade_bola_x
    if bola_x < 0:
        ponto_player += 1
        bola_x = largura // 2 - tamanho_bola // 2
        bola_y = altura // 2 - tamanho_bola
        velocidade_bola_x = -velocidade_bola_x

    # Movendo a raquete do pc pra seguir a bola
    if pc_y + altura_raquete // 2 < bola_y:
        pc_y += raquete_pc_dy
    elif pc_y + altura_raquete // 2 > bola_y:
        pc_y -= raquete_pc_dy

    # Movendo a raquete do player_1 pra seguir a bola
    if player_1_y + altura_raquete // 2 < bola_y:
        player_1_y += raquete_pc_dy
    elif player_1_y + altura_raquete // 2 > bola_y:
        player_1_y -= raquete_pc_dy

    # Evitar que a raquete do pc saia da área da tela
    if pc_y < 0:
        pc_y = 0
    elif pc_y > altura - altura_raquete:
        pc_y = altura - altura_raquete

    pygame.draw.rect(screen, branco, (pc_x, pc_y, largura_raquete, altura_raquete))

    pygame.draw.rect(
        screen, branco, (player_1_x, player_1_y, largura_raquete, altura_raquete)
    )

    pygame.draw.ellipse(screen, branco, (bola_x, bola_y, tamanho_bola, tamanho_bola))

    # Para mover a raquete do player com o teclado
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_w] and player_1_y > 0:
    #     player_1_y -= raquete_player_1_dy
    # if keys[pygame.K_s] and player_1_y < (altura - altura_raquete):
    #     player_1_y += raquete_player_1_dy

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()

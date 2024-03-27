import pygame
import sys

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
raquete_pc_1_dy = 5

clock = pygame.time.Clock()

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.fill(preto)

    pygame.draw.rect(screen, branco, (pc_x, pc_y, largura_raquete, altura_raquete))

    pygame.draw.rect(
        screen, branco, (player_1_x, player_1_y, largura_raquete, altura_raquete)
    )

    pygame.draw.ellipse(screen, branco, (bola_x, bola_y, tamanho_bola, tamanho_bola))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and player_1_y > 0:
        player_1_y -= raquete_player_1_dy
    if keys[pygame.K_s] and player_1_y < (altura - altura_raquete):
        player_1_y += raquete_player_1_dy

    pygame.display.flip()

    clock.tick(120)

pygame.quit()
sys.exit()

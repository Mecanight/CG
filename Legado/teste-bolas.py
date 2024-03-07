import sys
import pygame
import random

pygame.init()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pygame")

preto = (0,0,0)
branco = (255,255,255)
cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
cor1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

pygame.draw.circle(tela, branco, [320, 320], 30, 0)
pygame.draw.circle(tela, branco, [320, 320], 30, 0)

clock = pygame.time.Clock()

velocidade_x = random.randint(-1, 1)
vx = 0
velocidade_y = random.randint(-1, 1)
vy = 0

velocidade_x1 = random.randint(-1, 1)
velocidade_y1 = random.randint(-1, 1)


posicao_x = random.randint(0, 800)
posicao_y = random.randint(0, 600)

posicao_x1 = random.randint(0, 800)
posicao_y1 = random.randint(0, 600)

# while velocidade_x == 0:
#     velocidade_x = random.randint(-1, 1)
# while velocidade_y == 0:
#     velocidade_y = random.randint(-1, 1)


#Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    posicao_x += velocidade_x
    posicao_y += velocidade_y

    posicao_x1 += velocidade_x1
    posicao_y1 += velocidade_y1

    if posicao_x > (largura - 22):
        velocidade_x = -1
        cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if posicao_x1 > (largura - 22):
        velocidade_x1 = -1
        cor1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if posicao_x < 22:
        velocidade_x = 1
        cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if posicao_x1 < 22:
        velocidade_x1 = 1
        cor1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if posicao_y > (altura - 22):
        velocidade_y = -1
        cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if posicao_y1 > (altura - 22):
        velocidade_y1 = -1
        cor1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if posicao_y < 22:
        velocidade_y = 1
        cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if posicao_y1 < 22:
        velocidade_y1 = 1
        cor1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if posicao_x == posicao_x1 and posicao_y == posicao_y1:
        aux = velocidade_x
        velocidade_x = velocidade_x1
        velocidade_x1 = aux
        auy = velocidade_y
        velocidade_y = velocidade_y1
        velocidade_y1 = auy

    clock.tick(300)
    tela.fill(preto)
    pygame.draw.circle(tela, cor, [posicao_x, posicao_y], 30, 0)
    pygame.draw.circle(tela, cor1, [posicao_x1, posicao_y1], 30, 0)
    pygame.display.flip()

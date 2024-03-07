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

pygame.draw.circle(tela, branco, [320, 320], 30, 0)

clock = pygame.time.Clock()

velocidade_x = random.randint(-1, 1)
velocidade_y = random.randint(-1, 1)

posicao_x = random.randint(0, 800)
posicao_y = random.randint(0, 600)


while velocidade_x == 0:
    velocidade_x = random.randint(-1, 1)
while velocidade_y == 0:
    velocidade_y = random.randint(-1, 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    posicao_x += velocidade_x
    posicao_y += velocidade_y

    if posicao_x > (largura - 22):
        velocidade_x = random.randint(-1, 0)
        velocidade_y = random.randint(-1, 1)
        cor = cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if posicao_x < 22:
        velocidade_x = random.randint(0, 1)
        velocidade_y = random.randint(-1, 1)
        cor = cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if posicao_y > (altura - 22):
        velocidade_y = random.randint(-1, 0)
        velocidade_x = random.randint(-1, 1)
        cor = cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if posicao_y < 22:
        velocidade_y = random.randint(0, 1)
        velocidade_x = random.randint(-1, 1)
        cor = cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    clock.tick(200)
    tela.fill(preto)
    pygame.draw.circle(tela, cor, [posicao_x, posicao_y], 30, 0)
    pygame.draw.circle(tela, cor, [posicao_x, posicao_y], 30, 0)
    pygame.display.flip()

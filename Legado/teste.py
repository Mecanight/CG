import sys
import pygame
import random

pygame.init()

#Configuração da tel
largura=800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pygame")

preto = (0,0,0)
branco = (255,255,255)
vermelho = (255,0,0)
azul = (0,0,255)
verde = (0,255,0)

cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

tamanho_fonte = 50
fonte = pygame.font.SysFont(None, tamanho_fonte)

texto = fonte.render("Cassiano", True, branco)
# texto = pygame.draw.circle(tela, branco, (400, 300), 30)

texto_rect = texto.get_rect(center=(largura/2, altura/2))
# texto_rect = texto.get_rect()
# texto_rect.left = 0
# texto_rect.right = 800
# texto_rect.top = 0
# texto_rect.bottom = 600

clock = pygame.time.Clock()


velocidade_x = random.randint(-1, 1)
velocidade_y = random.randint(-1, 1)

while velocidade_x == 0:
    velocidade_x = random.randint(-1, 1)
while velocidade_y == 0:
    velocidade_y = random.randint(-1, 1)

# velocidade_x = 3
# velocidade_y = 3

#Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    texto_rect.x += velocidade_x
    texto_rect.y += velocidade_y

    if texto_rect.right >= largura:
        velocidade_x = random.randint(-1, 1)
        if texto_rect.right >= largura:
            velocidade_x = -1
        texto = fonte.render("Cassiano", True, vermelho)
        velocidade_y = random.randint(-1, 1)
    if texto_rect.left <= 0:
        velocidade_x = random.randint(-1, 1)
        if texto_rect.left <= 0:
            velocidade_x = 1
        texto = fonte.render("Cassiano", True, azul)
        velocidade_y = random.randint(-1, 1)
    if texto_rect.bottom >= altura:
        velocidade_y = random.randint(-1, 1)
        if texto_rect.top <= 0:
            velocidade_x = 1
        texto = fonte.render("Cassiano", True, verde)
        velocidade_x = random.randint(-1, 1)
    if texto_rect.top <= 0:
        velocidade_y = random.randint(-1, 1)
        if texto_rect.bottom >= altura:
            velocidade_x = 1
        texto = fonte.render("Cassiano", True, branco)
        velocidade_x = random.randint(-1, 1)

    clock.tick(300)
    tela.fill(preto)
    tela.blit(texto, texto_rect)
    pygame.display.flip()

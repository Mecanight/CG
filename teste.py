import sys
import pygame

pygame.init()

#Configuração da tel
largura=800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pygame")

preto = (0,0,0)
branco = (255,255,255)

tamanho_fonte = 50
fonte = pygame.font.SysFont(None, tamanho_fonte)

texto = fonte.render("Cassiano", True, branco)

texto_rect0 = texto.get_rect(center=(78, 25))
texto_rect1 = texto.get_rect(center=(400, 25))
texto_rect2 = texto.get_rect(center=(722, 25))
texto_rect3 = texto.get_rect(center=(78, 300))
texto_rect4 = texto.get_rect(center=(400, 300))
texto_rect5 = texto.get_rect(center=(722, 300))
texto_rect6 = texto.get_rect(center=(78, 575))
texto_rect7 = texto.get_rect(center=(400, 575))
texto_rect8 = texto.get_rect(center=(722, 575))


#Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill(preto)
    tela.blit(texto, texto_rect0)
    tela.blit(texto, texto_rect1)
    tela.blit(texto, texto_rect2)
    tela.blit(texto, texto_rect3)
    tela.blit(texto, texto_rect4)
    tela.blit(texto, texto_rect5)
    tela.blit(texto, texto_rect6)
    tela.blit(texto, texto_rect7)
    tela.blit(texto, texto_rect8)
    pygame.display.flip()
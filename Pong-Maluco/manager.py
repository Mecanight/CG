import pygame
from sets import *
import sys

def main_menu():
    global control
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    control = True
                    return
        # Renderiza o texto do menu
        screen.fill(black)
        menu_text = font.render("Pong", True, white)
        menu_text_rect = menu_text.get_rect(center=(width_screen // 2, height_screen // 2))
        screen.blit(menu_text, menu_text_rect)

        time_steps = pygame.time.get_ticks()
        print(time_steps)
        # Pressione Space para jogar
        if time_steps % 2000 < 1000:
            texto_iniciar = font.render("Pressione Espaço", True, white)
            texto_iniciar_rect = texto_iniciar.get_rect(center=(width_screen // 2, 450))
            screen.blit(texto_iniciar, texto_iniciar_rect)

        clock.tick(1)
        pygame.display.flip()

def fim_jogo(winner):
    global control
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    control = True

                    return
        # Renderiza o texto do menu
        screen.fill(black)
        texto_fim = font.render(f"winner: {winner}", True, white)
        text_fim_rect = texto_fim.get_rect(center=(width_screen // 2, height_screen // 2))
        screen.blit(texto_fim, text_fim_rect)

        pygame.display.flip()
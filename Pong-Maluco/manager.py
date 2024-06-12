# Importação de bibliotecas, métodos e variáveis
import pygame
from sets import *
import sys


# Criação do método main_menu()
def main_menu():
    global control

    # Inicia um loop iterando por cada evento do jogo e executando as ações para cada iteração
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Definir a ação ao pressionar a barra de espaço
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    control = True
                    return

        # Renderiza os efeitos do menuinicial na tela do jogo
        screen.fill(black)
        menu_text = font.render("Pong", True, white)
        menu_text_rect = menu_text.get_rect(
            center=(width_screen // 2, height_screen // 2)
        )
        screen.blit(menu_text, menu_text_rect)
        time_steps = pygame.time.get_ticks()
        print(time_steps)

        # Definir a ação de piscar o letreiro "Pressione Espaço" ao abrir o jogo
        if time_steps % 2000 < 1000:
            texto_iniciar = font.render("Pressione Espaço", True, white)
            texto_iniciar_rect = texto_iniciar.get_rect(center=(width_screen // 2, 450))
            screen.blit(texto_iniciar, texto_iniciar_rect)

        # Definir a taxa de atualização da tela
        clock.tick(1)

        # Atualiza a tela com os efeitos ou desenhos
        pygame.display.flip()


# Criação do método fim_jogo()
def fim_jogo(winner):
    global control

    # Inicia um loop iterando por cada evento do jogo e executando as ações para cada iteração
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Definir a ação ao pressionar a barra de espaço
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    control = True
                    return

        # Renderiza na tela o resultado final (vencedor) do jogo
        screen.fill(black)
        texto_fim = font.render(f"winner: {winner}", True, white)
        text_fim_rect = texto_fim.get_rect(
            center=(width_screen // 2, height_screen // 2)
        )
        screen.blit(texto_fim, text_fim_rect)

        # Atualiza a tela com os efeitos ou desenhos
        pygame.display.flip()

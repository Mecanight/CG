import pygame
from pygame import mixer
import sys

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

width_screen = 800
height_screen = 600

width_screen = 800
height_screen = 600

screen = pygame.display.set_mode((width_screen, height_screen))
pygame.display.set_caption("Pong")

# Definição da Raquete
racket_width = 10
racket_height = 60
ball_size = 10

# Velocidade da raquete
player_racket_speed = 5
pc_racket_speed = 5

# velocidade da bola
x_speed_ball = 3
y_speed_ball = 3

# Definir Winner
winner = ""

# Definir control
control = False
running = True

# Configuração da fonte
font_file = "font/PressStart2P-Regular.ttf"
font = pygame.font.Font(font_file, 36)

mixer.music.load("audios/music_game.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.5)
sound = mixer.Sound("audios/Sound_A.wav")

clock = pygame.time.Clock()


def main_menu():
    global running, control
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


def posicao_inicial():
    global pc_x, pc_y, player_1_x, player_1_y, bola_x, bola_y, score_pc, score_player_1

    # Posição da Raquete do pc
    pc_x = 10
    pc_y = height_screen // 2 - racket_height // 2

    # Posição da Raquete do player
    player_1_x = width_screen - 20
    player_1_y = height_screen // 2 - racket_height // 2

    # Posição da bola
    bola_x = width_screen // 2 - ball_size // 2
    bola_y = height_screen // 2 - ball_size // 2

    # Define o Score
    score_player_1 = 0
    score_pc = 0


def fim_jogo():
    global running, winner, control
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    control = True
                    posicao_inicial()

                    return
        # Renderiza o texto do menu
        screen.fill(black)
        texto_fim = font.render(f"winner: {winner}", True, white)
        text_fim_rect = texto_fim.get_rect(center=(width_screen // 2, height_screen // 2))
        screen.blit(texto_fim, text_fim_rect)

        pygame.display.flip()


main_menu()
posicao_inicial()

while running:
    if not control:
        fim_jogo()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(black)

        # Movendo a bola
        bola_x += x_speed_ball
        bola_y += y_speed_ball

        # Retângulos de Colisão
        bola_rect = pygame.Rect(bola_x, bola_y, ball_size, ball_size)
        raquete_pc_rect = pygame.Rect(pc_x, pc_y, racket_width, racket_height)
        raquete_player_1_rect = pygame.Rect(
            player_1_x, player_1_y, racket_width, racket_height
        )

        # Colisão da bola com a raquete do pc e a raquete do player
        if bola_rect.colliderect(raquete_pc_rect) or bola_rect.colliderect(
            raquete_player_1_rect
        ):
            sound.play()
            x_speed_ball = -x_speed_ball

        # Colisão da bola com as bordas da tela
        if bola_y <= 0 or bola_y >= height_screen - ball_size:
            y_speed_ball = -y_speed_ball

        # Posicionar a bola no inicio do jogo
        if bola_x <= 0:
            bola_x = width_screen // 2 - ball_size // 2
            bola_y = height_screen // 2 - ball_size // 2
            x_speed_ball = -x_speed_ball
            score_player_1 += 1
            print(f"Score Player_1: {score_player_1}")
            if score_player_1 == 5:
                print("Player_1 ganhou!")
                winner = "Player 1"
                fim_jogo()

        if bola_x >= width_screen - ball_size:
            bola_x = width_screen // 2 - ball_size // 2
            bola_y = height_screen // 2 - ball_size // 2
            x_speed_ball = -x_speed_ball
            score_pc += 1
            print(f"Score PC: {score_pc}")
            if score_pc == 5:
                print("PC ganhou!")
                winner = "PC"
                fim_jogo()

        # Movendo a raquete do pc pra seguir a bola
        if pc_y + racket_height // 2 < bola_y:
            pc_y += pc_racket_speed
        elif pc_y + racket_height // 2 > bola_y:
            pc_y -= pc_racket_speed

        # Evitar que a raquete do pc saia da área
        if pc_y < 0:
            pc_y = 0
        elif pc_y > height_screen - racket_height:
            pc_y = height_screen - racket_height

        # Mostrando Score no jogo
        fonte_score = pygame.font.Font(font_file, 16)
        score_texto = fonte_score.render(
            f"Score PC: {score_pc}       Score Player_1: {score_player_1}", True, white
        )
        score_rect = score_texto.get_rect(center=(width_screen // 2, 30))

        screen.blit(score_texto, score_rect)

        # assets (objetos)
        pygame.draw.rect(screen, white, (pc_x, pc_y, racket_width, racket_height))
        pygame.draw.rect(
            screen, white, (player_1_x, player_1_y, racket_width, racket_height)
        )
        pygame.draw.ellipse(
            screen, white, (bola_x, bola_y, ball_size, ball_size)
        )
        pygame.draw.aaline(screen, white, (width_screen // 2, 0), (width_screen // 2, height_screen))

        # control Teclado do Player_1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_1_y > 0:
            player_1_y -= player_racket_speed
        if keys[pygame.K_DOWN] and player_1_y < height_screen - racket_height:
            player_1_y += player_racket_speed

        pygame.display.flip()

        clock.tick(60)

# fim_jogo()
pygame.quit()
sys.exit()

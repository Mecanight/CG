from sets import *
from manager import *


def run():
    running = True
    control = False
    global bola_x, bola_y, x_speed_ball, y_speed_ball, pc_y, pc_x, racket_height, racket_width, player_1_y, score_pc, score_player_1, winner, limit_time
    while running:
        if control:
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
            if (bola_y < 350 and bola_y > 250) and (bola_x < 20 or bola_x > 770):
                x_speed_ball *= 3
                y_speed_ball *= 3

            # Colisão da bola com as bordas da tela
            if bola_y <= 0 or bola_y >= height_screen - ball_size:
                y_speed_ball = -y_speed_ball

            # Posicionar a bola no inicio do jogo
            if bola_x <= 0:
                x_speed_ball = 3
                y_speed_ball = 3
                bola_x = width_screen // 2 - ball_size // 2
                bola_y = random.randint(10, 590)
                x_speed_ball = -x_speed_ball
                score_player_1 += 1
                print(f"Score Player 1: {score_player_1}")

                # Ao final do jogo mostrar em tela o ganhador Player 1
                if score_player_1 == 5:
                    print("Player 1 ganhou!")
                    winner = "Player 1"
                    fim_jogo(winner)

            if bola_x >= width_screen - ball_size:
                x_speed_ball = 3
                y_speed_ball = 3
                bola_x = width_screen // 2 - ball_size // 2
                bola_y = random.randint(10, 590)
                x_speed_ball = -x_speed_ball
                score_pc += 1
                print(f"Score PC: {score_pc}")

                # Ao final do jogo mostrar em tela o ganhador PC
                if score_pc == 5:
                    print("PC ganhou!")
                    winner = "PC"
                    fim_jogo(winner)

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
                f"Score PC: {score_pc}       Score Player 1: {score_player_1}",
                True,
                white,
            )
            score_rect = score_texto.get_rect(center=(width_screen // 2, 30))

            screen.blit(score_texto, score_rect)

            # assets (objetos)
            pygame.draw.rect(screen, white, (pc_x, pc_y, racket_width, racket_height))
            pygame.draw.rect(
                screen, white, (player_1_x, player_1_y, racket_width, racket_height)
            )
            pygame.draw.ellipse(screen, white, (bola_x, bola_y, ball_size, ball_size))
            pygame.draw.aaline(
                screen,
                white,
                (width_screen // 2, 0),
                (width_screen // 2, height_screen),
            )

            # control Teclado do Player_1
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and player_1_y > 0:
                player_1_y -= player_racket_speed
            if keys[pygame.K_DOWN] and player_1_y < height_screen - racket_height:
                player_1_y += player_racket_speed

            pygame.display.flip()

            clock.tick(60)

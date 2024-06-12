
# Importação de bibliotecas, métodos e variáveis
import pygame
from pygame import mixer
import random

# Inicia os módulos necessário para o pymage funcionar
pygame.init()

# Definir as cores utilizadas
black = (0, 0, 0)
white = (255, 255, 255)
ball_color = white

# Definir tamanho da tela do jogo
width_screen = 800
height_screen = 600

# Definir os parâmetros da tela (tamanho, título)
screen = pygame.display.set_mode((width_screen, height_screen))
pygame.display.set_caption("Pong")

# Definir tamanho da Raquete
racket_width = 10
racket_height = 60

# Definir tamanho da bola
ball_size = 10

# Velocidade da raquete
player_racket_speed = 5
pc_racket_speed = 5

# Velocidade da bola
x_speed_ball = 3
y_speed_ball = 3

# Definir Winner
winner = ""

# Definir control
control = False

# Configuração da fonte
font_file = "font/PressStart2P-Regular.ttf"
font = pygame.font.Font(font_file, 36)

# Configuração dos sons utilizados
mixer.music.load("audios/music_game.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.5)
sound = mixer.Sound("audios/Sound_A.wav")

# Variável que é utilizada para definir a frequencia de atualização da tela
clock = pygame.time.Clock()

# Posição da Raquete do pc
pc_x = 10
pc_y = height_screen // 2 - racket_height // 2

# Posição da Raquete do player
player_1_x = width_screen - 20
player_1_y = height_screen // 2 - racket_height // 2

# Posição da bola
bola_x = width_screen // 2 - ball_size // 2
bola_y = random.randint(10, 590)

# Define o Score
score_player_1 = 0
score_pc = 0

# Importação de bibliotecas, métodos e variáveis
import pygame
from sets import *
from manager import main_menu, fim_jogo
import game

# Inicia os módulos necessário para o pymage funcionar
pygame.init()

# executa o método main_menu() do arquivo manager.py
main_menu()

# executa o método run() do arquivo game.py
game.run()
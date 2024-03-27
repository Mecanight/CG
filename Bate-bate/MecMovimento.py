import pygame  # importa a biblioteca pygame
import random  # importa a biblioteca random


class MovendoTexto:  # cria a classe MovendoTexto
    def __init__(
        self, texto, fonte_tamanho, largura, altura
    ):  # cria o método inicial construtor onde são declarados os atributos desta classe
        self.fonte = pygame.font.SysFont(
            None, fonte_tamanho
        )  # define o atributo fonte e atribui valores a ele
        self.texto = texto  # define o atributo texto e atribui um valor a ele
        self.largura = largura  # define o atributo largura e atribui um valor a ele
        self.altura = altura  # define o atributo altura e atribui um valor a ele
        self.texto_surf = self.fonte.render(
            texto, True, (255, 255, 255)
        )  # define o atributo texto_surf e atribui um valor a ele
        self.rect = self.texto_surf.get_rect(
            center=(largura / 2, altura / 2)
        )  # define o atributo rect e atribui um valor a ele

        self.velocidade_x = (
            self.gerar_numero_nao_zero()
        )  # define o atributo velocidade_x e atribui um valor a ele atraves da função gerar_numero_nao_zero
        self.velocidade_y = (
            self.gerar_numero_nao_zero()
        )  # define o atributo velocidade_y e atribui um valor a ele atraves da função gerar_numero_nao_zero

    def gerar_numero_nao_zero(self):  # cria o metodo gerar_numero_nao_zero
        numero = random.randint(
            -1, 1
        )  # define a variavel numero e atribui um valor aleatorio entre -1 e 1 para ela
        return numero  # retorna o valor da variavel numero

    def move(self):  # cria o método move
        self.rect.x += (
            self.velocidade_x
        )  # declara a variavel rect.x com o valor de velocidade_x
        self.rect.y += (
            self.velocidade_y
        )  # declara a variavel rect.y com o valor de velocidade_y

        if self.rect.left < 1:  # condição se a posição left do objeto for menor que 1
            self.velocidade_x = random.randint(
                0, 1
            )  # atribui o valor aleatório en tre 0 e 1 para a velocidade_x
            self.velocidade_y = random.randint(
                -1, 1
            )  # atribui o valor aleatório en tre -1 e 1 para a velocidade_y
            self.change_color()  # inicia o método para mudar a cor do objeto

        if self.rect.right > (
            self.largura - 1
        ):  # condição se a posição do objeto for menor que (largura -1)
            self.velocidade_x = random.randint(
                -1, 0
            )  # atribui o valor aleatório en tre -1 e 0 para a velocidade_x
            self.velocidade_y = random.randint(
                -1, 1
            )  # atribui o valor aleatório en tre -1 e 1 para a velocidade_y
            self.change_color()  # inicia o método para mudar a cor do objeto

        if self.rect.top < 1:  # condição se a posição top do objeto for menor que 1
            self.velocidade_x = random.randint(
                -1, 1
            )  # atribui o valor aleatório en tre -1 e 1 para a velocidade_x
            self.velocidade_y = random.randint(
                0, 1
            )  # atribui o valor aleatório en tre 0 e 1 para a velocidade_y
            self.change_color()  # inicia o método para mudar a cor do objeto

        if self.rect.bottom > (
            self.altura - 1
        ):  # condição se a posição bottom do objeto for menor que (largura - 1)
            self.velocidade_x = random.randint(
                -1, 1
            )  # atribui o valor aleatório en tre -1 e 1 para a velocidade_x
            self.velocidade_y = random.randint(
                -1, 0
            )  # atribui o valor aleatório en tre -1 e 0 para a velocidade_y
            self.change_color()  # inicia o método para mudar a cor do objeto

    def change_color(self):  # cria o método change_color
        cor_texto = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )  # atribui à lista do objeto cor_texto os 03 parametros de cor (RGB) com numeros aleatorios entre 0 e 255
        self.texto_surf = self.fonte.render(
            self.texto, True, cor_texto
        )  # atribui os valores de cor_texto para o atributo fonte do texto

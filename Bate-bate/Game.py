import pygame  # importa a biblioteca pygame
import sys  # importa a biblioteca sys
from MecMovimento import (
    MovendoTexto,
)  # importa a classe MovendoTexto do arquivo MecMovimento


class Game:  # cria a classe Game
    def __init__(
        self,
    ):  # cria o método inicial construtor onde são declarados os atributos desta classe
        pygame.init()  # inicia os módulos necessário para o pymage funcionar
        self.largura = 800  # define o atributo largura com o valor de 800
        self.altura = 600  # define o atributo altura com o valor de 600
        self.tela = pygame.display.set_mode(
            (self.largura, self.altura)
        )  # define o atributo tela com o método display do pygame e com tamanho (largura x altura) que será a tela gerada pelo programa
        pygame.display.set_caption(
            "Bate-Bate"
        )  # define o nome a ser exibido na barra superior da tela como "Bate-Bate"
        self.clock = (
            pygame.time.Clock()
        )  # define o atributo clock com o metodo Clock do pygame.time, utilizado para definir a frequencia de atualização da tela
        self.MovendoTexto = MovendoTexto(
            "Cassiano", 50, self.largura, self.altura
        )  # define o atributo MovendoTexto com a classe MovendoTexto do arquivo MecMovimento e informa valores para os atributos deste

    def run(self):  # cria o método run() desta classe
        rodando = True  # declara a variavel rodando e atribui a ela o valor True
        while (
            rodando
        ):  # inicia um loop while que vai executar enquanto rodando tiver o valor True
            for (
                evento
            ) in (
                pygame.event.get()
            ):  # inicia um loop for que executa a cada evento pygame
                if (
                    evento.type == pygame.QUIT
                ):  # condicao para quando o evento for do tipo pygame.QUIT
                    rodando = False  # atribui o valor False a variavel rodando

            self.MovendoTexto.move()  # executa o método move() da classe MovendoTexto
            self.tela.fill((0, 0, 0))  # preenche a tela com a cor preta
            self.tela.blit(
                self.MovendoTexto.texto_surf, self.MovendoTexto.rect
            )  # desenha/copia para a tela os efeitos/desenhos e o local onde ficarão
            pygame.display.flip()  # atualiza a tela com os efeitos ou desenhos
            self.clock.tick(300)  # define a taxa de atualização da tela para 300

        pygame.quit()  # encerra/fecha a tela gerada pelo programa
        sys.exit()  # encerra o processo de execução (PID) do pygame no sistema operacional

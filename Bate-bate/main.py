from Game import Game # importa a classe Game() do arquivo Game

if __name__ == "__main__": # condição que será verdadeira caso o programa/scrypt for iniciado por este arquivo e falsa caso seja iniciado por outro arquivo
    game = Game() # declara a variável/objeto "game" como instância de Game()
    game.run() # executa o método run() da classe
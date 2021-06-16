import pygame
from classes import Obj
from playing import start_game


# Inicializando o pygame e criando a janela

pygame.init()

Tela = pygame.display.set_mode([1080, 720])
pygame.display.set_caption("PCA Game Sustentabilidade")

# carregando sprites

menu = pygame.image.load("Layout/Telas/fundo_tela_inicial.png")
ButtomStart = pygame.image.load("Layout/botoes/botão1.png")
ButtomExit = pygame.image.load("Layout/botoes/botão2.png")
ButtomCredits = pygame.image.load("Layout/botoes/botão3.png")


# desenhando sprites

Tela.blit(menu, (0, 0))
Tela.blit(ButtomStart, (520, 260))
Tela.blit(ButtomExit, (550, 420))
Tela.blit(ButtomCredits, (550, 550))


# colocando Musica

pygame.mixer.music.load("sons/music.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

# Funcionalidades do jogo

gameLoop = True
ingame = False

while gameLoop:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameLoop = False
# funcionalidade botões do menu

        if event.type == pygame.MOUSEBUTTONDOWN:
            MousePos = pygame.mouse.get_pos()
            print(pygame.mouse.get_pos())

            # ingame
            if 575 <= MousePos[0] <= 949 and 307 <= MousePos[1] <= 407 and not ingame:
                ingame = True
                while ingame:
                    ingame = start_game()
                gameLoop = False

            if 673 <= MousePos[0] <= 843 and 599 <= MousePos[1] <= 669 and not ingame:
                print("Créditos!")

            if 550 < MousePos[0] < (550 + 437) and 420 < MousePos[1] < (420 + 177) and not ingame:
                gameLoop = False

    pygame.display.update()

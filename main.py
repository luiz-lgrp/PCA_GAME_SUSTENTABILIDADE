import pygame
from playing import start_game
from classes import Obj


def main():
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
                    menu = start_game()
                    if menu:
                        main()
                        gameLoop = False
                    else:
                        gameLoop = False

                if 673 <= MousePos[0] <= 843 and 599 <= MousePos[1] <= 669 and not ingame:
                    gameLoop = creditos(Tela)

                if 550 < MousePos[0] < (550 + 437) and 420 < MousePos[1] < (420 + 177) and not ingame:
                    gameLoop = False
                    break

        pygame.display.update()


def creditos(Tela):
    BG_end = Obj("Layout/Telas/creditos.png", 0, 0)
    menu_button = Obj("Layout/botoes/botaomenu.png", 60, 530)

    while True:
        BG_end.draw(Tela)
        menu_button.draw(Tela)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button.rect[0] < pos[0] < (menu_button.rect[0] + menu_button.rect[2]) and menu_button.rect[1] \
                        < pos[1] < (menu_button.rect[1] + menu_button.rect[3]):
                    main()
                    return False

            if event.type == pygame.QUIT:
                return False

        pygame.display.update()


main()

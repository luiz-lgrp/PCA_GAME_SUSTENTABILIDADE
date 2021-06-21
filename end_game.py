import pygame
from classes import Obj

def Game_Over(erros, Tela):
    BG_end = Obj("Layout/tela-final/FundoJogo.png", 0, 0)
    img_erros = pygame.image.load(f'Layout/tela-final/{erros}.png')
    menu_button = Obj("Layout/botoes/botaomenu.png", 60, 560)
    pygame.mixer.music.load("sons/music.wav")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    running = True

    while running:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                return False

            if events.type == pygame.MOUSEBUTTONDOWN:
                Pos = pygame.mouse.get_pos()
                print(Pos)
                if menu_button.rect[0] < Pos[0] < (menu_button.rect[0] + menu_button.rect[2]) and menu_button.rect[1] < Pos[1] < (menu_button.rect[1] + menu_button.rect[3]):
                    print('clicou')
                    return True

        BG_end.draw(Tela)
        Tela.blit(img_erros, (310, 440))
        menu_button.draw(Tela)

        pygame.display.update()

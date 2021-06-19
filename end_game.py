import pygame
from classes import Obj
def Game_Over(erros, Tela):
    BG_end = Obj("Layout/tela-final/FundoJogo.png", 0, 0)
    img_erros = pygame.image.load(f'Layout/tela-final/{erros}.png')
    pygame.mixer.music.load("sons/music.wav")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    
    running = True
    
    while running:
        
        BG_end.draw(Tela)
        Tela.blit(img_erros, (310, 440))

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                return
            
            if events.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
        pygame.display.update()
                

    
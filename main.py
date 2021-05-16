import pygame

#Inicializando o pygame e criando a janela

pygame.init()

Tela = pygame.display.set_mode([1080, 720])
pygame.display.set_caption("PCA Game Sustentabilidade")

#carregando sprites

menu = pygame.image.load("Layout/Telas/fundo_tela_inicial.png")
ButtomStart = pygame.image.load("Layout/botoes/botão1.png")
ButtomExit = pygame.image.load("Layout/botoes/botão2.png")
ButtomCredits = pygame.image.load("Layout/botoes/botão3.png")


#desenhando sprites

Tela.blit(menu, (0, 0))
Tela.blit(ButtomStart, (520, 260))
Tela.blit(ButtomExit, (550, 420))
Tela.blit(ButtomCredits, (550, 550))


#colocando Musica

pygame.mixer.music.load("sons/music.wav")
pygame.mixer.music.play(-1)

#Funcionalidades do jogo

gameLoop = True

while gameLoop:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameLoop = False
#funcionalidade botões do menu

        if event.type == pygame.MOUSEBUTTONDOWN:
            ButtomExit = pygame.mouse.get_pos()
            print(pygame.mouse.get_pos())
            if 550 < ButtomExit[0] < (550 + 437) and 420 < ButtomExit[1] < (420 + 177):
                gameLoop = False



    pygame.display.update()




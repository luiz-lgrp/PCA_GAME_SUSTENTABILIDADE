import pygame

"#Inicializando o pygame e criando a janela"

pygame.init()

Tela = pygame.display.set_mode([1080, 720])
pygame.display.set_caption("PCA Game Sustentabilidade")

"#carregando sprites"
menu = pygame.image.load("assets/test-menu.png")

'#desenhando sprites'
Tela.blit(menu, (0, 0))

'#colocando Musica'
pygame.mixer.music.load("sons/happy.mp3")
pygame.mixer.music.play(-1)

'#Inicializando o pygame e criando a janela'

gameLoop = True

while gameLoop:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameLoop = False
        if event.type == pygame.QUIT:
            gameLoop = False

    pygame.display.update()

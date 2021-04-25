import pygame

#Inicializando o pygame e criando a janela

pygame.init()

Tela = pygame.display.set_mode([1024, 673])
pygame.display.set_caption("PCA Game Sustentabilidade")

#colocando Musica
pygame.mixer.music.load("./sons/music.wav")
pygame.mixer.music.play(-1)

#Inicializando o pygame e criando a janela

gameLoop = True

if __name__ == "__main__":
    while gameLoop:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameLoop = False



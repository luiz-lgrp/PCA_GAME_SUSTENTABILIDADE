import pygame


class Obj:

    def __init__(self, image, posX, posY):
        self.name = str(image)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect[0] = posX
        self.rect[1] = posY

    def draw(self, window):

        window.blit(self.image, (self.rect[0], self.rect[1]))

    def move_obj(self, event):
        self.rect[0] = pygame.mouse.get_pos()[0] - (self.rect[2]/2)
        self.rect[1] = pygame.mouse.get_pos()[1] - (self.rect[3]/2)
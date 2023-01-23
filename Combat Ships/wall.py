import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, img, dimensions, coordinates):
        super().__init__()
        self.image = img
        self.image = pygame.transform.scale(img, dimensions)
        self.rect = self.image.get_rect(topleft=coordinates)

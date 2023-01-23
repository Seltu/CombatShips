import pygame
import config


class AnimationGif(pygame.sprite.Sprite):
    def __init__(self, path, tiles, pos_x, pos_y, w, h):
        super().__init__()
        self.sprites = []

        for i in range(0, tiles):
            image = pygame.image.load(f"{path}{i:03d}.png")
            self.sprites.append(image)

        self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (w, h))

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self, speed, w, h, play_once):
        self.current_sprite += speed

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            if play_once == 1:
                self.kill()

        self.image = self.sprites[int(self.current_sprite)]
        self.image = pygame.transform.scale(self.sprites[int(self.current_sprite)], (w, h))


yipee_sprites = pygame.sprite.Group()
yipee = AnimationGif("Sprites/yipee/tile", 23, config.screen_width / 3, config.screen_height / 3,
                     config.screen_width / 3, config.screen_width / 3)
yipee_sprites.add(yipee)

boom_sprites = pygame.sprite.Group()
boom = AnimationGif("Sprites/Boom/tile", 17, 100, 100,
                    config.screen_width / 6, config.screen_width / 6)
boom_sprites.add(boom)

# def create_explosion(pos_x, pos_y):
# boom_sprites = pygame.sprite.Group()
# boom = AnimationGif("Sprites/Boom/tile", 17, pos_x, pos_y,
#                    config.screen_width / 6, config.screen_width / 6)
# boom_sprites.add(boom)

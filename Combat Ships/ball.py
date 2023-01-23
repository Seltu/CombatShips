import pygame
from config import thud_sound_effect


class Ball(pygame.sprite.Sprite):

    def __init__(self, ball_sprite, tank_x, tank_y, vel_x, vel_y):
        pygame.sprite.Sprite.__init__(self)
        self.x = tank_x
        self.y = tank_y
        self.collided = False
        self.cont = 0
        self.image = ball_sprite
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.group = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]
        self.dx = vel_x
        self.dy = vel_y

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def wall_collision(self, walls):
        for wall in walls:
            if pygame.sprite.collide_mask(self, wall):
                thud_sound_effect.set_volume(0.3)
                thud_sound_effect.play()
                # collision with top side of the wall
                if abs(self.rect.top - wall.rect.bottom) < 10 and self.dy < 0:
                    self.dy *= -1
                    self.rect.top = wall.rect.bottom
                # collision with bottom side of the wall
                elif abs(wall.rect.top - self.rect.bottom) < 10 and self.dy > 0:
                    self.dy *= -1
                    self.rect.bottom = wall.rect.top
                # collision with the left side of the wall
                elif abs(wall.rect.left - self.rect.right) < 10 and self.dx > 0:
                    self.dx *= -1
                # collision with the right side of the wall
                elif abs(self.rect.left - wall.rect.right) < 10 and self.dx < 0:
                    self.dx *= -1
                if not self.collided:
                    self.cont += 1
                    self.collided = True

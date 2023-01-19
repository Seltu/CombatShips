import math

import game
from config import *
from ball import *
import random


class Tank(pygame.sprite.Sprite):
    def __init__(self, sheet, pos_x, pos_y, current_sprite):
        super().__init__()
        self.score = 0
        self.img_tank = []
        self.ball_list = []
        for i in range(4):
            for j in range(4):
                self.img_tank.append(sheet.subsurface((j*48, i*48), (48, 48)))
        self.direction = current_sprite
        self.image = self.img_tank[self.direction]
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.x = pos_x
        self.y = pos_y
        self.rot = 0
        self.moveW = False
        self.shoot = False
        self.hit = False
        self.stop = False
        self.shoot_time = 0

    def shoot_(self):
        self.shoot = True

    def no_move_w(self):
        self.moveW = False

    def move_w(self):
        self.moveW = True

    def no_rot(self):
        self.rot = 0

    def rotate(self, rotation):
        self.rot = rotation

    def update(self):
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        self.ball_update()
        if (self.stop or self.hit) and game.hit_timer <= 0:
            self.stop = False
            self.hit = False
            choice = random.choice(game.coord)
            game.coord.remove(choice)
            self.x = choice[0]
            self.y = choice[1]
        if self.stop:
            return
        self.shoot_time -= 1
        self.direction -= self.rot
        if self.direction < 0:
            self.direction = 15
        if self.direction > 15:
            self.direction = 0
        self.image = self.img_tank[int(self.direction)]
        if self.hit:
            self.direction -= 0.8
            return
        vel_x = math.cos((2-int(self.direction)/8)*math.pi)
        vel_y = -math.sin((2-int(self.direction)/8)*math.pi)
        if self.moveW:
            self.x += vel_x * 2
            self.y += vel_y * 2
        if self.shoot and self.shoot_time <= 0 and len(self.ball_list) <= 2:
            self.shoot = False
            self.shoot_time = shot_time
            ball = Ball(self.rect.x+3+vel_x*15, self.rect.y+5+vel_y*18, vel_x*4, vel_y*4)
            self.ball_list.append(ball)
            game.ball_sprites.add(ball)

    def ball_update(self):
        # update balls in list
        for ball in self.ball_list:
            for i in range(0, ball_speed):
                ball.move()
                ball.wall_collision(game.walls)
            if ball.cont >= ball_bounce:
                self.ball_list.remove(ball)
                game.ball_sprites.remove(ball)


# tank wall collision
def wall_collision(tank):
    for wall in game.walls:
        if pygame.sprite.collide_mask(tank, wall):
            # collision with top side of the wall
            if abs(tank.rect.top - wall.rect.bottom) < 25:
                tank.y += tank_speed
            # collision with bottom side of the wall
            elif abs(wall.rect.top - tank.rect.bottom) < 25:
                tank.y -= tank_speed
            # collision with the left side of the wall
            elif abs(wall.rect.left - tank.rect.right) < 25:
                tank.x -= tank_speed
            # collision with the right side of the wall
            elif abs(tank.rect.left - wall.rect.right) < 25:
                tank.x += tank_speed

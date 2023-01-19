import pygame.sprite
import layouts
from tank import *

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Combat-Atari")

tank_sprites = pygame.sprite.Group()
tank1 = Tank(tank_1, 40, 280, 0)
tank2 = Tank(tank_2, 730, 280, 8)
coord = [[400, 275], [40, 120], [730, 120], [730, 400]]
tank_sprites.add(tank1, tank2)
hit_timer = 0


# ball collision with tank
def ball_collision(tank_one, tank_two):
    if tank_two.stop:
        return
    for ball in tank_two.ball_list:
        if pygame.sprite.collide_mask(ball, tank_one):
            tank_two.ball_list.remove(ball)
            game.ball_sprites.empty()
            game.hit_timer = defeat_time
            game.coord = [[400, 275], [40, 120], [730, 120], [730, 400]]
            tank_one.hit = True
            tank_two.stop = True
            tank_two.score += 1


class Game:
    def __init__(self):
        pass

    # Check if an event happens
    @staticmethod
    def check_events():
        global hit_timer
        clk.tick(60)
        if hit_timer > 0:
            hit_timer -= 1
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    tank1.rotate(rot_speed)
                if event.key == pygame.K_d:
                    tank1.rotate(-rot_speed)
                if event.key == pygame.K_w:
                    tank1.move_w()
                if event.key == pygame.K_e:
                    tank1.shoot_()
                if event.key == pygame.K_k:
                    tank2.shoot_()
                if event.key == pygame.K_LEFT:
                    tank2.rotate(rot_speed)
                if event.key == pygame.K_RIGHT:
                    tank2.rotate(-rot_speed)
                if event.key == pygame.K_UP:
                    tank2.move_w()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    tank1.no_rot()
                if event.key == pygame.K_d:
                    tank1.no_rot()
                if event.key == pygame.K_w:
                    tank1.no_move_w()
                if event.key == pygame.K_LEFT:
                    tank2.no_rot()
                if event.key == pygame.K_RIGHT:
                    tank2.no_rot()
                if event.key == pygame.K_UP:
                    tank2.no_move_w()

    def game_loop(self):

        get_screen(1)

        while True:
            ball_collision(tank1, tank2)
            ball_collision(tank2, tank1)
            wall_collision(tank1)
            wall_collision(tank2)
            self.check_events()
            draw_sprites()
            check_winner(tank1, tank2)

            pygame.display.update()

            clk.tick(fps)


# Select Layout
def get_screen(layout_type):
    global background, walls

    layout = layouts.Layouts(layout_type)
    background = layout.get_bg_color()
    walls = layout.get_group()


# Draws Elements
def draw_sprites():
    global walls, background

    screen.fill(background)
    tank_sprites.draw(screen)
    tank_sprites.update()
    walls.draw(screen)
    ball_sprites.draw(screen)
    ball_sprites.update()


def check_winner(tank_one, tank_two):
    global score_text_1, score_text_2

    if tank_one.score < max_score and tank_two.score < max_score:
        score_text_1 = score_font.render(str(tank_one.score), True, GREEN)
        score_text_2 = score_font.render(str(tank_two.score), True, BLUE)
        screen.blit(score_text_1, score_text_1_rect)
        screen.blit(score_text_2, score_text_2_rect)

    else:
        if hit_timer > 0:
            score_text_1 = score_font.render(str(tank_one.score), True, GREEN)
            score_text_2 = score_font.render(str(tank_two.score), True, BLUE)
            screen.blit(score_text_1, score_text_1_rect)
            screen.blit(score_text_2, score_text_2_rect)
            return
        if tank_two.score < tank_one.score:
            screen.fill(RED)
            score_text_1 = score_font.render(str(tank_one.score), True, GREEN)
            screen.blit(victory_text1, victory_text_rect)
        elif tank_one.score < tank_two.score:
            screen.fill(RED)
            score_text_2 = score_font.render(str(tank_two.score), True, BLUE)
            screen.blit(victory_text2, victory_text_rect)


# score text
score_font = pygame.font.Font('font/Gamer.ttf', 90)
score_text_1 = score_font.render(f'{tank1.score}', True, GREEN)
score_text_2 = score_font.render(f'{tank2.score}', True, BLUE)
score_text_1_rect = (180, -15)
score_text_2_rect = (600, -15)

# victory text
victory_font = pygame.font.Font('font/Gamer.ttf', 100)
victory_text1 = victory_font.render('VICTORY PLAYER 1', True, YELLOW)
victory_text2 = victory_font.render('VICTORY PLAYER 2', True, YELLOW)
victory_text_rect = (110, 210)

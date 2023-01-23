import pygame.sprite
import layouts
import  Animation
from tank import *

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Combat-Atari")

tank_sprites = pygame.sprite.Group()
tank1 = Tank(tank_1, 40, 280, 0, ball_1)
tank2 = Tank(tank_2, 730, 280, 8, ball_2)
arena_index = 0
coord = [[400, 275], [40, 120], [730, 120], [730, 400], [40, 400]]
tank_sprites.add(tank1, tank2)
hit_timer = 0
yipee_can_play = True


# ball collision with tank
def ball_collision(tank_one, tank_two):

    if tank_two.stop:
        return
    for ball in tank_two.ball_list:
        if pygame.sprite.collide_mask(ball, tank_one):
            tank_two.ball_list.remove(ball)
            ball_sprites.empty()
            game.hit_timer = defeat_time
            game.coord = [[400, 275], [40, 120], [730, 120], [730, 400], [40, 400]]
            tank_one.hit = True
            tank_two.stop = True
            tank_two.score += 1
            vine_boom_sound_effect.play()


class Game:
    def __init__(self):
        pass

    # Check if an event happens
    @staticmethod
    def check_events():
        global hit_timer, arena_index
        clk.tick(60)
        if hit_timer > 0:
            hit_timer -= 1
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4:
                    arena_index -= 1
                    get_screen(arena_index)
                if event.key == pygame.K_6:
                    arena_index += 1
                    get_screen(arena_index)
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
    global walls, tank1, tank2, coord
    tank1.reposition()
    tank2.reposition()
    coord = [[400, 275], [40, 120], [730, 120], [730, 400], [40, 400]]
    layout = layouts.Layouts(layout_type)
    walls = layout.get_group()


# Draws Elements
def draw_sprites():
    global walls, background

    screen.blit(background, (0, 0))
    tank_sprites.draw(screen)
    tank_sprites.update()
    walls.draw(screen)
    ball_sprites.draw(screen)
    ball_sprites.update()


def check_winner(tank_one, tank_two):
    global score_text_1, score_text_2, yipee_can_play

    if tank_one.score < max_score and tank_two.score < max_score:
        score_text_1 = score_font.render(str(tank_one.score), True, BLUE)
        score_text_2 = score_font.render(str(tank_two.score), True, RED)
        screen.blit(score_text_1, score_text_1_rect)
        screen.blit(score_text_2, score_text_2_rect)

    else:
        if hit_timer > 0:
            score_text_1 = score_font.render(str(tank_one.score), True, BLUE)
            score_text_2 = score_font.render(str(tank_two.score), True, RED)
            screen.blit(score_text_1, score_text_1_rect)
            screen.blit(score_text_2, score_text_2_rect)
            return

        if tank_two.score < tank_one.score:
            screen.fill(DARKER_GREEN)
            score_text_1 = score_font.render(str(tank_one.score), True, GREEN)
            screen.blit(victory_text1, victory_text_rect)
            Animation.yipee_sprites.draw(screen)
            Animation.yipee_sprites.update(0.6, screen_width / 3, screen_width / 3, 0)
            if yipee_can_play:
                yippeee_sound_effect.play(-1)
            yipee_can_play = False

        elif tank_one.score < tank_two.score:
            screen.fill(DARKER_BLUE)
            score_text_2 = score_font.render(str(tank_two.score), True, BLUE)
            screen.blit(victory_text2, victory_text_rect)
            Animation.yipee_sprites.draw(screen)
            Animation.yipee_sprites.update(0.6, screen_width / 3, screen_width / 3, 0)
            if yipee_can_play:
                yippeee_sound_effect.play(-1)
            yipee_can_play = False


# score text
score_font = pygame.font.Font('font/Gamer.ttf', 90)
score_text_1 = score_font.render(f'{tank1.score}', True, GREEN)
score_text_2 = score_font.render(f'{tank2.score}', True, BLUE)
score_text_1_rect = (screen_width / 4, -15)
score_text_2_rect = (screen_width - screen_width / 4, -15)

# victory text
victory_font = pygame.font.Font('font/Gamer.ttf', 100)
victory_text1 = victory_font.render('VICTORY PLAYER 1', True, GREEN)
victory_text2 = victory_font.render('VICTORY PLAYER 2', True, BLUE)
victory_text_rect = (screen_width / 9, screen_height / 10)

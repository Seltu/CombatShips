import pygame

pygame.font.init()
pygame.mixer.init()

# Screen
score_height = 50
wall_width = 25
screen_width = 800
screen_height = 550

# Colors
RED = (134, 28, 9)
YELLOW = (212, 169, 65)
WHITE = (255, 255, 255)
GREEN = (0, 127, 33)
BLUE = (0, 97, 148)
DARKER_GREEN = (31, 61, 12)
DARKER_BLUE = (11, 11, 69)

# Rectangles constant
RECT_1 = (25, 25)

# Screen refresh
fps = 60

# Wall group
walls = pygame.sprite.Group()
ball_sprites = pygame.sprite.Group()

TAM_TANK = 32

# Clock
clk = pygame.time.Clock()

# Game
defeat_time = 50
max_score = 3

# Tanks
tank_1 = pygame.image.load("Sprites/Tank_1.png")
tank_2 = pygame.image.load("Sprites/Tank_2.png")
ball_1 = pygame.image.load("Sprites/Ball_1.png")
ball_2 = pygame.image.load("Sprites/Ball_2.png")
img_border = pygame.image.load("Sprites/rectangle.png")
wall_sheet = pygame.image.load("Sprites/tiles.png")
background = pygame.transform.scale(pygame.image.load("Sprites/background.png"), (screen_width, screen_height))
rot_speed = 0.4
tank_speed = 3
ball_speed = 3
ball_bounce = 5

shot_time = 10

# Sounds
yippeee_sound_effect = pygame.mixer.Sound("Sounds/Yippeee.wav")
vine_boom_sound_effect = pygame.mixer.Sound("Sounds/VineBoom.wav")
delta_boom_sound_effect = pygame.mixer.Sound("Sounds/DeltaruneBoom.wav")
thud_sound_effect = pygame.mixer.Sound("Sounds/Thud.wav")
shot_sound_effect = pygame.mixer.Sound("Sounds/Shot.wav")

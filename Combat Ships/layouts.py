import os
import random

import wall
from config import *


class Layouts:
    layouts = []

    def __init__(self, layout_type: int):
        self.group = pygame.sprite.Group()
        self.get_screen()
        self.wall_tiles = []
        for i in range(3):
            for j in range(3):
                self.wall_tiles.append(wall_sheet.subsurface((j*96, i*96), (96, 96)))
        self.bg_color = "#8CB7C0"
        self.rectangle()

        for layout in self.layouts[layout_type]:
            self.group.add(wall.Wall(self.wall_tiles[4], layout[0], layout[1]))

    def get_group(self):
        return self.group

    def get_bg_color(self):
        return self.bg_color

    def rectangle(self):
        self.group.add(wall.Wall(img_border, (screen_width, wall_width), (0, score_height)))
        self.group.add(wall.Wall(img_border, (screen_width, wall_width), (0, screen_height - wall_width)))
        self.group.add(wall.Wall(img_border, (wall_width, screen_height - 100), (0, score_height + wall_width)))
        self.group.add(wall.Wall(img_border, (wall_width, screen_height - 100), (screen_width - wall_width, score_height + wall_width)))

    def get_screen(self):
        i = 0
        while os.path.isfile('arena'+str(i)+'.txt'):
            layout_temp = []
            with open('arena'+str(i)+'.txt') as f:
                lines = f.readlines()
            for line in range(len(lines)):
                for char in range(len(lines[line])):
                    if lines[line][char] == '1':
                        layout_temp.append([RECT_1, (wall_width+char*RECT_1[0], wall_width+score_height+line*RECT_1[1])])
            i += 1
            self.layouts.append(layout_temp)

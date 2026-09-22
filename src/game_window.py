import pygame
import colorsys
from config import RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_LENGTH
import math
import random
from player import Player
from utils import sin, cos

class GameWindow:
    def __init__(self):
        # Every scene starts with no next scene queued up
        self.next_scene = False

        self.color = 0
        self.color1 = colorsys.hsv_to_rgb(.77 - self.color, .79, 117)
        self.color2 = colorsys.hsv_to_rgb(.77 - self.color, .8, 64)
        self.color3 = colorsys.hsv_to_rgb(.77 - self.color, .26, 240)
        self.color4 = (242, 198, 19)

        self.font = pygame.font.Font(None, 50, )
        self.degree_point = random.randint(50, 360)

        self.circle_x = 500 + RADIUS * cos(self.degree_point)
        self.circle_y = 350 + RADIUS * sin(self.degree_point)

        self.player = Player()

        self.point_hitbox = pygame.Rect(0, 0, 60, 60)
        self.point_hitbox.center = (int(500 + RADIUS * cos(self.degree_point)),int(350 + RADIUS * sin(self.degree_point)))

    def handle_events(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.player.check_collision(self.point_hitbox):

                    self.player.update_speed()
                    self.player.update_score()
                    self.player.update_direction()

                    degrees = self.player.get_degrees()

                    self.degree_point = GameWindow.random_point(int(degrees))
                    self.circle_x = 500 + RADIUS * cos(self.degree_point)
                    self.circle_y = 350 + RADIUS * sin(self.degree_point)

                    self.point_hitbox.center = (int(500 + RADIUS * cos(self.degree_point)),
                                                int(350 + RADIUS * sin(self.degree_point)))

                    self.color += 0.009

                    self.color1 = colorsys.hsv_to_rgb(.77 - self.color, .79, 117)
                    self.color2 = colorsys.hsv_to_rgb(.77 - self.color, .8, 64)
                    self.color3 = colorsys.hsv_to_rgb(.77 - self.color, .26, 240)

                else:
                    score = self.player.get_score()
                    self.next_scene = ["END", (self.color1, self.color2, self.color3, score)]

    def update(self):
        self.player.update()

    def draw(self, screen):

        score = self.player.get_score()
        text=self.font.render(f"Score: {score}", False, self.color3)
        text_rect = text.get_rect(center=(500, 700))
        screen.fill(self.color1)

        screen.blit(text, text_rect)

        pygame.draw.circle(screen, self.color2, (500, 350), 275)
        pygame.draw.circle(screen, self.color1, (500, 350), 175)

        self.player.draw(screen)

        pygame.draw.circle(screen, self.color4, (self.circle_x, self.circle_y), 30)

    def get_next_scene(self):
        return self.next_scene

    @staticmethod
    def random_point(degrees):
        if degrees-50 <= 0:
            lowerbound = 50
            upperbound = 360
            return random.randint(lowerbound, upperbound)
        elif degrees+50 >= 360:
            lowerbound = 0
            upperbound = 360-50
            return random.randint(lowerbound, upperbound)
        else:
            lowerbound1 = 0
            upperbound1 = degrees-50
            lowerbound2 = degrees+50
            upperbound2 = 360
            choice = random.randint(0, 1)
            if choice == 0:
                return random.randint(lowerbound1, upperbound1)
            else:
                return random.randint(lowerbound2, upperbound2)



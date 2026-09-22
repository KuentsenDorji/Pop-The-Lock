import pygame
import random
from config import RADIUS, POINT_RADIUS, SCREEN_CENTER_X, SCREEN_CENTER_Y, POINT_HITBOX_LENGTH
from utils import sin, cos

class Point:
    def __init__(self):
        self.degrees = random.randint(50, 360)

        self.circle_x = SCREEN_CENTER_X + RADIUS * cos( self.degrees)
        self.circle_y = SCREEN_CENTER_Y + RADIUS * sin( self.degrees)

        self.point_hitbox = pygame.Rect(0, 0, POINT_HITBOX_LENGTH, POINT_HITBOX_LENGTH)
        self.point_hitbox.center = (int(SCREEN_CENTER_X + RADIUS * cos(self.degrees)),
                                    int(SCREEN_CENTER_Y + RADIUS * sin(self.degrees)))

    def update(self):
        self.circle_x = SCREEN_CENTER_X + RADIUS * cos(self.degrees)
        self.circle_y = SCREEN_CENTER_Y + RADIUS * sin(self.degrees)

        self.point_hitbox.center = (int(SCREEN_CENTER_X + RADIUS * cos(self.degrees)),
                                    int(SCREEN_CENTER_Y + RADIUS * sin(self.degrees)))

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (self.circle_x, self.circle_y), POINT_RADIUS)

    def set_random_degrees(self, current_degrees, buffer=50):
        self.degrees = (current_degrees + random.randint(buffer, 360 - buffer)) % 360



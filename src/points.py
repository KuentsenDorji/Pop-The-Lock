import pygame
import random
from config import RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT, POINT_RADIUS
from utils import sin, cos

class Point:
    def __init__(self):
        self.degrees = random.randint(50, 360)

        self.circle_x = SCREEN_WIDTH//2 + RADIUS * cos( self.degrees)
        self.circle_y = SCREEN_HEIGHT//2-50 + RADIUS * sin( self.degrees)

        self.point_hitbox = pygame.Rect(0, 0, 60, 60)
        self.point_hitbox.center = (int(SCREEN_WIDTH//2 + RADIUS * cos(self.degrees)),
                                    int(SCREEN_HEIGHT//2-50 + RADIUS * sin(self.degrees)))

    def update(self):
        self.circle_x = SCREEN_WIDTH//2 + RADIUS * cos(self.degrees)
        self.circle_y = SCREEN_HEIGHT//2-50 + RADIUS * sin(self.degrees)

        self.point_hitbox.center = (int(SCREEN_WIDTH//2 + RADIUS * cos(self.degrees)),
                                    int(SCREEN_HEIGHT//2-50 + RADIUS * sin(self.degrees)))

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (self.circle_x, self.circle_y), POINT_RADIUS)

    def get_degrees(self):
        return self.degrees

    def get_point_hitbox(self):
        return self.point_hitbox

    def set_random_degrees(self, degrees):
        if degrees-50 <= 0:
            lowerbound = 50
            upperbound = 360
            self.degrees = random.randint(lowerbound, upperbound)
        elif degrees+50 >= 360:
            lowerbound = 0
            upperbound = 360-50
            self.degrees = random.randint(lowerbound, upperbound)
        else:
            lowerbound1 = 0
            upperbound1 = degrees-50
            lowerbound2 = degrees+50
            upperbound2 = 360
            choice = random.randint(0, 1)
            if choice == 0:
                self.degrees = random.randint(lowerbound1, upperbound1)
            else:
                self.degrees = random.randint(lowerbound2, upperbound2)



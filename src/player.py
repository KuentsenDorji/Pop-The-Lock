import pygame
from config import SPEED, DIR, PLAYER_RADIUS, RADIUS, PLAYER_LENGTH, SCREEN_WIDTH, SCREEN_HEIGHT
from utils import sin, cos

class Player:
    def __init__(self):
        self.direction = DIR
        self.speed = SPEED
        self.degrees = 0
        self.score = 0

        self.line_x1 = SCREEN_WIDTH//2 + PLAYER_RADIUS * cos(self.degrees)
        self.line_y1 = SCREEN_HEIGHT//2-50 + PLAYER_RADIUS * sin(self.degrees)
        self.line_x2 = self.line_x1 + (PLAYER_LENGTH * cos(self.degrees))
        self.line_y2 = self.line_y1 + (PLAYER_LENGTH * sin(self.degrees))

        self.player_hitbox = pygame.Rect(0, 0, 45, 45)
        self.player_hitbox.center = (int(SCREEN_WIDTH//2 + RADIUS * cos(self.degrees)),
                                     int(SCREEN_HEIGHT//2-50 + RADIUS *   sin(self.degrees)))

    def update(self):
        self.degrees = ((self.direction * self.speed) + self.degrees) % 360

        self.line_x1 = SCREEN_WIDTH//2 + PLAYER_RADIUS * cos(self.degrees)
        self.line_y1 = SCREEN_HEIGHT//2-50 + PLAYER_RADIUS * sin(self.degrees)
        self.line_x2 = self.line_x1 + (PLAYER_LENGTH * cos(self.degrees))
        self.line_y2 = self.line_y1 + (PLAYER_LENGTH * sin(self.degrees))

        self.player_hitbox.center = (int(SCREEN_WIDTH//2 + RADIUS * cos(self.degrees)),
                                     int(SCREEN_HEIGHT//2-50 + RADIUS * sin(self.degrees)))

    def draw(self, screen):

        color5 = (227, 18, 81)
        pygame.draw.line(screen, color5, (self.line_x1, self.line_y1), (self.line_x2, self.line_y2), 15)

    def check_collision(self, point_hitbox):
        if pygame.Rect.colliderect(self.player_hitbox, point_hitbox):
            return True
        return False

    def update_speed(self):
        if self.speed < 12:
            self.speed += 0.2
        else:
            pass

    def update_score(self):
        self.score += 1

    def update_direction(self):
        self.direction *= -1

    def get_score(self):
        return self.score

    def get_degrees(self):
        return self.degrees

    def get_direction(self):
        return self.direction


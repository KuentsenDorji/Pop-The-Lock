import pygame
from config import SPEED, DIR, PLAYER_RADIUS, RADIUS, PLAYER_LENGTH, SCREEN_CENTER_X, SCREEN_CENTER_Y, PLAYER_COLOR, PLAYER_HITBOX_LENGTH, PLAYER_WIDTH
from utils import sin, cos

class Player:
    def __init__(self):
        self.direction = DIR
        self.speed = SPEED
        self.degrees = 0
        self.score = 0

        self.line_x1 = SCREEN_CENTER_X + PLAYER_RADIUS * cos(self.degrees)
        self.line_y1 = SCREEN_CENTER_Y + PLAYER_RADIUS * sin(self.degrees)
        self.line_x2 = self.line_x1 + (PLAYER_LENGTH * cos(self.degrees))
        self.line_y2 = self.line_y1 + (PLAYER_LENGTH * sin(self.degrees))

        self.player_hitbox = pygame.Rect(0, 0, PLAYER_HITBOX_LENGTH, PLAYER_HITBOX_LENGTH)
        self.player_hitbox.center = (int(SCREEN_CENTER_X + RADIUS * cos(self.degrees)),
                                     int(SCREEN_CENTER_Y + RADIUS *   sin(self.degrees)))

    def update(self):
        self.degrees = ((self.direction * self.speed) + self.degrees) % 360

        self.line_x1 = SCREEN_CENTER_X + PLAYER_RADIUS * cos(self.degrees)
        self.line_y1 = SCREEN_CENTER_Y + PLAYER_RADIUS * sin(self.degrees)
        self.line_x2 = self.line_x1 + (PLAYER_LENGTH * cos(self.degrees))
        self.line_y2 = self.line_y1 + (PLAYER_LENGTH * sin(self.degrees))

        self.player_hitbox.center = (int(SCREEN_CENTER_X + RADIUS * cos(self.degrees)),
                                     int(SCREEN_CENTER_Y + RADIUS * sin(self.degrees)))

    def draw(self, screen):

        pygame.draw.line(screen, PLAYER_COLOR, (self.line_x1, self.line_y1), (self.line_x2, self.line_y2), PLAYER_WIDTH)

    def check_collision(self, point_hitbox):
        if pygame.Rect.colliderect(self.player_hitbox, point_hitbox):
            return True
        return False

    def score_point(self):
        self.score += 1
        self.direction *= -1
        self.update_speed()

    def update_speed(self):
        if self.speed < 10:
            self.speed += 0.1
        else:
            pass



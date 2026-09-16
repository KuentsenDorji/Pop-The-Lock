import pygame
import colorsys
from config import RADIUS
import math

class GameWindow:
    def __init__(self):
        # Every scene starts with no next scene queued up
        self.next_scene = False
        self.color1 = colorsys.hsv_to_rgb(.77, .79, 117)
        self.color2 = colorsys.hsv_to_rgb(.77, .8, 64)
        self.color3 = colorsys.hsv_to_rgb(.77, .26, 240)
        self.color4 = (242, 198, 19)
        self.font = pygame.font.Font(None, 50, )
        self.score = 0
        self.degrees = 0
        self.circle_x = 500 + RADIUS * GameWindow.cos(90)
        self.circle_y = 350 + RADIUS * GameWindow.sin(90)
        self.speed = 3
        self.direction = 1

    def handle_events(self, event):
        # Look for mouse clicks, key presses, etc.
        pass

    def update(self):
        # Calculate game math, timers, and collisions
        self.degrees = ((self.direction * self.speed) + self.degrees) % 360
        self.circle_x = 500 + RADIUS * GameWindow.cos(self.degrees)
        self.circle_y = 350 + RADIUS * GameWindow.sin(self.degrees)

    def draw(self, screen):
        # Draw everything onto the canvas
        text=self.font.render(f"Score: {self.score}", False, self.color3)
        text_rect = text.get_rect(center=(500, 700))
        screen.fill(self.color1)
        screen.blit(text, text_rect)
        pygame.draw.circle(screen, self.color2, (500, 350), 275)
        pygame.draw.circle(screen, self.color1, (500, 350), 175)
        pygame.draw.circle(screen, self.color4, (self.circle_x, self.circle_y), 30)

    def get_next_scene(self):
        return self.next_scene

    @staticmethod
    def sin(degrees):
        return math.sin(math.radians(degrees))

    @staticmethod
    def cos(degrees):
        return math.cos(math.radians(degrees))
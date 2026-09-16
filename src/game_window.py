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
        self.circle_x = 500 + RADIUS * GameWindow.cos(self.degrees)
        self.circle_y = 350 + RADIUS * GameWindow.sin(self.degrees)
        self.speed = 3
        self.direction = 1
        self.line_x1 = 500 + (1 * GameWindow.cos(self.degrees))
        self.line_y1 = 350 + (1 * GameWindow.sin(self.degrees))
        self.line_x2 = self.line_x1 + (75 * GameWindow.cos(self.degrees))
        self.line_y2 = self.line_y1 + (75 * GameWindow.sin(self.degrees))

    def handle_events(self, event):
        # Look for mouse clicks, key presses, etc.
        pass

    def update(self):
        # Calculate game math, timers, and collisions
        self.degrees = ((self.direction * self.speed) + self.degrees) % 360
        self.line_x1 = 500 + (190 * GameWindow.cos(self.degrees))
        self.line_y1 = 350 + (190 * GameWindow.sin(self.degrees))
        self.line_x2 = self.line_x1 + (70 * GameWindow.cos(self.degrees))
        self.line_y2 = self.line_y1 + (70 * GameWindow.sin(self.degrees))
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
        pygame.draw.line(screen, (227, 18, 81), (self.line_x1, self.line_y1), (self.line_x2, self.line_y2), 15)
        pygame.draw.circle(screen, self.color4, (self.circle_x, self.circle_y), 30)

    def get_next_scene(self):
        return self.next_scene

    @staticmethod
    def sin(degrees):
        return math.sin(math.radians(degrees))

    @staticmethod
    def cos(degrees):
        return math.cos(math.radians(degrees))

    @staticmethod
    def draw_ellipse_angle(surface, color, rect, angle, width=0):
        target_rect = pygame.Rect(rect)
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
        rotated_surf = pygame.transform.rotate(shape_surf, angle)
        surface.blit(rotated_surf, rotated_surf.get_rect(center=target_rect.center))
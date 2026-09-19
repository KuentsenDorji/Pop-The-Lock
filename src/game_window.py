import pygame
import colorsys
from config import RADIUS
import math
import random

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
        self.degree_point = random.randint(50, 360)
        self.circle_x = 500 + RADIUS * GameWindow.cos(self.degree_point)
        self.circle_y = 350 + RADIUS * GameWindow.sin(self.degree_point)
        self.speed = 3
        self.direction = 1
        self.line_x1 = 500 + (1 * GameWindow.cos(self.degrees))
        self.line_y1 = 350 + (1 * GameWindow.sin(self.degrees))
        self.line_x2 = self.line_x1 + (75 * GameWindow.cos(self.degrees))
        self.line_y2 = self.line_y1 + (75 * GameWindow.sin(self.degrees))
        self.direction = 1

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.check_collision():
                    self.direction *= -1
                    self.speed += 0.2
                    self.degree_point = GameWindow.random_point(int(self.degrees))
                    self.circle_x = 500 + RADIUS * GameWindow.cos(self.degree_point)
                    self.circle_y = 350 + RADIUS * GameWindow.sin(self.degree_point)
                    self.score += 1
                else:
                    from welcome_window import WelcomeWindow
                    self.next_scene = WelcomeWindow()

    def update(self):
        # Calculate game math, timers, and collisions
        self.degrees = ((self.direction * self.speed) + self.degrees) % 360
        self.line_x1 = 500 + (190 * GameWindow.cos(self.degrees))
        self.line_y1 = 350 + (190 * GameWindow.sin(self.degrees))
        self.line_x2 = self.line_x1 + (70 * GameWindow.cos(self.degrees))
        self.line_y2 = self.line_y1 + (70 * GameWindow.sin(self.degrees))

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

    def check_collision(self):
        if abs(self.degree_point-self.degrees) < 15:
            return True
        return False

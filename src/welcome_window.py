import pygame
from config import RADIUS_OUTER, RADIUS_INNER, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_CENTER_X, SCREEN_CENTER_Y, COLOR1, COLOR2, COLOR3
from utils import get_hsv_color

class WelcomeWindow:

    def __init__(self):
        self.next_scene = None

        self.color1 = get_hsv_color(*COLOR1)
        self.color2 = get_hsv_color(*COLOR2)
        self.color3 = get_hsv_color(*COLOR3)

        self.font = pygame.font.Font(None, 50, )

        self.text=self.font.render("Click Space to Begin", False, self.color3)
        self.text_rect = self.text.get_rect(center=(SCREEN_CENTER_X, SCREEN_HEIGHT-100))

        self.circle_center = (SCREEN_CENTER_X, SCREEN_CENTER_Y)

    def handle_events(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.next_scene = ["GAME"]

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(self.color1)

        pygame.draw.circle(screen, self.color2, self.circle_center, RADIUS_OUTER)
        pygame.draw.circle(screen, self.color1, self.circle_center, RADIUS_INNER)

        screen.blit(self.text, self.text_rect)


    def get_next_scene(self):
        return self.next_scene
import pygame
import colorsys
from config import RADIUS_OUTER, RADIUS_INNER, SCREEN_WIDTH, SCREEN_HEIGHT

class WelcomeWindow:

    def __init__(self):
        self.next_scene = False

        self.color1 = colorsys.hsv_to_rgb(.77, .79, 117)
        self.color2 = colorsys.hsv_to_rgb(.77, .8, 64)
        self.color3 = colorsys.hsv_to_rgb(.77, .26, 240)

        self.font = pygame.font.Font(None, 50, )

        self.text=self.font.render("Click Space to Begin", False, self.color3)
        self.text_rect = self.text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT-100))

        self.circle_center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2-50)

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
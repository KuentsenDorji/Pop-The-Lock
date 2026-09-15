import pygame
from game_window import GameWindow
import colorsys


class WelcomeWindow:

    def __init__(self):
        self.next_scene = False
        self.color1 = colorsys.hsv_to_rgb(.77, .79, 117)
        self.color2 = colorsys.hsv_to_rgb(.77, .8, 64)
        self.color3 = colorsys.hsv_to_rgb(.77, .26, 240)
        self.font = pygame.font.Font(None, 50, )

    def handle_events(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.next_scene = GameWindow()

    def update(self):
        pass

    def draw(self, screen):
        text=self.font.render("Click Space to Begin", False, self.color3)
        text_rect = text.get_rect(center=(500, 700))
        screen.fill(self.color1)
        screen.blit(text, text_rect)
        pygame.draw.circle(screen, self.color2, (500, 350), 275)
        pygame.draw.circle(screen, self.color1, (500, 350), 175)


    def get_next_scene(self):
        return self.next_scene
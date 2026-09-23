import pygame
from config import RADIUS_OUTER, RADIUS_INNER, SCREEN_CENTER_X, SCREEN_CENTER_Y, COLOR1, COLOR2, COLOR3, TEXT_Y
from utils import get_hsv_color

class WelcomeWindow:

    def __init__(self, face_tracker):
        self.next_scene = None

        self.color1 = get_hsv_color(*COLOR1)
        self.color2 = get_hsv_color(*COLOR2)
        self.color3 = get_hsv_color(*COLOR3)

        self.font = pygame.font.Font(None, 50, )
        self.text_value = "Waiting on the Camera"

        self.text=self.font.render(self.text_value, False, self.color3)
        self.text_rect = self.text.get_rect(center=(SCREEN_CENTER_X, TEXT_Y))

        self.circle_center = (SCREEN_CENTER_X, SCREEN_CENTER_Y)

        self.face_tracker = face_tracker

    def handle_events(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.face_tracker.is_ready():
                self.next_scene = ["GAME", [self.face_tracker]]

    def update(self):
        pass

        if self.face_tracker.is_ready():
            self.text_value = "Click Space to Begin!"
            self.text = self.font.render(self.text_value, False, self.color3)

    def draw(self, screen):
        screen.fill(self.color1)

        pygame.draw.circle(screen, self.color2, self.circle_center, RADIUS_OUTER)
        pygame.draw.circle(screen, self.color1, self.circle_center, RADIUS_INNER)

        self.face_tracker.draw(screen)

        screen.blit(self.text, self.text_rect)


    def get_next_scene(self):
        return self.next_scene

    def handle_camera(self):
        pass
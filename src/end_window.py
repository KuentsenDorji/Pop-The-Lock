import pygame
from config import SCREEN_CENTER_X, SCREEN_CENTER_Y, TEXT_Y

class EndWindow:

    def __init__(self, color1, color2, color3, score, face_tracker):
        self.next_scene = None
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.score = score
        self.face_tracker = face_tracker
        self.font = pygame.font.Font(None, 50, )
        self.font2 = pygame.font.Font(None, 80, )
        self.text_begin = self.font.render(f"Score: {self.score}", False, self.color3)
        self.text_begin_rect = self.text_begin.get_rect(center=(SCREEN_CENTER_X, TEXT_Y))
        self.text_go = self.font2.render("GAME OVER", False, self.color3)
        self.text_go_rect = self.text_go.get_rect(center=(SCREEN_CENTER_X, SCREEN_CENTER_Y))
        self.text_again = self.font.render("Press Space to Play Again", False, self.color3)
        self.text_again_rect = self.text_again.get_rect(center=(SCREEN_CENTER_X, SCREEN_CENTER_Y+100))

    def handle_events(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.next_scene = ["GAME", [self.face_tracker]]

    def update(self):
        pass

    def draw(self, screen):

        screen.fill(self.color1)
        screen.blit(self.text_begin, self.text_begin_rect)
        screen.blit(self.text_go, self.text_go_rect)
        screen.blit(self.text_again, self.text_again_rect)

        self.face_tracker.draw(screen)


    def get_next_scene(self):
        return self.next_scene

    def handle_camera(self):
        pass
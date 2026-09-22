import pygame
import colorsys
from config import SCREEN_HEIGHT, SCREEN_WIDTH, RADIUS_OUTER, RADIUS_INNER
from player import Player
from points import Point
from utils import get_hsv_color

class GameWindow:
    def __init__(self):
        # Every scene starts with no next scene queued up
        self.next_scene = False

        self.color = 0
        self.color1 = get_hsv_color(.77 - self.color, .79, 117)
        self.color2 = get_hsv_color(.77 - self.color, .8, 64)
        self.color3 = get_hsv_color(.77 - self.color, .26, 240)
        self.color4 = (242, 198, 19)

        self.font = pygame.font.Font(None, 50, )
        self.text=self.font.render(f"Score: {0}", False, self.color3)
        self.text_rect = self.text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT-100))

        self.player = Player()
        self.point = Point()

        self.center_circle_pos = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2-50)


    def handle_events(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.player.check_collision(self.point.get_point_hitbox()):

                    self.player.update_speed()
                    self.player.update_score()
                    self.player.update_direction()

                    degrees = self.player.get_degrees()

                    self.point.set_random_degrees(int(degrees))
                    self.point.update()

                    self.color += 0.009

                    self.color1 = get_hsv_color(.77 - self.color, .79, 117)
                    self.color2 = get_hsv_color(.77 - self.color, .8, 64)
                    self.color3 = get_hsv_color(.77 - self.color, .26, 240)

                    score = self.player.get_score()
                    self.text = self.font.render(f"Score: {score}", False, self.color3)

                else:
                    score = self.player.get_score()
                    self.next_scene = ["END", (self.color1, self.color2, self.color3, score)]

    def update(self):
        self.player.update()

    def draw(self, screen):

        screen.fill(self.color1)

        screen.blit(self.text, self.text_rect)

        pygame.draw.circle(screen, self.color2, self.center_circle_pos, RADIUS_OUTER)
        pygame.draw.circle(screen, self.color1, self.center_circle_pos, RADIUS_INNER)

        self.player.draw(screen)

        self.point.draw(screen, self.color4)

    def get_next_scene(self):
        return self.next_scene




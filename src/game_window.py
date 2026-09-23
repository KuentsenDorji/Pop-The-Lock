import pygame
from config import SCREEN_HEIGHT, SCREEN_WIDTH, RADIUS_OUTER, RADIUS_INNER, SCREEN_CENTER_X, SCREEN_CENTER_Y, COLOR1, COLOR2, COLOR3, COLOR4, COLOR_CHANGE, TEXT_Y
from player import Player
from points import Point
from utils import get_hsv_color

class GameWindow:
    def __init__(self, face_tracker):
        # Every scene starts with no next scene queued up
        self.next_scene = None

        self.hue = COLOR1[0]
        self.update_colors()

        self.font = pygame.font.Font(None, 50)
        self.text = self.font.render(f"Score: {0}",False, self.color3)
        self.text_rect = self.text.get_rect(center=(SCREEN_CENTER_X, TEXT_Y))

        self.player = Player()
        self.point = Point()

        self.center_circle_pos = (SCREEN_CENTER_X, SCREEN_CENTER_Y)
        self.face_tracker = face_tracker


    def handle_events(self, event):
        pass

    def update(self):
        self.player.update()
        self.face_tracker.update()

    def draw(self, screen):

        screen.fill(self.color1)

        screen.blit(self.text, self.text_rect)

        pygame.draw.circle(screen, self.color2, self.center_circle_pos, RADIUS_OUTER)
        pygame.draw.circle(screen, self.color1, self.center_circle_pos, RADIUS_INNER)

        self.player.draw(screen)

        self.point.draw(screen, COLOR4)

        self.face_tracker.draw(screen)

    def get_next_scene(self):
        return self.next_scene

    def update_colors(self):
        self.color1 = get_hsv_color(self.hue, COLOR1[1], COLOR1[2])
        self.color2 = get_hsv_color(self.hue, COLOR2[1], COLOR2[2])
        self.color3 = get_hsv_color(self.hue, COLOR3[1], COLOR3[2])

    def handle_camera(self):
        if self.face_tracker.win_con():

            if self.player.check_collision(self.point.point_hitbox):

                self.player.score_point()

                degrees = self.player.degrees

                self.point.set_random_degrees(int(degrees))
                self.point.update()

                self.hue -= COLOR_CHANGE

                self.update_colors()

                score = self.player.score
                self.text = self.font.render(f"Score: {score}", False, self.color3)

            else:
                score = self.player.score
                self.next_scene = ["END", (self.color1, self.color2, self.color3, score, self.face_tracker)]




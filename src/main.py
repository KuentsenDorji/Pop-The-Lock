import sys
import pygame
from config import WIDTH, HEIGHT
from welcome_window import WelcomeWindow
from game_window import GameWindow
from end_window import EndWindow

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED, vsync=1)
    clock = pygame.time.Clock()
    scene = WelcomeWindow()

    while True:
        for event in pygame.event.get():
            scene.handle_events(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if scene.get_next_scene():
            scene = scene.get_next_scene()

        scene.update()
        scene.draw(screen)
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
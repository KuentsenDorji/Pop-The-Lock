import sys
import pygame
from config import SCREEN_HEIGHT, SCREEN_WIDTH
from welcome_window import WelcomeWindow
from game_window import GameWindow
from end_window import EndWindow

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED, vsync=1)
    clock = pygame.time.Clock()
    scene = WelcomeWindow()

    scenes = {
        "WELCOME": WelcomeWindow,
        "GAME": GameWindow,
        "END": EndWindow
    }

    while True:
        for event in pygame.event.get():
            scene.handle_events(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        next_scene_name = scene.get_next_scene()

        if next_scene_name:
            if len(next_scene_name) == 1:
                scene = scenes[next_scene_name[0]]()
            else:
                scene = scenes[next_scene_name[0]](*next_scene_name[1])

        scene.update()
        scene.draw(screen)
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
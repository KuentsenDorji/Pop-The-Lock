import sys
import pygame
from config import WIDTH, HEIGHT
from welcome_window import WelcomeWindow

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
        clock.tick(30)


if __name__ == '__main__':
    main()
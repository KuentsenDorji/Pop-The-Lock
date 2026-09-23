import sys
import pygame
from config import SCREEN_HEIGHT, SCREEN_WIDTH, FPS
from welcome_window import WelcomeWindow
from game_window import GameWindow
from end_window import EndWindow
from face_tracking import FaceTracker
from utils import load_sound

def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED, vsync=1)
    clock = pygame.time.Clock()
    face_tracker = FaceTracker()
    scene = WelcomeWindow(face_tracker)

    pygame.mixer.music.load(load_sound("Music.mp3"))

    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.3)

    scenes = {
        "WELCOME": WelcomeWindow,
        "GAME": GameWindow,
        "END": EndWindow
    }

    while True:

        for event in pygame.event.get():
            scene.handle_events(event)
            if event.type == pygame.QUIT:
                face_tracker.camera.stop()
                face_tracker.cleanup()
                pygame.quit()
                sys.exit()


        scene.handle_camera()
        scene.update()
        scene.draw(screen)
        pygame.display.update()

        next_scene_name = scene.get_next_scene()

        if next_scene_name:
            scene = scenes[next_scene_name[0]](*next_scene_name[1])


        clock.tick(FPS)


if __name__ == '__main__':
    main()
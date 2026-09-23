import pygame
import cv2
import threading
from cvzone.FaceMeshModule import FaceMeshDetector
from config import CAMERA_RESOLUTION, AMPLITUDE, MOUTH_THRESHOLD, LOADING_RADIUS, COLOR3, CAMERA_X, CAMERA_Y, BORDER_X, BORDER_Y, BORDER_RESOLUTION, COLOR2, BORDER_THICKNESS, LOADING_DISTANCE
from utils import get_hsv_color
import math


class FaceTracker:
    def __init__(self):
        self.detector = FaceMeshDetector(maxFaces=1)
        self.faces = None
        self.face_screen = None
        self.timer = 0

        self.running = True
        self.lock = threading.Lock()

        self.thread = threading.Thread(target=self.camera_thread, daemon=True)
        self.thread.start()

        self.border_color = get_hsv_color(*COLOR2)
        self.camera_border = pygame.Rect(BORDER_X, BORDER_Y, BORDER_RESOLUTION[0], BORDER_RESOLUTION[1])

        self.center_pos = [0, 0, 0]
        self.initiate_loading()
        self.loading_color = get_hsv_color(*COLOR3)

        self.loading_timer = 0

    def camera_thread(self):
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        frame_count = 0

        while self.running:

            success, img = cap.read()

            if not success:
                continue

            img, faces = self.detector.findFaceMesh(img, draw=True)


            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            img_pygame = img_rgb.swapaxes(0, 1)
            surface = pygame.surfarray.make_surface(img_pygame)
            surface = pygame.transform.scale(surface, (CAMERA_RESOLUTION[0], CAMERA_RESOLUTION[1]))

            with self.lock:
                self.faces = faces
                self.face_screen = surface

        cap.release()

    def update_color(self, hue):
        self.border_color = get_hsv_color(hue, COLOR2[1], COLOR2[2])

    def draw(self, screen):

        pygame.draw.rect(screen, self.border_color, self.camera_border, BORDER_THICKNESS)


        with self.lock:
            if self.face_screen is not None:
                screen.blit(self.face_screen,
                            (CAMERA_X, CAMERA_Y))

        self.loading_animation(screen)


    def win_con(self):
        with self.lock:
            current_faces = self.faces

        if current_faces and self.timer_ready():
            face = current_faces[0]
            upper_lip = face[0]
            lower_lip = face[14]
            left_eye = face[77]
            right_eye = face[324]

            vert, _ = self.detector.findDistance(upper_lip, lower_lip)
            hori, _ = self.detector.findDistance(left_eye, right_eye)

            ratio_mouth_closed = vert / hori * 100

            if ratio_mouth_closed <= MOUTH_THRESHOLD:
                self.timer = pygame.time.get_ticks()
                return True

        return False

    def timer_ready(self):
        return pygame.time.get_ticks() - self.timer >= 500

    def cleanup(self):
        self.running = False
        self.thread.join()

    def is_ready(self):
        return self.face_screen is not None

    def initiate_loading(self):
        for i in range(-1, 2):
            self.center_pos[i + 1] = (self.camera_border.centerx + i * LOADING_DISTANCE, self.camera_border.centery)

    def loading_animation(self, screen):

        if not self.is_ready():

            self.loading_timer += 0.1

            for i in range(-1, 2):

                dot_angle = self.loading_timer + (i * 0.8)

                y_offset = math.sin(dot_angle) * AMPLITUDE

                current_y = self.camera_border.centery + y_offset

                self.center_pos[i + 1] = (self.camera_border.centerx + i * LOADING_DISTANCE, current_y)

                pygame.draw.circle(screen, self.loading_color, self.center_pos[i+1], LOADING_RADIUS)














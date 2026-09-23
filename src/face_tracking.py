import pygame
import cv2
import threading
from cvzone.FaceMeshModule import FaceMeshDetector
from config import SCREEN_WIDTH, SCREEN_HEIGHT, CAMERA_RESOLUTION, MOUTH_THRESHOLD


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

    def camera_thread(self):
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_RESOLUTION[0])
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_RESOLUTION[1])

        while self.running:
            success, img = cap.read()
            if not success:
                continue

            img, faces = self.detector.findFaceMesh(img, draw=True)

            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            img_pygame = img_rgb.swapaxes(0, 1)
            surface = pygame.surfarray.make_surface(img_pygame)

            with self.lock:
                self.faces = faces
                self.face_screen = surface

        cap.release()

    def update(self):
        pass

    def draw(self, screen):
        with self.lock:
            if self.face_screen is not None:
                screen.blit(self.face_screen,
                            (SCREEN_WIDTH - CAMERA_RESOLUTION[0], SCREEN_HEIGHT - CAMERA_RESOLUTION[1]))

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








import pygame

class Clock:
    def __init__(self, fps):
        self.clock = pygame.time.Clock()
        self.fps = fps
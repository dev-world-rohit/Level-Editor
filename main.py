import pygame
from pygame.locals import *

from data.scripts.font import Font
from data.scripts.clock import Clock


class GameWindow:
    def __init__(self):
        pygame.init()

        self.tile_size = [16, 16]
        self.tile_number = [30, 20]
        self.screen_size = [(self.tile_size[0] * self.tile_number[0]) * 2 + 201, (self.tile_size[1] * self.tile_number[1]) * 2]
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Level Editor")
        pygame.display.set_icon(pygame.image.load("data/images/level_editor.png"))
        self.editor_size = (self.tile_size[0] * self.tile_number[0], self.tile_size[1] * self.tile_number[1])
        self.editor_display = pygame.Surface(self.editor_size)
        self.tileset_display = pygame.Surface((200, self.screen_size[1]))

        self.text = Font('small_font.png')
        self.clock = Clock(30)

        self.game = True

    def main_loop(self):
        while self.game:
            self.screen.fill((255, 0, 0))
            self.editor_display.fill((0, 0, 0))
            self.tileset_display.fill((0, 0, 0))

            self.text.display_fonts(self.editor_display, "Hello, World!", [10, 10], 2)
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.game = False

            self.screen.blit(pygame.transform.scale(self.editor_display, [self.screen_size[0] - 201, self.screen_size[1]]), (0, 0))
            self.screen.blit(self.tileset_display, (self.screen_size[0] - 200, 0))
            self.clock.clock.tick(self.clock.fps)
            pygame.display.update()

if __name__ == "__main__":
    game = GameWindow()
    game.main_loop()
    pygame.quit()

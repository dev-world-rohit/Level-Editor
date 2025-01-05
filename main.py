import pygame
from pygame.locals import *

from data.scripts.font import Font
from data.scripts.clock import Clock
from data.scripts.tileset_loader import TileSetManager

class GameWindow:
    def __init__(self):
        pygame.init()

        self.tile_size = [16, 16]
        self.tile_number = [30, 20]
        self.ratio = 2
        self.screen_size = [(self.tile_size[0] * self.tile_number[0]) * self.ratio + 201, (self.tile_size[1] * self.tile_number[1]) * self.ratio]
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Level Editor")
        pygame.display.set_icon(pygame.image.load("data/images/level_editor.png"))
        self.editor_size = (self.tile_size[0] * self.tile_number[0], self.tile_size[1] * self.tile_number[1])
        self.editor_display = pygame.Surface(self.editor_size)
        self.tileset_display = pygame.Surface((200, self.screen_size[1]))

        self.text = Font('small_font.png', (255, 255, 255), 2)
        self.clock = Clock(30)
        self.tileset_manager = TileSetManager()

        self.game = True

    def main_loop(self):
        click = False
        while self.game:
            mouse_pos = pygame.mouse.get_pos()

            self.screen.fill((0, 149, 239))
            self.editor_display.fill((0, 0, 0))
            self.tileset_display.fill((0, 0, 0))

            self.tileset_manager.display_tilesets(self.tileset_display, self.text, self.screen_size, mouse_pos, click)

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.game = False

                if event.type == pygame.KEYDOWN:
                    if event.key == K_r:
                        self.tileset_manager.change_tileset_number(1)
                    if event.key == K_e:
                        self.tileset_manager.change_tileset_number(-1)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # left click
                        click = True
                    if event.button == 2:  # mouse wheel click
                        print("2")
                    if event.button == 3:  # right click
                        print("3")
                    if event.button == 4:  # anti-clock wise mouse wheel rotation
                        self.tileset_manager.initial_pos_y += 16
                        if self.tileset_manager.initial_pos_y > 50:
                            self.tileset_manager.initial_pos_y = 50

                    if event.button == 5:  # clock wise mouse wheel rotation
                        self.tileset_manager.initial_pos_y -= 16

                # if event.type == pygame.MOUSEBUTTONUP:
                #     if event.button == 1:  # left click
                #         print("1")
                #     if event.button == 2:  # mouse wheel click
                #         print("2")
                #     if event.button == 3:  # right click
                #         print("3")
                #     if event.button == 4:  # anti-clock wise mouse wheel rotation
                #         print("4")
                #     if event.button == 5:  # clock wise mouse wheel rotation
                #         print("5")

            self.screen.blit(pygame.transform.scale(self.editor_display, [self.screen_size[0] - 201, self.screen_size[1]]), (0, 0))
            self.screen.blit(self.tileset_display, (self.screen_size[0] - 200, 0))
            self.clock.clock.tick(self.clock.fps)
            pygame.display.update()

if __name__ == "__main__":
    game = GameWindow()
    game.main_loop()
    pygame.quit()

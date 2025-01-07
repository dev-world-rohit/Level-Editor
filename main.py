import pygame
from pygame.locals import *

from data.scripts.font import Font
from data.scripts.clock import Clock
from data.scripts.tileset_loader import TileSetManager
from data.scripts.editor_manager import EditorManager


class GameWindow:
    def __init__(self):
        pygame.init()

        self.tile_size = [16, 16]
        self.tile_number = [30, 20]
        self.ratio = 2
        self.screen_size = [(self.tile_size[0] * self.tile_number[0]) * self.ratio + 201, (self.tile_size[1] *
                                                                                           self.tile_number[1]) * self.ratio]
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Level Editor")
        pygame.display.set_icon(pygame.image.load("data/images/level_editor.png"))
        self.editor_size = (self.tile_size[0] * self.tile_number[0], self.tile_size[1] * self.tile_number[1])
        self.editor_display = pygame.Surface(self.editor_size)
        self.tileset_display = pygame.Surface((200, self.screen_size[1]))

        self.text = Font('small_font.png', (255, 255, 255), 2)
        self.editor_text = Font('small_font.png', (255, 255, 255), 1)
        self.clock = Clock(30)
        self.tileset_manager = TileSetManager()
        self.editor_manager = EditorManager()

        self.game = True

    def main_loop(self):
        while self.game:
            mouse_pos = pygame.mouse.get_pos()

            self.screen.fill((0, 149, 239))
            self.editor_display.fill((0, 0, 0))
            self.tileset_display.fill((0, 0, 0))

            self.tileset_manager.display_tilesets(self.tileset_display, self.text, self.screen_size, mouse_pos,
                                                  self.tileset_manager.click)

            self.editor_manager.show_map(self.editor_display)
            self.editor_display.blit(self.tileset_manager.tile, (((mouse_pos[0] // self.ratio) // 16) *
                                     16, ((mouse_pos[1] // self.ratio)
                                          // 16) * 16))

            self.editor_manager.show_layer(self.editor_display, self.editor_text)
            self.editor_manager.change_offset(self.tile_size[0])
            if self.editor_manager.click:
                pos = [(((mouse_pos[0]) // self.ratio) // 16) *
                       16, (((mouse_pos[1]) // self.ratio)
                            // 16) * 16]
                self.editor_manager.add_tile([self.tileset_manager.current_tileset,
                                              self.tileset_manager.tile], pos)
            if self.editor_manager.erase_click:
                pos = [((mouse_pos[0] // self.ratio) // 16) *
                       16, ((mouse_pos[1] // self.ratio)
                            // 16) * 16]
                self.editor_manager.remove_tile(pos)


            for event in pygame.event.get():
                if event.type == QUIT:
                    self.game = False

                if event.type == pygame.KEYDOWN:
                    if event.key == K_r:
                        self.tileset_manager.change_tileset_number(1)
                    if event.key == K_w:
                        self.tileset_manager.change_tileset_number(-1)
                    if event.key == K_3:
                        self.editor_manager.change_layer(1)
                    if event.key == K_4:
                        self.editor_manager.change_layer(-1)
                    if event.key == K_a:
                        self.editor_manager.shift_x = "right"
                    if event.key == K_f:
                        self.editor_manager.shift_x = "left"
                    if event.key == K_e:
                        self.editor_manager.shift_y = "top"
                    if event.key == K_d:
                        self.editor_manager.shift_y = "bottom"
                    if event.key == K_s:
                        self.editor_manager.save_map(self.tileset_manager.tileset_data)
                    if event.key == K_i:
                        self.editor_manager.load_map(self.tileset_manager.tileset_data)

                if event.type == pygame.KEYUP:
                    if event.key == K_a:
                        self.editor_manager.shift_x = None
                    if event.key == K_f:
                        self.editor_manager.shift_x = None
                    if event.key == K_e:
                        self.editor_manager.shift_y = None
                    if event.key == K_d:
                        self.editor_manager.shift_y = None

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # left click
                        if self.screen_size[0] - 200 < mouse_pos[0] < self.screen_size[0]:
                            self.tileset_manager.click = True
                        else:
                            self.editor_manager.click = True
                    if event.button == 2:  # mouse wheel click
                        print("2")
                    if event.button == 3:  # right click
                        self.editor_manager.erase_click = True

                    if event.button == 4:  # anti-clock wise mouse wheel rotation
                        if self.screen_size[0] - 200 < mouse_pos[0] < self.screen_size[0]:
                            self.tileset_manager.initial_pos_y += self.tile_size[0] * self.ratio
                            if self.tileset_manager.initial_pos_y > 50:
                                self.tileset_manager.initial_pos_y = 50
                    if event.button == 5:  # clock wise mouse wheel rotation
                        self.tileset_manager.initial_pos_y -= 16

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:  # left click
                        self.editor_manager.click = False
                #     if event.button == 2:  # mouse wheel click
                #         print("2")
                    if event.button == 3:  # right click
                        self.editor_manager.erase_click = False
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

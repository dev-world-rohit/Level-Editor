import pygame

from data.scripts.file_manager import read_json
from data.scripts.image_functions import load_image, clip_surface

def tileset_loader(folder_name, tileset_name, tile_width, tile_height, tile_space = 0):
    tileset_image = load_image(folder_name + "/" +tileset_name + ".png")
    tileset = []
    tileset_width = tileset_image.get_width()
    pos_x = 0
    pos_y = 0
    while pos_x + 1 < tileset_width:
        tile = clip_surface(tileset_image, pos_x, pos_y, tile_width, tile_height)
        tileset.append(tile)
        pos_x += tile_width + tile_space
        if pos_x + 1 >= tileset_width:
            if pos_y + 1 >= tile_height:
                break
            pos_y += tile_height + tile_space
            pos_x = 0
    return tileset


class TileSetManager:
    def __init__(self):
        self.path = "images/tilesets_data.txt"
        self.tileset_data = {}
        self.tileset_file_data = read_json(self.path)

    def load_tilesets(self):
        self.tileset_file_data = self.tileset_file_data.split('\n')
        for i in range(1, len(self.tileset_file_data) - 1):
            tile_data = self.tileset_file_data[i].split(' ')
            self.tileset_data[tile_data[1]] = tileset_loader(tile_data[0], tile_data[1], int(tile_data[2]), int(tile_data[3]), int(tile_data[4]))

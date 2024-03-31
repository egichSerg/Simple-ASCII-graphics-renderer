import numpy as np
import os


class Sprite:
    def __init__(self, texture):
        self.texture = list()
        self.lindents = np.empty(shape=0)
        self.sprite_width = 0



        # define texture with left side indents
        # To draw things nicely we only need left side indents and raw line without spaces. That's why I .strip() line
        for row in texture:
            self.texture.append(np.array(list(row.strip())))
            self.lindents = np.append(self.lindents, len(row)-len(row.lstrip()))
            self.sprite_width = max(self.sprite_width, len(row))

        self.sprite_height = len(self.texture)
        self.lindents = self.lindents.astype(np.int32)


    def get_texture(self):
        return self.texture
    
    def get_size(self):
        return (self.sprite_width, self.sprite_height)
    
    def get_indent(self):
        return self.lindents
    

class TextRenderer:

    # init with width (in chars per row) and height (in rows) of field
    def __init__(self, width, height):
        self.canvas = np.full(shape=(height, width), fill_value=' ')
        self.xmax = width
        self.ymax = height

    # places sprite on canvas
    def draw_sprite(self, _sprite, x, y):
        width, height = _sprite.get_size()
        for i, (indent, row) in enumerate(zip(_sprite.get_indent(), _sprite.get_texture())):
            if y+i >= self.ymax:
                break

            self.canvas[max(0, y+i), max(x+indent, 0):min(x+indent+len(row), self.xmax)] = row[abs(min(0, x+indent)):min(len(row), max(0, self.xmax-x-indent))]

    # prints canvas
    def show(self):
        for line in self.canvas:
            print(*line, sep='')

    # clear screen, cross platform
    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')

    # reset canvas, clear screen
    def clear(self):
        self.canvas = np.full(shape=(self.ymax, self.xmax), fill_value=' ')
        self.cls()
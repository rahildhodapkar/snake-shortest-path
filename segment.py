import pyxel


class Segment:
    def __init__(self, x, y):
        self.w = 6
        self.x = x
        self.y = y
        self.prev_x = None
        self.prev_y = None
        self.sprite_img = 0
        self.sprite_width = 6
        self.sprite_u = 8
        self.sprite_v = 0

    def draw(self):
        pyxel.blt(
            self.x,
            self.y,
            self.sprite_img,
            self.sprite_u,
            self.sprite_v,
            self.sprite_width,
            self.sprite_width
        )

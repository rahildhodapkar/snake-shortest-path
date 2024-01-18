from random import randint

import pyxel


class Food:
    def __init__(self):
        self.w = 6
        self.x = None
        self.y = None
        self.generate_coordinates()

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.w, 7)

    def generate_coordinates(self):
        while True:
            self.x = int(randint(0, pyxel.width - self.w) / self.w) * self.w
            self.y = int(randint(0, pyxel.height - self.w) / self.w) * self.w
            if self.x != pyxel.width / 2 and self.y != pyxel.height / 2:
                break

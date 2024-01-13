import pyxel
from random import randint


class Food:
    def __init__(self):
        self.w = 6
        self.x = int(randint(0, pyxel.width - self.w) / self.w) * self.w
        self.y = int(randint(0, pyxel.height - self.w) / self.w) * self.w
        self.points = 3

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.w, 7)

    def update(self):
        pass

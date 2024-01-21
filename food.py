from random import randint

import pyxel


class Food:
    """Class that represents the bit of food the snake eats to grow in length."""

    def __init__(self):
        """Constructor for Food."""
        self.w = 6
        self.x = None
        self.y = None
        self.generate_coordinates()

    def draw(self):
        """Draws a rectangle at the specified X and Y coordinates representing the bit of food."""
        pyxel.rect(self.x, self.y, self.w, self.w, 7)

    def generate_coordinates(self):
        """Randomly generates an X and Y coordinate to represent the location of the Food when it is first initialized.

        Coordinates are generated randomly until the X and Y coordinate do not intercept where the snake initially
        starts.
        """
        while True:
            self.x = int(randint(0, pyxel.width - self.w) / self.w) * self.w
            self.y = int(randint(0, pyxel.height - self.w) / self.w) * self.w
            if self.x != pyxel.width / 2 and self.y != pyxel.height / 2:
                break

import pyxel


class Segment:
    """The segment class represents a segment of the snake.

    Each segment contains its X and Y coordinates, its previous X and Y coordinates,
    and information of its sprite.
    """

    def __init__(self, x, y):
        """Constructor for Segment

        :param x: X coordinate for location of segment
        :param y: Y coordinate for location of segment
        """
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
        """Draws the segment based on the segment's X and Y coordinates"""

        pyxel.blt(
            self.x,
            self.y,
            self.sprite_img,
            self.sprite_u,
            self.sprite_v,
            self.sprite_width,
            self.sprite_width
        )

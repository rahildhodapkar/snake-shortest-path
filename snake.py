import enum
import pyxel


class Direction(enum.Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Snake:
    def __init__(self):
        self.w = 6
        self.x = pyxel.width / 2
        self.y = pyxel.height / 2
        self.direction = None
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

    def update(self):
        self.check_input()
        match self.direction:
            case Direction.UP:
                self.y = int(self.y / self.w) * self.w - self.w
            case Direction.DOWN:
                self.y = int(self.y / self.w) * self.w + self.w
            case Direction.LEFT:
                self.x = int(self.x / self.w) * self.w - self.w
            case Direction.RIGHT:
                self.x = int(self.x / self.w) * self.w + self.w
            case _:
                pass

    def check_input(self):
        if pyxel.btnp(pyxel.KEY_W):
            self.direction = Direction.UP
        elif pyxel.btnp(pyxel.KEY_S):
            self.direction = Direction.DOWN
        elif pyxel.btnp(pyxel.KEY_A):
            self.direction = Direction.LEFT
        elif pyxel.btnp(pyxel.KEY_D):
            self.direction = Direction.RIGHT

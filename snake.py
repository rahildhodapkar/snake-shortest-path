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
                self.y = round(self.y / self.w) * self.w - self.w
            case Direction.DOWN:
                self.y = round(self.y / self.w) * self.w + self.w
            case Direction.LEFT:
                self.x = round(self.x / self.w) * self.w - self.w
            case Direction.RIGHT:
                self.x = round(self.x / self.w) * self.w + self.w
            case _:
                pass

    def check_input(self):
        if pyxel.btnp(pyxel.KEY_W) and self.direction != Direction.DOWN:
            self.direction = Direction.UP
        elif pyxel.btnp(pyxel.KEY_S) and self.direction != Direction.UP:
            self.direction = Direction.DOWN
        elif pyxel.btnp(pyxel.KEY_A) and self.direction != Direction.RIGHT:
            self.direction = Direction.LEFT
        elif pyxel.btnp(pyxel.KEY_D) and self.direction != Direction.LEFT:
            self.direction = Direction.RIGHT

    def detect_food_collision(self, obj):
        num_steps = self.w
        if self.direction is None:
            return False

        step_size = 1.0 / num_steps

        for step in range(1, num_steps + 1):
            _L = step * step_size
            if self.direction == Direction.UP:
                sub_snake_x, sub_snake_y = self.x, self.y - _L * self.w
            elif self.direction == Direction.DOWN:
                sub_snake_x, sub_snake_y = self.x, self.y + _L * self.w
            elif self.direction == Direction.LEFT:
                sub_snake_x, sub_snake_y = self.x - _L * self.w, self.y
            elif self.direction == Direction.RIGHT:
                sub_snake_x, sub_snake_y = self.x + _L * self.w, self.y

            if (
                    sub_snake_x + self.w > obj.x
                    and sub_snake_x < obj.x + obj.w
                    and sub_snake_y + self.w > obj.y
                    and sub_snake_y < obj.y + obj.w
            ):
                return True
        return False


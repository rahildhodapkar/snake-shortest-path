import enum
import pyxel
from segment import Segment


class Direction(enum.Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    NOT_MOVING = 4


class Snake:
    def __init__(self):
        self.direction = None
        self.snake_list = None

    def load_snake(self):
        self.snake_list = []
        self.snake_list.append(Segment(pyxel.width / 2, pyxel.height / 2))
        self.direction = None

    def draw(self):
        for seg in self.snake_list:
            seg.draw()

    def update(self):
        if self.direction == Direction.NOT_MOVING:
            return

        self.check_input()
        w = self.snake_list[0].w

        head = self.snake_list[0]
        head.prev_x, head.prev_y = head.x, head.y
        match self.direction:
            case Direction.UP:
                head.y -= w
            case Direction.DOWN:
                head.y += w
            case Direction.LEFT:
                head.x -= w
            case Direction.RIGHT:
                head.x += w

        if len(self.snake_list) > 1:
            for i in range(1, len(self.snake_list)):
                self.snake_list[i].prev_x, self.snake_list[i].prev_y = self.snake_list[i].x, self.snake_list[i].y
                self.snake_list[i].x, self.snake_list[i].y = self.snake_list[i - 1].prev_x, self.snake_list[
                    i - 1].prev_y

    def check_input(self):
        if (pyxel.btnp(pyxel.KEY_W) or pyxel.btnp(pyxel.KEY_UP)) and self.direction != Direction.DOWN:
            self.direction = Direction.UP
        elif (pyxel.btnp(pyxel.KEY_S) or pyxel.btnp(pyxel.KEY_DOWN)) and self.direction != Direction.UP:
            self.direction = Direction.DOWN
        elif (pyxel.btnp(pyxel.KEY_A) or pyxel.btnp(pyxel.KEY_LEFT)) and self.direction != Direction.RIGHT:
            self.direction = Direction.LEFT
        elif (pyxel.btnp(pyxel.KEY_D) or pyxel.btnp(pyxel.KEY_RIGHT)) and self.direction != Direction.LEFT:
            self.direction = Direction.RIGHT

    def detect_food_collision(self, obj):
        num_steps = 6
        w = 6
        if self.direction is None:
            return False

        step_size = 1.0 / num_steps

        sub_snake_x, sub_snake_y = 0, 0

        for step in range(1, num_steps + 1):
            _L = step * step_size
            if self.direction == Direction.UP:
                sub_snake_x, sub_snake_y = self.snake_list[0].x, self.snake_list[0].y - _L * w
            elif self.direction == Direction.DOWN:
                sub_snake_x, sub_snake_y = self.snake_list[0].x, self.snake_list[0].y + _L * w
            elif self.direction == Direction.LEFT:
                sub_snake_x, sub_snake_y = self.snake_list[0].x - _L * w, self.snake_list[0].y
            elif self.direction == Direction.RIGHT:
                sub_snake_x, sub_snake_y = self.snake_list[0].x + _L * w, self.snake_list[0].y

            if (
                    sub_snake_x + w > obj.x
                    and sub_snake_x < obj.x + obj.w
                    and sub_snake_y + w > obj.y
                    and sub_snake_y < obj.y + obj.w
            ):
                self.update_snake()
                return True
        return False

    def detect_out_of_bounds(self):
        x = self.snake_list[0].x
        y = self.snake_list[0].y
        w = self.snake_list[0].w

        if (
                y < 0 or
                y + w > pyxel.height or
                x < 0 or
                x + w > pyxel.width
        ):
            return True
        return False

    def detect_snake_collision(self):
        if len(self.snake_list) < 1:
            return False
        x = self.snake_list[0].x
        y = self.snake_list[0].y
        for i in range(1, len(self.snake_list), 1):
            if x == self.snake_list[i].x and y == self.snake_list[i].y:
                return True
        return False

    def update_snake(self):
        last_seg = self.snake_list[len(self.snake_list) - 1]
        seg = Segment(last_seg.prev_x, last_seg.prev_y)
        self.snake_list.append(seg)

    def end_snake(self):
        self.direction = Direction.NOT_MOVING

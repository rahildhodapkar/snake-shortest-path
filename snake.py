from collections import deque as queue
import heapq

import pyxel

from direction import Direction
from segment import Segment
from node import Node


def get_direction_from_parent(parent, current):
    py, px = parent
    cy, cx = current
    if cx == px + 1:
        return Direction.RIGHT
    if cx == px - 1:
        return Direction.LEFT
    if cy == py + 1:
        return Direction.DOWN
    if cy == py - 1:
        return Direction.UP


def reconstruct_path(parent, start, goal):
    path = []
    current = goal
    while current != start:
        prev = parent[current]
        direction = get_direction_from_parent(prev, current)
        path.append(direction)
        current = prev
    path.reverse()
    return path


def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


class Snake:
    def __init__(self):
        self.direction = None
        self.direction_list = []
        self.snake_list = None
        self.grid = None

    def load_snake(self):
        self.snake_list = []
        self.snake_list.append(Segment(pyxel.width / 2, pyxel.height / 2))
        self.direction = None

    def draw(self):
        for seg in self.snake_list:
            seg.draw()

    def update(self, mode, food_x, food_y):
        if self.direction == Direction.NOT_MOVING:
            return

        if mode == 0:
            self.check_input()
        elif mode == 1:
            self.load_grid()
            self.bfs(food_x, food_y)
            if len(self.direction_list) > 0:
                self.direction = self.direction_list.pop(0)
        elif mode == 2:
            self.load_grid()
            self.a_star(food_x, food_y)
            if len(self.direction_list) > 0:
                self.direction = self.direction_list.pop(0)

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
                self.snake_list[i].x, self.snake_list[i].y = (
                    self.snake_list[i - 1].prev_x,
                    self.snake_list[i - 1].prev_y
                )

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
        tail = self.snake_list[len(self.snake_list) - 1]
        seg = Segment(tail.prev_x, tail.prev_y)
        self.snake_list.append(seg)

    def end_snake(self):
        self.direction = Direction.NOT_MOVING

    def load_grid(self):
        rows = pyxel.height // 6
        cols = pyxel.width // 6
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        for seg in self.snake_list:
            grid_x = round(seg.x / 6)
            grid_y = round(seg.y / 6)
            if 0 <= grid_x < len(self.grid[0]) and 0 <= grid_y < len(self.grid):
                self.grid[grid_y][grid_x] = 1

    def bfs(self, food_x, food_y):
        rows, cols = len(self.grid), len(self.grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        q = queue()
        parent = {}

        d_row = [1, -1, 0, 0]
        d_col = [0, 0, -1, 1]

        head = self.snake_list[0]
        start = (round(head.y / 6), round(head.x / 6))
        goal = (round(food_y / 6), round(food_x / 6))

        q.append(start)
        visited[start[0]][start[1]] = True

        while q:
            y, x = q.popleft()
            if (y, x) == goal:
                self.direction_list = reconstruct_path(parent, start, goal)
                return

            for i in range(4):
                adj_y, adj_x = y + d_row[i], x + d_col[i]
                if self.is_valid(adj_y, adj_x, visited):
                    q.append((adj_y, adj_x))
                    visited[adj_y][adj_x] = True
                    parent[(adj_y, adj_x)] = (y, x)

        self.direction_list = []

    def a_star(self, food_x, food_y):
        pq = []
        rows, cols = len(self.grid), len(self.grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        node_grid = [[Node(0, 0, 0) for _ in range(cols)] for _ in range(rows)]
        parent = {}

        d_row = [1, -1, 0, 0]
        d_col = [0, 0, -1, 1]

        head = self.snake_list[0]
        start = (round(head.y / 6), round(head.x / 6))
        goal = (round(food_y / 6), round(food_x / 6))
        heapq.heappush(pq, (0, start))

        while len(pq) > 0:
            current = heapq.heappop(pq)[1]
            y, x = current[0], current[1]
            visited[y][x] = True

            if x == goal[1] and y == goal[0]:
                self.direction_list = reconstruct_path(parent, start, goal)
                return

            for i in range(4):
                adj_y, adj_x = y + d_row[i], x + d_col[i]
                if self.is_valid(adj_y, adj_x, visited):
                    child = node_grid[adj_y][adj_x]
                    child.g = node_grid[y][x].g + manhattan_distance((adj_y, adj_x), (y, x))
                    child.h = manhattan_distance((adj_y, adj_x), (food_y, food_x))
                    child.f = child.g + child.h

                    for n in pq:
                        if (n[1][1], n[1][0]) == (adj_x, adj_y):
                            if child.g >= node_grid[adj_y][adj_x].g:
                                break
                    else:
                        heapq.heappush(pq, (child.f, (adj_y, adj_x)))
                        parent[(adj_y, adj_x)] = (y, x)

    def is_valid(self, row, col, visited):
        return (
                0 <= row < len(self.grid) and
                0 <= col < len(self.grid[0]) and
                not visited[row][col] and
                self.grid[row][col] == 0
        )

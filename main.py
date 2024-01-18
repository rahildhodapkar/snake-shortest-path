from random import randint

import pyxel

from food import Food
from gamestate import GameState
from hud import (draw_automatic_instructions, draw_game_over, draw_hud,
                 draw_manual_instructions, draw_pause_instructions,
                 draw_ready_screen)
from snake import Snake


class App:
    def __init__(self):
        pyxel.init(384, 300, display_scale=2, title="SNAKE SHORTEST PATH", fps=20)
        pyxel.load("assets/resources.pyxres")
        self.food = None
        self.snake = Snake()
        self.score = None
        self.state = GameState.READY
        self.is_manual = True
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.state == GameState.READY:
            self.food = Food()
            self.snake.load_snake()
            self.score = 1
            if pyxel.btnp(pyxel.KEY_1):
                self.state = GameState.MANUAL
            if pyxel.btnp(pyxel.KEY_2):
                self.state = GameState.BFS

        if self.state == GameState.MANUAL:
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.state = GameState.RUNNING

        if self.state == GameState.BFS:
            self.is_manual = False
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.state = GameState.RUNNING

        if self.state == GameState.RUNNING:
            if pyxel.btnp(pyxel.KEY_P):
                self.state = GameState.PAUSED
                return
            self.check_collision()
            self.snake.update(self.is_manual, self.food.x, self.food.y)

        if self.state == GameState.PAUSED:
            if pyxel.btnp(pyxel.KEY_P):
                self.state = GameState.RUNNING

        if self.state == GameState.END:
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.state = GameState.READY
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        if self.state == GameState.END:
            draw_game_over(self.score)
        if self.state == GameState.READY:
            draw_ready_screen()
        if self.state == GameState.MANUAL:
            draw_manual_instructions()
        if self.state == GameState.BFS:
            draw_automatic_instructions()
        if self.state == GameState.RUNNING:
            self.snake.draw()
            self.food.draw()
            draw_hud(self.score)
        if self.state == GameState.PAUSED:
            draw_pause_instructions()

    def check_collision(self):
        if self.snake.detect_out_of_bounds() or self.snake.detect_snake_collision():
            self.snake.end_snake()
            self.state = GameState.END
        if self.snake.detect_food_collision(self.food):
            while True:
                self.food.x = int(randint(0, pyxel.width - self.food.w) / self.food.w) * self.food.w
                self.food.y = int(randint(0, pyxel.height - self.food.w) / self.food.w) * self.food.w
                flag = False
                for seg in self.snake.snake_list:
                    if self.food.x == seg.x and self.food.y == seg.y:
                        flag = True
                        break
                if not flag:
                    break
            self.score += 1


App()

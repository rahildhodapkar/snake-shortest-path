from random import randint

import pyxel

from food import Food
from gamestate import GameState
from hud import (draw_automatic_instructions, draw_game_over, draw_hud,
                 draw_manual_instructions, draw_pause_instructions,
                 draw_ready_screen, draw_game_type, draw_avg_time_to_compute_path)
from snake import Snake


class App:
    """Driver file for program.

    Initiates the game to run at 20 fps, running the program at more than 20 fps leads to performance
    issues for the A* algorithm.
    """
    def __init__(self):
        pyxel.init(384, 300, display_scale=2, title="SNAKE SHORTEST PATH", fps=20)
        pyxel.load("assets/resources.pyxres")
        self.food = None
        self.snake = Snake()
        self.score = None
        self.state = GameState.READY
        self.mode = None
        pyxel.run(self.update, self.draw)

    def update(self):
        """Updates the game based on which GameState it is in."""

        if self.state == GameState.READY:
            self.food = Food()
            self.snake.load_snake()
            self.score = 1
            if pyxel.btnp(pyxel.KEY_1):
                self.state = GameState.MANUAL
            if pyxel.btnp(pyxel.KEY_2):
                self.state = GameState.BFS
            if pyxel.btnp(pyxel.KEY_3):
                self.state = GameState.A_STAR
            if pyxel.btnp(pyxel.KEY_4):
                self.state = GameState.GREEDY_BEST_FIRST

        if self.state == GameState.MANUAL:
            self.mode = 0
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.state = GameState.RUNNING

        if self.state == GameState.BFS:
            self.mode = 1
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.state = GameState.RUNNING

        if self.state == GameState.A_STAR:
            self.mode = 2
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.state = GameState.RUNNING

        if self.state == GameState.GREEDY_BEST_FIRST:
            self.mode = 3
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.state = GameState.RUNNING

        if self.state == GameState.RUNNING:
            if pyxel.btnp(pyxel.KEY_P):
                self.state = GameState.PAUSED
                return
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()
            if pyxel.btnp(pyxel.KEY_E):
                self.state = GameState.END
                return
            self.check_collision()
            self.snake.update(self.mode, self.food.x, self.food.y)

        if self.state == GameState.PAUSED:
            if pyxel.btnp(pyxel.KEY_P):
                self.state = GameState.RUNNING
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()

        if self.state == GameState.END:
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.state = GameState.READY
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()

    def draw(self):
        """Draws components related to the current GameState."""

        pyxel.cls(0)
        if self.state == GameState.END:
            draw_game_over(self.score)
        if self.state == GameState.READY:
            draw_ready_screen()
        if self.state == GameState.MANUAL:
            draw_manual_instructions()
        if (
                self.state == GameState.BFS or
                self.state == GameState.A_STAR or
                self.state == GameState.GREEDY_BEST_FIRST
        ):
            draw_automatic_instructions()
        if self.state == GameState.RUNNING:
            self.snake.draw()
            self.food.draw()
            if self.mode > 0:
                draw_avg_time_to_compute_path(self.snake.avg_time)
            draw_hud(self.score)
            draw_game_type(self.mode)
        if self.state == GameState.PAUSED:
            draw_pause_instructions()

    def check_collision(self):
        """Checks if the snake ever collides with itself, food, or goes out-of-bounds.

        If the snake collides with food, the score is incremented by 1. If it goes out-of-bounds or collides with itself,
        the GameState is set to GameState.END
        """

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

import enum
import pyxel
from hud import draw_hud, draw_ready_screen, draw_game_over, draw_manual_instructions, draw_pause_instructions
from food import Food
from snake import Snake
from random import randint


class GameState(enum.Enum):
    READY = 0
    MANUAL = 1
    BFS = 2
    RUNNING = 3
    PAUSED = 4
    END = 5


class App:
    def __init__(self):
        pyxel.init(384, 300, display_scale=3, title="Segment", fps=20)
        pyxel.load("assets/resources.pyxres")
        self.food = Food()
        self.snake = Snake()
        self.score = None
        self.state = GameState.READY
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.state == GameState.READY:
            self.snake.load_snake()
            self.score = 0
            if pyxel.btnp(pyxel.KEY_1):
                self.state = GameState.MANUAL
            if pyxel.btnp(pyxel.KEY_2):
                self.state = GameState.BFS

        if self.state == GameState.MANUAL or GameState.BFS:
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.state = GameState.RUNNING

        if self.state == GameState.RUNNING:
            if pyxel.btnp(pyxel.KEY_P):
                self.state = GameState.PAUSED
                return
            self.snake.update()
            self.check_collision()

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
            draw_game_over(score=self.score)
        if self.state == GameState.READY:
            draw_ready_screen()
        if self.state == GameState.MANUAL:
            draw_manual_instructions()
        if self.state == GameState.RUNNING:
            self.snake.draw()
            self.food.draw()
            draw_hud(score=self.score)
        if self.state == GameState.PAUSED:
            draw_pause_instructions()

    def check_collision(self):
        if self.snake.detect_out_of_bounds() or self.snake.detect_snake_collision():
            self.snake.end_snake()
            self.state = GameState.END
        if self.snake.detect_food_collision(self.food):
            self.food.x = int(randint(0, pyxel.width - self.food.w) / self.food.w) * self.food.w
            self.food.y = int(randint(0, pyxel.height - self.food.w) / self.food.w) * self.food.w
            self.score += 1


App()

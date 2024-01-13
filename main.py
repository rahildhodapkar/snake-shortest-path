import pyxel
from food import Food
from snake import Snake
from random import randint
from hud import draw_hud


class App:
    def __init__(self):
        pyxel.init(384, 300, display_scale=3, title="Segment", fps=20)
        pyxel.load("assets/resources.pyxres")
        self.food = Food()
        self.snake = Snake()
        self.score = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.snake.update()

    def draw(self):
        pyxel.cls(0)
        self.snake.draw()
        if self.snake.detect_food_collision(self.food):
            self.food.x = int(randint(0, pyxel.width - self.food.w) / self.food.w) * self.food.w
            self.food.y = int(randint(0, pyxel.height - self.food.w) / self.food.w) * self.food.w
            self.score += 1
        self.food.draw()
        draw_hud(self.score)


App()

import pyxel
from food import Food
from snake import Snake


class App:
    def __init__(self):
        pyxel.init(384, 300, display_scale=3, title="Snake", fps=20)
        pyxel.load("assets/resources.pyxres")
        self.food = Food()
        self.snake = Snake()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.snake.update()

    def draw(self):
        pyxel.cls(0)
        self.food.draw()
        self.snake.draw()


App()

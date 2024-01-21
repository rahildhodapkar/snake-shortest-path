from enum import Enum


class Direction(Enum):
    """Enum class that represents directions the snake can move.

    NOT_MOVING is used to mark when the snake collides with itself or boundaries.
    """

    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    NOT_MOVING = 4

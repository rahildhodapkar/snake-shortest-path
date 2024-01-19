from enum import Enum


class GameState(Enum):
    READY = 0
    MANUAL = 1
    BFS = 2
    A_STAR = 3
    RUNNING = 4
    PAUSED = 5
    END = 6

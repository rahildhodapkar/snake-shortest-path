from enum import Enum


class GameState(Enum):
    READY = 0
    MANUAL = 1
    BFS = 2
    RUNNING = 3
    PAUSED = 4
    END = 5

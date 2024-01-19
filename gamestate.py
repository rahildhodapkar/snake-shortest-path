from enum import Enum


class GameState(Enum):
    READY = 0
    MANUAL = 1
    BFS = 2
    A_STAR = 3
    GREEDY_BEST_FIRST = 4
    RUNNING = 5
    PAUSED = 6
    END = 7

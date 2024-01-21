from enum import Enum


class GameState(Enum):
    """Enum class that represents the different GameStates

    READY represents the home page
    MANUAL represents the User choosing to play manually
    BFS represents the User choosing to use BFS
    A_STAR represents the User choosing to use A*
    Greedy_BEST_FIRST represents the User choosing to use Greedy Best-First
    RUNNING represents the game actually starting
    PAUSED represents the user pausing the game
    END represents a collision and the ability to either restart or quit
    """

    READY = 0
    MANUAL = 1
    BFS = 2
    A_STAR = 3
    GREEDY_BEST_FIRST = 4
    RUNNING = 5
    PAUSED = 6
    END = 7

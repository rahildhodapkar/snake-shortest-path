class Node:
    """This class is used in the A* and Greedy Best-First algorithms.

    Both of those algorithms require heuristics to run, so this Node class allows one to track those heuristics
    in the 2D grid representations of the game used in the search algorithms.
    """

    def __init__(self, f, g, h):
        self.f = f
        self.g = g
        self.h = h

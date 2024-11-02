from enum import Enum

import pygame


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


ALLOWED_NEW_DIRECTION = {
    Direction.UP: [Direction.LEFT, Direction.RIGHT],
    Direction.DOWN: [Direction.LEFT, Direction.RIGHT],
    Direction.LEFT: [Direction.UP, Direction.DOWN],
    Direction.RIGHT: [Direction.UP, Direction.DOWN]
}

DIRECTION_KEYS = {
    pygame.K_UP: Direction.UP,
    pygame.K_DOWN: Direction.DOWN,
    pygame.K_LEFT: Direction.LEFT,
    pygame.K_RIGHT: Direction.RIGHT
}
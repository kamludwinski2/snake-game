from typing import List, Tuple

from src.config import Config
from src.direction import ALLOWED_NEW_DIRECTION, Direction


class Snake:
    def __init__(self, initial_position: Tuple[int, int]) -> None:
        self.body: List[Tuple[int, int]] = [initial_position]
        self.direction: Direction = Direction.RIGHT
        self.grow_on_next_move: bool = False

    def get_head_position(self) -> Tuple[int, int]:
        return self.body[0]

    def move(self) -> bool:
        head_x, head_y = self.get_head_position()
        move_x, move_y = self.direction.value
        new_head = (head_x + move_x, head_y + move_y)

        if not (0 <= new_head[0] < Config.ROWS and 0 <= new_head[1] < Config.COLS):
            return False

        if new_head in self.body:
            return False

        if self.grow_on_next_move:
            self.body = [new_head] + self.body
            self.grow_on_next_move = False
        else:
            self.body = [new_head] + self.body[:-1]

        return True

    def change_direction(self, new_direction: Direction) -> None:
        if new_direction in ALLOWED_NEW_DIRECTION[self.direction]:
            self.direction = new_direction

    def get_body_positions(self) -> List[Tuple[int, int]]:
        return self.body
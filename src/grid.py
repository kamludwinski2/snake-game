import random
from typing import List, Tuple

from src.snake import Snake
from src.square_state import SquareState

from src.config import Config


class Grid:
    def __init__(self) -> None:
        self.rows: int = Config.ROWS
        self.cols: int = Config.COLS
        self.grid: List[List[SquareState]] = []
        self.snake = Snake((self.rows // 2, self.cols // 2))
        self.food_position: Tuple[int, int] | None = None

        self.reset_grid()
        self.place_food()
        self.update_grid()

    def __getitem__(self, index: int) -> List[SquareState]:
        return self.grid[index]

    def reset_grid(self) -> None:
        self.grid = [[SquareState.EMPTY for _ in range(self.cols)] for _ in range(self.rows)]

    def set_cell(self, row: int, col: int, state: SquareState) -> None:
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row][col] = state
        else:
            raise IndexError("Cell position out of bounds.")

    def update_grid(self) -> None:
        self.reset_grid()

        for row, col in self.snake.get_body_positions():
            self.grid[row][col] = SquareState.SNAKE

        if self.food_position:
            self.grid[self.food_position[0]][self.food_position[1]] = SquareState.FOOD

    def place_food(self) -> None:
        empty_cells = [(r, c) for r in range(self.rows) for c in range(self.cols)
                       if self.grid[r][c] == SquareState.EMPTY]
        if not empty_cells:
            raise ValueError("No empty space to place food.")

        self.food_position = random.choice(empty_cells)
        self.set_cell(self.food_position[0], self.food_position[1], SquareState.FOOD)
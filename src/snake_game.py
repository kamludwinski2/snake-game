import pygame
from pygame import Surface, SurfaceType

from src.colour import Colour
from src.config import Config
from src.direction import DIRECTION_KEYS
from src.grid import Grid
from src.square_state import SquareState


class SnakeGame:
    def __init__(self) -> None:
        pygame.init()

        self.grid: Grid = Grid()
        self.screen: Surface | SurfaceType = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
        pygame.display.set_caption(Config.WINDOW_NAME)

        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.running: bool = True
        self.direction_changed: bool = False
        self.moves: int = 0

    def draw_grid(self) -> None:
        for row in range(self.grid.rows):
            for col in range(self.grid.cols):
                cell_state = self.grid[row][col]
                colour = Colour.BLACK.value

                if cell_state == SquareState.SNAKE:
                    colour = Colour.GREEN.value
                elif cell_state == SquareState.FOOD:
                    colour = Colour.RED.value

                pygame.draw.rect(
                    self.screen,
                    colour,
                    pygame.Rect(col * Config.SQUARE_SIZE, row * Config.SQUARE_SIZE, Config.SQUARE_SIZE,
                                Config.SQUARE_SIZE)
                )

    def update_window_title(self) -> None:
        if (snake_length := (len(self.grid.snake.body)) - 1) > 0:
            pygame.display.set_caption(f'{Config.WINDOW_NAME} -Moves: {self.moves} -Points: {snake_length}')

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and not self.direction_changed:
                self.grid.snake.change_direction(DIRECTION_KEYS[event.key])
                self.direction_changed = True
                self.moves += 1

    def run(self) -> None:
        while self.running:
            self.handle_events()

            if not self.grid.snake.move():
                print('Game Over')
                self.running = False

            if self.grid.snake.get_head_position() == self.grid.food_position:
                self.grid.snake.grow_on_next_move = True
                self.grid.place_food()

            self.grid.update_grid()
            self.update_window_title()
            self.direction_changed = False

            self.screen.fill((0, 0, 0))
            self.draw_grid()
            pygame.display.flip()
            self.clock.tick(10)

        pygame.quit()
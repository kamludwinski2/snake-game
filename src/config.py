import json


class Config:
    SQUARE_SIZE: int = 25
    ROWS: int = 12
    COLS: int = 12

    WINDOW_NAME: str = 'Snake Game'
    WINDOW_WIDTH: int = ROWS * SQUARE_SIZE
    WINDOW_HEIGHT: int = COLS * SQUARE_SIZE

    FPS: int = 10

    @classmethod
    def load_from_file(cls, filename="resources/config.json"):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)

                cls.SQUARE_SIZE = data.get("squareSize", cls.SQUARE_SIZE)
                cls.ROWS = data.get("rows", cls.ROWS)
                cls.COLS = data.get("cols", cls.COLS)
                cls.WINDOW_NAME = data.get("windowName", cls.WINDOW_NAME)
                cls.FPS = data.get('fps', cls.FPS)

                cls.WINDOW_WIDTH = cls.ROWS * cls.SQUARE_SIZE
                cls.WINDOW_HEIGHT = cls.COLS * cls.SQUARE_SIZE

        except FileNotFoundError:
            print(f"Config file '{filename}' not found, using default values")

        finally:
            print(f"Config file '{filename}' loaded")
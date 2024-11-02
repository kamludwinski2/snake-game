from src.snake_game import SnakeGame

from src.config import Config

if __name__ == '__main__':
    Config.load_from_file()
    SnakeGame().run()
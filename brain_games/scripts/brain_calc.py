"""
Игра калькулятор.

Пользователю предлагается решить простой пример.
"""

from brain_games.games.calc import game
from brain_games.engine import execute


def main():
    """Вызов игры."""
    execute(game)


if __name__ == '__main__':
    main()

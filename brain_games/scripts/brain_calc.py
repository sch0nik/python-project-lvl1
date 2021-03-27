"""
Игра калькулятор.

Пользователю предлагается решить простой пример.
"""

from brain_games.games.calc import game
from scripts.engine import execution


def main():
    """Вызов игры."""
    execution(game)


if __name__ == '__main__':
    main()

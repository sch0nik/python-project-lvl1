"""
Игра калькулятор.

Пользователю предлагается решить пример.
"""

from brain_games.engine import execute
from brain_games.games import calc


def main():
    """Вызов игры."""
    execute(calc)


if __name__ == '__main__':
    main()

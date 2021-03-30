"""
Игра калькулятор.

Пользователю предлагается решить пример.
"""

from brain_games.engine import execute
from brain_games.games.calc import generating_game_values


def main():
    """Вызов игры."""
    execute(generating_game_values)


if __name__ == '__main__':
    main()

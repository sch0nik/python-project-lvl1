"""
Игра проверка числа, простое ли оно.

Пользователь должен сказать простое ли число.
"""

from brain_games.engine import execute
from brain_games.games.prime import generating_game_values


def main():
    """Тело игры."""
    execute(generating_game_values)


if __name__ == '__main__':
    main()

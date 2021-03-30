"""
Игра проверка числа, простое ли оно.

Пользователь должен сказать простое ли число.
"""

from brain_games.games.prime import game
from brain_games.scripts.engine import execute


def main():
    """Тело игры."""
    execute(game)


if __name__ == '__main__':
    main()

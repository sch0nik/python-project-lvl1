"""
Игра проверка числа, простое ли оно.

Пользователь должен сказать простое ли число.
"""

from brain_games.engine import execute
from brain_games.games import prime


def main():
    """Тело игры."""
    execute(prime)


if __name__ == '__main__':
    main()

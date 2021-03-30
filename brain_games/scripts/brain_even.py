"""
Скрипт для игры чет-нечет.

Игра спрашивает имя и задает число. Вам нужно ответить только 'yes' или 'no'.
"""

from brain_games.engine import execute
from brain_games.games import even


def main():
    """Вызов игры."""
    execute(even)


if __name__ == '__main__':
    main()

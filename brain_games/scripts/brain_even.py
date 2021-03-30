"""
Скрипт для игры чет-нечет.

Игра спрашивает имя и задает число. Вам нужно ответить только 'yes' или 'no'.
"""

from brain_games.games.even import game
from brain_games.scripts.engine import execute


def main():
    """Вызов игры."""
    execute(game)


if __name__ == '__main__':
    main()

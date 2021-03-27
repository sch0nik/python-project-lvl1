"""
Скрипт для игры чет-нечет.

Игра спрашивает имя и задает число. Вам нужно ответить только 'yes' или 'no'.
"""

from brain_games.games.even import game
from brain_games.scripts.engine import execution


def main():
    """Вызов игры."""
    execution(game)


if __name__ == '__main__':
    main()

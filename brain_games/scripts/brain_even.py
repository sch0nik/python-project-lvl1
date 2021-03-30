"""
Скрипт для игры чет-нечет.

Игра спрашивает имя и задает число. Вам нужно ответить только 'yes' или 'no'.
"""

from brain_games.games.even import generating_game_values
from brain_games.engine import execute


def main():
    """Вызов игры."""
    execute(generating_game_values)


if __name__ == '__main__':
    main()

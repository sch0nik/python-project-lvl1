"""
Скрипт для игры чет-нечет.

Игра спрашивает имя и задает число. Вам нужно ответить только 'yes' или 'no'.
"""

from brain_games.games.even import game
from scripts.engine import execution


def main():
    execution(game)


if __name__ == '__main__':
    main()

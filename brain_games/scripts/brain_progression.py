"""Скрипт запуска игры арифметическая прогрессия."""

from brain_games.engine import execute
from brain_games.games import progression


def main():
    """Тело игры."""
    execute(progression)


if __name__ == '__main__':
    main()

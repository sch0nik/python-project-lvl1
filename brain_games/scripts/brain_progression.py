"""Скрипт запуска игры арифметическая прогрессия."""

from brain_games.games.progression import game
from brain_games.scripts.engine import execute


def main():
    """Тело игры."""
    execute(game)


if __name__ == '__main__':
    main()

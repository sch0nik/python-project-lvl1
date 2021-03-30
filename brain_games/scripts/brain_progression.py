"""Скрипт запуска игры арифметическая прогрессия."""

from brain_games.games.progression import generating_game_values
from brain_games.engine import execute


def main():
    """Тело игры."""
    execute(generating_game_values)


if __name__ == '__main__':
    main()

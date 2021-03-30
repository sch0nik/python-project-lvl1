"""Игра наибольший общий делитель (НОД)."""

from brain_games.engine import execute
from brain_games.games import gcd


def main():
    """Тело игры."""
    execute(gcd)


if __name__ == '__main__':
    main()

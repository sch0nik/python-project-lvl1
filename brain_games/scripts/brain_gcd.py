"""Игра наибольший общий делитель (НОД)."""

from brain_games.cli import welcome_user
from brain_games.games.gcd import game
from scripts.engine import engine


def main():
    """Тело игры."""
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')

    if engine(game):
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()

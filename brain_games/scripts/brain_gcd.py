"""Игра наибольший общий делитель (НОД)."""

from prompt import string
from brain_games.games.gcd import game
from scripts.engine import engine


def main():
    """Тело игры."""
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')

    if engine(game):
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()

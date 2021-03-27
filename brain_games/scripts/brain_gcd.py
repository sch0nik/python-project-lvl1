"""Игра наибольший общий делитель (НОД)."""

from brain_games.games.gcd import game
from prompt import string
from scripts.engine import execution


def main():
    """Тело игры."""
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')

    if execution(game):
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()

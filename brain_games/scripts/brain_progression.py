"""Скрипт запуска игры арифметическая прогрессия."""

from prompt import string
from brain_games.games.progression import game
from scripts.engine import engine


def main():
    """Тело игры."""
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')

    if engine(game):
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()

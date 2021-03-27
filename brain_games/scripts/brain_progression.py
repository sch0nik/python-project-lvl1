"""Скрипт запуска игры арифметическая прогрессия."""

from brain_games.cli import welcome_user
from scripts.engine import engine
from brain_games.games.progression import game


def main():
    """Тело игры."""
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')

    if engine(game):
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()

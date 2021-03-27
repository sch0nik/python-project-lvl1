"""
Игра проверка числа, простое ли оно.

Пользователь должен сказать простое ли число.
"""

from prompt import string
from brain_games.games.prime import game
from scripts.engine import engine


def main():
    """Тело игры."""
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    if engine(game):
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()

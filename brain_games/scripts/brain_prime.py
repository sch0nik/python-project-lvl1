"""
Игра проверка числа, простое ли оно.

Пользователь должен сказать простое ли число.
"""

from brain_games.games.prime import game
from prompt import string
from brain_games.scripts.engine import execution


def main():
    """Тело игры."""
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    if execution(game):
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()

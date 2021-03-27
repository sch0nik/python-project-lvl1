"""
Игра калькулятор.

Пользователю предлагается решить простой пример.
"""

from prompt import string
from brain_games.games.calc import game
from scripts.engine import execution


def main():
    """Тело игры."""
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')

    if execution(game):
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()

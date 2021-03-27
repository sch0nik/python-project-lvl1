"""
Игра калькулятор.

Пользователю предлагается решить простой пример.
"""

from brain_games.cli import welcome_user
from brain_games.games.calc import game
from scripts.engine import engine


def main():
    """Тело игры."""
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(f'Hello, {name}!')
    print('What is the result of the expression?')

    if engine(game):
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()

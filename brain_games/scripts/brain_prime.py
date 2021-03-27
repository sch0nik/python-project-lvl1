"""
Игра проверка числа, простое ли оно.

Пользователь должен сказать простое ли число.
"""

from brain_games.cli import welcome_user
from scripts.engine import engine
from brain_games.games.prime import game


def main():
    """Тело игры."""
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    if engine(game):
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()

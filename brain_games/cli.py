"""
Модуль Cli.py. Пока только функция welcome_user().

welcome_user() - запрос, приветсвие и возврат имени пользователя.
"""

import prompt


def welcome_user():
    """Собственно сама функция.

    Returns:
        Возвращает имя пользователя.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

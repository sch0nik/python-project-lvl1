"""
Модуль Cli.py. Пока только функция welcom_user().

welcom_user() - запрос имени пользователя и приветсвие его по имени.
"""

import prompt


def welcom_user():
    """Запрос имени пользователя и приветсвие его по имени."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

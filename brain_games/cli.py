"""
Модуль Cli.py. Пока только функция welcom_user().

welcom_user() - запрос, приветсвие и возврат тмени пользователя.
"""

import prompt


def welcom_user():
    """Собственно сама функция.

    Returns:
        Возвращает имя пользователя.
    """
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

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
    return prompt.string('May I have your name? ')

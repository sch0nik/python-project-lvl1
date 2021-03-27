"""Главный элемент игры чет-нечет."""

from random import randint

from prompt import string


def game():
    """
    Сама игра.

    Функция придумывает число, показывает пользователю,
    и спрашивает ответ.

    Returns:
        True или False, в зависимости от ответа пользователя.
    """
    print('Answer "yes" if the number is even, otherwise answer "no".')

    number = randint(0, 1000)
    print(f'Question: {number}')
    return 'yes' if number % 2 == 0 else 'no'

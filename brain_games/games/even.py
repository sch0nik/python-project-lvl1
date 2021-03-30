"""Главный элемент игры чет-нечет."""

from random import randint

RULES_OF_THE_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def generating_game_values():
    """
    Сама игра.

    Функция придумывает число, показывает пользователю,
    и спрашивает ответ.

    Returns:
        Возвращает вопрос и верный результат.
    """
    number = randint(0, 1000)

    return (
        f'Question: {number}',
        'yes' if number % 2 == 0 else 'no',
    )

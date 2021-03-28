"""Главный элемент игры чет-нечет."""

from random import randint


def game():
    """
    Сама игра.

    Функция придумывает число, показывает пользователю,
    и спрашивает ответ.

    Returns:
        Возвращает условие игры, вопрос и верный результат.
    """
    number = randint(0, 1000)

    return (
        'Answer "yes" if the number is even, otherwise answer "no".',
        f'Question: {number}',
        'yes' if number % 2 == 0 else 'no',
    )

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
    condition = 'Answer "yes" if the number is even, otherwise answer "no".'

    number = randint(0, 1000)
    question = f'Question: {number}'
    expected = 'yes' if number % 2 == 0 else 'no'
    return condition, question, expected

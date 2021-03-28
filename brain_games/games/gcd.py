"""Игра НОД."""

from random import randint


def game():
    """
    Игровой процесс.

    Returns:
        Возвращает условие игры, вопрос и верный результат.
    """
    condition = 'Find the greatest common divisor of given numbers.'
    number_a = randint(1, 100)
    number_b = randint(1, 100)
    question = f'Question: {number_a} {number_b}'
    while number_a != 0 and number_b != 0:
        if number_a > number_b:
            number_a %= number_b
        else:
            number_b %= number_a

    return condition, question, str(number_a + number_b)

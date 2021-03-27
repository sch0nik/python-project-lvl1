"""Игра НОД."""

from random import randint


def game():
    """
    Игровой процесс.

    Returns:
        True или False, в зависимости от ответа пользователя.
    """
    print('Find the greatest common divisor of given numbers.')
    number_a = randint(1, 100)
    number_b = randint(1, 100)
    print(f'Question: {number_a} {number_b}')
    while number_a != 0 and number_b != 0:
        if number_a > number_b:
            number_a %= number_b
        else:
            number_b %= number_a

    return str(number_a + number_b)

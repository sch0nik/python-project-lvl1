"""Игра НОД."""

from random import randint

RULES_OF_THE_GAME = 'Find the greatest common divisor of given numbers.'


def getting_the_gcd(number_a, number_b):
    """
    Получение НОД.

    Args:
        number_a: целое число
        number_b: целое число

    Returns:
        Возвращает НОД
    """
    while number_a != 0 and number_b != 0:
        if number_a > number_b:
            number_a %= number_b
        else:
            number_b %= number_a

    return number_a + number_b


def generate_game_values():
    """
    Игровой процесс.

    Returns:
        Возвращает вопрос и верный результат.
    """
    number_a = randint(1, 100)
    number_b = randint(1, 100)
    question = f'Question: {number_a} {number_b}'

    return (
        question,
        str(getting_the_gcd(number_a, number_b)),
    )

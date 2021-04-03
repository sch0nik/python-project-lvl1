"""Главный элемент игры Calc."""

from random import choice, randint

RULES_OF_THE_GAME = 'What is the result of the expression?'


def calculating(number_a, number_b, operator):
    """ВЫчисление значения в зависимости от оператора.

    Args:
        number_a: целое число.
        number_b: целое число.
        operator: символ арифметической операции.

    Returns:
        Рзультат вычисления.
    """
    if operator == '+':
        return number_a + number_b
    elif operator == '-':
        return number_a - number_b
    return number_a * number_b


def generate_game_values():
    """
    Игра Calc.

    Случайным образом выбираются два числа и арифметическое действие.
    Пользователю нужно решить получившийся пример.

    Returns:
        Возвращает вопрос и верный результат.
    """
    number_a = randint(0, 100)
    number_b = randint(0, 100)
    operator = choice('+-*')
    expected = calculating(number_a, number_b, operator)

    return (
        f'Question: {number_a} {operator} {number_b}',
        str(expected),
    )

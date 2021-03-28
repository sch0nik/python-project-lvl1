"""Главный элемент игры Calc."""

from random import choice, randint


def game():
    """
    Игра Calc.

    Случайным образом выбираются два числа и арифметическое действие.
    Пользователю нужно решить получившийся пример.

    Returns:
        Возвращает условие игры, вопрос и верный результат.
    """
    number_a = randint(0, 100)
    number_b = randint(0, 100)
    operator = choice('+-*')
    if operator == '+':
        expected = number_a + number_b
    elif operator == '-':
        expected = number_a - number_b
    else:
        expected = number_a * number_b

    return (
        'What is the result of the expression?',
        f'Question: {number_a} {operator} {number_b}',
        str(expected),
    )

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
    condition = 'What is the result of the expression?'

    number_a = randint(0, 100)
    number_b = randint(0, 100)
    operator = choice('+-*')
    question = f'Question: {number_a} {operator} {number_b}'
    if operator == '+':
        expected = number_a + number_b
    elif operator == '-':
        expected = number_a - number_b
    else:
        expected = number_a * number_b

    return condition, question, str(expected)

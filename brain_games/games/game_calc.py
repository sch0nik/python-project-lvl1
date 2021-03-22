"""Главный элемент игры Calc."""

from random import randint

from prompt import string


def game():
    """
    Игра Calc.

    Случайным образом выбираются два числа и арифметическое действие.
    Пользователю нужно решить получившийся пример.

    Returns:
        Возвращает True или False,
        в зависимости оттого, правильно ли решен пример.
    """
    number_a = randint(0, 100)
    number_b = randint(0, 100)
    operator = '+-*'[randint(0, 2)]
    print(f'Question: {number_a} {operator} {number_b}')
    if operator == '+':
        right_answer = number_a + number_b
    elif operator == '-':
        right_answer = number_a - number_b
    else:
        right_answer = number_a * number_b

    answer = string('Your answer: ')
    if answer == str(right_answer):
        print('Correct!')
        return True
    else:
        print(f'{answer} is wrong answer ;(. Correct answer was {right_answer}.')
    return False

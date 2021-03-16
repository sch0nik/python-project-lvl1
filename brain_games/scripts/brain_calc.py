"""
Игра калькулятор.

Пользователю предлагается решить простой пример.
Арифметические операции: +, - и *.
"""

from random import randint

from prompt import string


def calc(operator, number_a, number_b):
    """
    Получение результата вычислений.

    Args:
        operator: символ оператора в виде строки.
        number_a: целое число.
        number_b: целое число.
    Returns:
        результат вычисления, в зависимости от operator.
    """
    print(f'Question: {number_a} {operator} {number_b}')
    if operator == '+':
        return number_a + number_b
    elif operator == '-':
        return number_a - number_b
    return number_a * number_b


def compare(right_answer):
    """
    Получение ответа пользователя и сравнение его с текущим.

    Args:
        right_answer: integer number
    Returns:
        True или False в зависимости от результата
    """
    answer = string('Your answer: ')
    if answer == str(right_answer):
        return True
    answer = f'{answer} is wrong answer ;(. Correct answer was {right_answer}.'
    print(answer)
    return False


def main():
    """Тело игры."""
    print('Welcome to the Brain Games!')
    # запрос имени, приветсвие и правила игры
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')

    current_round = 1

    while current_round <= 3:
        operator = '+-*'[randint(0, 2)]
        right_answer = calc(operator, randint(0, 100), randint(0, 100))

        if compare(right_answer):
            print('Correct!')
            current_round += 1
        else:
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

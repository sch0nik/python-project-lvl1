"""Игра простое ли число."""

from random import randint

from prompt import string


def game():
    """
    Игровой процесс.

    Берется случайное число. И спрашивается у пользователя
    простое ли оно?

    Returns:
        True или False, в зависимости от ответа пользователя.
    """
    number = randint(1, 1000)
    print(f'Question: {number}')

    # Числа есть простые и составные. У любого составного числа
    # есть собственный (то есть не равный 1) делитель,
    # не превосходящий квадратного корня из числа.
    # Этот цикл заканчивает работу либо при нахождении делителя,
    # либо если проверяемый делитель станет больше корня из number.
    # Число number будет простым, если цикл закончился по причине того,
    # что проверяемый делитель стал больше, чем корень из number.
    # А еще сразу отбрасываем четные числа.
    if number % 2 == 0:
        right_answer = 'no'
    else:
        count = 3
        while count * count <= number and number % count != 0:
            count += 2
        right_answer = 'yes' if count * count > number else 'no'

    answer = string('Your answer: ')
    if answer == right_answer:
        return True
    print(f'{answer} is wrong answer ;(. Correct answer was {right_answer}.')
    return False

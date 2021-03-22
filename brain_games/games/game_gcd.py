"""Игра НОД."""

from random import randint

from prompt import string


def game():
    """
    Игровой процесс.

    Returns:
        True или False, в зависимости от ответа пользователя.
    """
    number_a = randint(1, 100)
    number_b = randint(1, 100)
    print(f'Question: {number_a} {number_b}')
    while number_a != 0 and number_b != 0:
        if number_a > number_b:
            number_a %= number_b
        else:
            number_b %= number_a
    right_answer = number_a + number_b

    answer = string('Your answer: ')
    if answer == str(right_answer):
        print('Correct!')
        return True
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
    return False

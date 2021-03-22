"""Главный элемент игры чет-нечет."""

from random import randint

from prompt import string


def game():
    """
    Сама игра.

    Функция придумывает число, показывает пользователю,
    и спрашивает ответ.

    Returns:
        True или False, в зависимости от ответа пользователя.
    """
    number = randint(0, 1000)
    right_answer = 'yes' if number % 2 == 0 else 'no'
    print(f'Question: {number}')
    answer = string('Your answer: ')
    if answer == right_answer:
        print('Correct!')
        return True
    else:
        print(f'{answer} is wrong answer ;(. Correct answer was {right_answer}.')
    return False

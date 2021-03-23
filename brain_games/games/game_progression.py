"""Игровой процесс игры арифметическая прогрессия."""

from random import randint

from prompt import string


def game():
    """
    Игровой процесс.

    Придумывается арифметическая прогрессия.
    Выводится на экран без одного члена.
    Нужно узнать его.

    Returns:
        True или False, в зависимости от ответа пользователя.
    """
    number_of_elements = 5 + randint(1, 5)
    diff = randint(1, 10)
    secret_item = randint(0, number_of_elements - 1)
    right_answer = 0
    count = 0
    current_element = randint(0, 10)
    arithmetic = ''

    # Генерирование прогрессиии
    while count < number_of_elements:
        if count == secret_item:
            arithmetic = f'{arithmetic}..'
            right_answer = current_element
        else:
            arithmetic = f'{arithmetic}{current_element}'
        # это пробелы между числами,
        # если последний элемент, то пробел не будет ставится
        if count != number_of_elements - 1:
            arithmetic = f'{arithmetic} '
        count += 1
        current_element += diff

    print(arithmetic)
    answer = string('Your answer: ')
    if answer == str(right_answer):
        print('Correct!')
        return True
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
    return False

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
    number_of_elements = 5 + randint(0, 5)
    diff = randint(1, 10)
    secret_item = randint(0, number_of_elements - 1)
    current_element = randint(0, 10)
    arithmetic = ''
    expected = 0

    # Генерирование прогрессиии
    count = 0
    while count < number_of_elements:
        if count == secret_item:
            arithmetic = f'{arithmetic}..'
            expected = current_element
        else:
            arithmetic = f'{arithmetic}{current_element}'
        # это пробелы между числами,
        # если последний элемент, то пробел не будет ставится
        if count != number_of_elements - 1:
            arithmetic = f'{arithmetic} '
        count += 1
        current_element += diff

    print(f'Question: {arithmetic}')
    answer = string('Your answer: ')
    if answer == str(expected):
        print('Correct!')
        return True
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{expected}'.")
    return False
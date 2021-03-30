"""Игровой процесс игры арифметическая прогрессия."""

from random import randint

RULES_OF_THE_GAME = 'What number is missing in the progression?'


def generating_progression():
    """
    Генерироване арифметической прогрессии.

    Returns:
        Возвращает список с арифметической прогрессией.
    """
    number_of_elements = randint(5, 10)
    diff = randint(1, 10)
    arithmetic = [randint(1, 10)]

    for index in range(number_of_elements):
        if index == 0:
            continue
        arithmetic.append(arithmetic[index - 1] + diff)

    return arithmetic


def generating_game_values():
    """
    Игровой процесс.

    Придумывается арифметическая прогрессия.
    Выводится на экран без одного члена.
    Нужно узнать его.

    Returns:
        Возвращает вопрос и верный результат.
    """
    arithmetic = generating_progression()

    secret_index = randint(0, len(arithmetic) - 1)

    # Получение строки с прогрессией
    arithmetic = list(map(str, arithmetic))

    # И замена секретного элемента на ".."
    string_progression = ' '.join(arithmetic[:secret_index])
    string_progression = f'{string_progression} .. '

    temp_str = ' '.join(arithmetic[secret_index + 1:])
    string_progression = f'{string_progression}{temp_str}'

    return (
        f'Question: {string_progression}',
        arithmetic[secret_index],
    )

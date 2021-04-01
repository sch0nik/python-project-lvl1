"""Игровой процесс игры арифметическая прогрессия."""

from random import randint

RULES_OF_THE_GAME = 'What number is missing in the progression?'


def generate_progression():
    """
    Генерироване арифметической прогрессии.

    Returns:
        Возвращает список с арифметической прогрессией.
    """
    number_of_elements = randint(5, 10)
    diff = randint(1, 10)
    arithmetic = []

    for index in range(number_of_elements):
        arithmetic.append(index * diff + diff)

    return arithmetic


def generate_game_values():
    """
    Игровой процесс.

    Придумывается арифметическая прогрессия.
    Выводится на экран без одного члена.
    Нужно узнать его.

    Returns:
        Возвращает вопрос и верный результат.
    """
    arithmetic = generate_progression()

    secret_index = randint(0, len(arithmetic) - 1)

    # Получение строки с прогрессией
    arithmetic = list(map(str, arithmetic))

    # правильный ответ
    expected = arithmetic[secret_index]

    # И замена секретного элемента на ".."
    arithmetic[secret_index] = '..'
    ' '.join(arithmetic)  # noqa: WPS326

    return (
        f'Question: {arithmetic}',
        expected,
    )

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
    progression = generate_progression()

    secret_index = randint(0, len(progression) - 1)

    # Получение строки с прогрессией
    progression = list(map(str, progression))

    # правильный ответ
    expected = progression[secret_index]

    # И замена секретного элемента на ".."
    progression[secret_index] = '..'
    question = ' '.join(progression)

    return (
        question,
        expected,
    )

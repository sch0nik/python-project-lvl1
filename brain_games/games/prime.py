"""Игра простое ли число."""

from random import randint

RULES_OF_THE_GAME = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)


def generating_game_values():
    """
    Игровой процесс.

    Берется случайное число. И спрашивается у пользователя
    простое ли оно?

    Returns:
        Возвращает условие игры, вопрос и верный результат.
    """
    number = randint(1, 1000)
    question = f'Question: {number}'

    # Числа есть простые и составные. У любого составного числа
    # есть собственный (то есть не равный 1) делитель,
    # не превосходящий квадратного корня из числа.
    # Этот цикл заканчивает работу либо при нахождении делителя,
    # либо если проверяемый делитель станет больше корня из number.
    # Число number будет простым, если цикл закончился по причине того,
    # что проверяемый делитель стал больше, чем корень из number.
    # А еще сразу отбрасываем четные числа.
    if number % 2 == 0:
        return question, 'no'
    count = 3
    while count * count <= number and number % count != 0:
        count += 2
    expected = 'yes' if count * count > number else 'no'

    return question, expected

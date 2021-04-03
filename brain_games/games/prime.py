"""Игра простое ли число."""

from random import randint

RULES_OF_THE_GAME = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)


def is_prime(number):
    """
    Проверка простое ли число.

    Числа есть простые и составные. У любого составного числа
    есть собственный (то есть не равный 1) делитель,
    не превосходящий квадратного корня из числа.
    Этот цикл заканчивает работу либо при нахождении делителя,
    либо если проверяемый делитель станет больше корня из number.
    Число number будет простым, если цикл закончился по причине того,
    что проверяемый делитель стал больше, чем корень из number.
    А еще сразу отбрасываем четные числа.

    Args:
        number: целое число

    Returns:
        True или False, в зависимоости от результата.
    """
    # Отсекаются отрицательные числа, 0 и 1
    if number % 2 == 0 or number < 2:
        return False

    # 2 тоже простое число
    if number == 2:
        return True

    count = 3
    while count * count <= number and number % count != 0:
        count += 2

    return count * count > number


def generate_game_values():
    """
    Игровой процесс.

    Берется случайное число. И спрашивается у пользователя
    простое ли оно?

    Returns:
        Возвращает строу с числом и верный ответ.
    """
    number = randint(1, 1000)

    return str(number), 'yes' if is_prime(number) else 'no'

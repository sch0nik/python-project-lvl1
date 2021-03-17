"""
Игра проверка числа, простое ли оно.

Пользователь должен сказать простое ли число.
"""

from random import randint

from prompt import string


def calc():
    """
    Получение результата вычислений.

    Returns:
        Возвращает правильный ответ.
    """
    number = randint(1, 1000)
    print(f'Question: {number}')

    # Числа есть простые и составные. У любого составного числа
    # есть собственный (то есть не равный 1) делитель,
    # не превосходящий квадратного корня из числа.
    # Этот цикл заканчивает работу либо при нахождении делителя,
    # либо если проверяемый делитель станет больше корня из number.
    # Чиcло number будет простым, если цикл закончился по причине того,
    # что проверяемый делитель стал больше, чем корень из number.
    # А еще сразу отбрасываем четные числа.
    if number % 2 == 0:
        return 'no'
    count = 3
    while count * count <= number and number % count != 0:
        count += 2

    return 'yes' if count * count > number else 'no'


def compare(right_answer):
    """
    Получение ответа пользователя и сравнение его с текущим.

    Args:
        right_answer: правильный ответ

    Returns:
        True или False в зависимости от результата
    """
    answer = string('Your answer: ')
    if answer == str(right_answer):
        return True
    answer = f'{answer} is wrong answer ;(. Correct answer was {right_answer}.'
    print(answer)
    return False


def main():
    """Тело игры."""
    print('Welcome to the Brain Games!')
    # запрос имени, приветсвие и правила игры
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    current_round = 1

    while current_round <= 3:
        if compare(calc()):
            print('Correct!')
            current_round += 1
        else:
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

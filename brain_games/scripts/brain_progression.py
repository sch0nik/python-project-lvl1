"""
Игра арифметическая прогрессия.

calc() - подсчет значений.
Пользователю предлагается найти скрытый член арифметической прогрессии.
"""

from random import randint

from prompt import string


def calc():
    """
    Получение результата вычислений.

    Returns:
        Возвращает скрытый член арифметической прогрессии.
    """
    # прогрессия будет храниться в виде списка
    arithmetic = []
    count = 1
    end = randint(4, 9)
    # первый член прогрессии находим случайным образом
    arithmetic.append(randint(0, 10))
    # разность прогрессии
    diff = randint(1, 10)
    # заполнение
    while count <= end:
        arithmetic.append(arithmetic[count - 1] + diff)
        count += 1

    count = 0
    arithmetic_str = ''
    # индекс последнего элемента
    end = len(arithmetic) - 1
    secret_i = randint(0, end)
    # логика такая, в цикле добавляю каждый элемент к строке,
    # а секретный заменяю точками
    while count <= end:
        if count == secret_i:
            arithmetic_str = f'{arithmetic_str}..'
        else:
            arithmetic_str = f'{arithmetic_str}{arithmetic[count]}'
        # это пробелы между числами,
        # если последний элемент, то пробел не будет ставится
        if count != end:
            arithmetic_str = f'{arithmetic_str} '
        count += 1

    print(f'Question: {arithmetic_str}')

    return arithmetic[secret_i]


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
    print('What is the result of the expression?')

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

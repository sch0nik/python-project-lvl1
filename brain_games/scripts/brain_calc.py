"""
Игра калькулятор.

Пользователю предлагается решить простой пример.
Арифметические операции: +, - и *.
"""

from random import randint

from prompt import string


def main():
    """Тело игры. Здесь всего одна функция."""
    print('Welcome to the Brain Games!')
    # запрос имени, приветсвие и правила игры
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')

    current_round = 1
    right_answer = 0
    answer = ''

    while current_round <= 3:
        operator = '+-*'
        number_a = randint(0, 100)
        number_b = randint(0, 100)
        operator = operator[randint(0, 2)]

        if operator == '+':
            right_answer = number_a + number_b
        elif operator == '-':
            right_answer = number_a - number_b
        else:
            right_answer = number_a * number_b

        print(f'Question: {number_a} {operator} {number_b}')

        answer = string('Your answer: ')
        if answer == str(right_answer):
            print('Correct!')
            current_round += 1
        else:
            current_round = -1
            break

    answer = f'{answer} is wrong answer ;(. Correct answer was {right_answer}.'
    if current_round == -1:
        print(answer)
        print(f"Let's try again, {name}!")
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

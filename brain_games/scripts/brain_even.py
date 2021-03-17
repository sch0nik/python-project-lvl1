"""
Скрипт для игры чет-нечет.

Игра спрашивает имя и задает число. Вам нужно ответить только 'yes' или 'no'.
"""

from random import randint

from prompt import string


def main():
    """Тело игры. Здесь всего одна функция."""
    print('Welcome to the Brain Games!')
    # запрос имени, приветсвие и правила игры
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    current_round = 1

    while current_round <= 3:
        number = randint(0, 1000)
        right_answer = 'yes' if number % 2 == 0 else 'no'
        print(f'Question: {number}')

        answer = string('Your answer: ')
        if answer == right_answer:
            print('Correct!')
            current_round += 1
        else:
            current_round = -1
            break
    answer = f'{answer} is wrong answer ;(. Correct answer was {right_answer}.'
    if current_round == -1:
        print(answer)
        print(f"Let's try again, {name}!")
        print(f"Let's try again, {name}")
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

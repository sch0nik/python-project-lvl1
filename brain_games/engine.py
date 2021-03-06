"""
Игровой движок.

Общая игровая логика.
NUMBER_OF_ROUNDS - количество победных раундов подряд.
"""

from prompt import string

# Количество победных раундов подряд, чтобы выиграть всю игру
NUMBER_OF_ROUNDS = 3


def execute(game):
    """
    Сам движок.

    Принимает игровую функцию. Получает от нее ответ.

    Args:
        game: функция игрового процесса
    """
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES_OF_THE_GAME)

    current_round = 0
    while current_round < NUMBER_OF_ROUNDS:
        question, expected = game.generate_game_values()
        print(f'Question: {question}')

        answer = string('Your answer: ')
        if answer == expected:
            current_round += 1
            print('Correct!')
        else:
            print(
                f'{answer} is wrong answer ;(. Correct answer was {expected}.',
            )
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')

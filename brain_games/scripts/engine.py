"""
Игровой движок.

Общая игровая логика.
NUMBER_OF_RAUNDS - количество победных раундов подряд.
"""


# Количество победных раундов подряд, чтобы выиграть всю игру
NUMBER_OF_RAUNDS = 3


def execution(game):
    """
    Сам движок.

    Принимает игровую функцию. Получает от нее ответ.

    Args:
        game: функция игрового процесса

    Returns:
        True или False в зависимости от результата
    """
    current_round = 0
    while current_round < NUMBER_OF_RAUNDS:
        if game():
            current_round += 1
        else:
            break

    return current_round == NUMBER_OF_RAUNDS

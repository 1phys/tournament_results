"""
Агент, который делает случайный выбор между "Камнем", "Бумагой" и "Ножницами".
"""

import random

def random_agent(observation, configuration):
    """
    Возвращает случайное действие: "Камень", "Бумага" или "Ножницы".

    Параметры:
    observation (dict): Наблюдение о текущем состоянии игры.
    configuration (dict): Конфигурация игры.

    Возвращает:
    int: 0, 1 или 2 - "Камень", "Бумага" или "Ножницы"
    """
    return random.randint(0, 2)

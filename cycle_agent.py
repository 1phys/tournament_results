"""
Агент, который циклично выбирает действия: "Камень", "Бумага", "Ножницы".
"""

def cycle_agent(observation, configuration):
    """
    Выбирает действие по циклу: 0 -> 1 -> 2 (Камень -> Бумага -> Ножницы).

    Параметры:
    observation (dict): Наблюдение о текущем состоянии игры.
    configuration (dict): Конфигурация игры.

    Возвращает:
    int: Действие в зависимости от шага игры
    """
    return (observation.step % 3)  # Меняет выбор по циклу

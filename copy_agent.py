def copy_agent(observation, configuration):
    if observation.step > 0:
        return observation.lastOpponentAction  # Копирует ход противника
    return 0  # На первом шаге выбирает "Камень"
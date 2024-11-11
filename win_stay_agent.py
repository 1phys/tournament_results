
def win_stay_agent(observation, configuration):
    if observation.step == 0:
        return 0  # На первом шаге выбирает "Камень"
    if observation.reward > 0:
        return observation.lastOpponentAction  # Если выиграл, выбирает то же действие
    return (observation.lastOpponentAction + 1) % 3  # Иначе выбирает следующее по циклу


def counter_previous_agent(observation, configuration):
    if observation.step > 0:
        return (observation.lastOpponentAction + 1) % 3
    return 0  # На первом шаге выбирает "Камень"

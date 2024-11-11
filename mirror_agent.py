# выбирает то же самое, что противник выбрал на прошлом шаге.
def mirror_agent(observation, configuration):
    if observation.step > 0:
        return observation.lastOpponentAction
    return 1  # Начинает с "Бумаги"

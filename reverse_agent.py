#выбирает противоположное действие последнему своему выбору
def reverse_agent(observation, configuration):
    if observation.step == 0:
        return 0  # Начинает с "Камня"
    return (observation.lastOpponentAction + 2) % 3  # Меняет выбор на противоположное

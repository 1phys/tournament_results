
def least_common_agent(observation, configuration):
    if observation.step == 0:
        return 0  # На первом шаге выбирает "Камень"
    count = [0, 0, 0]
    for step in observation["steps"]:
        count[step[1]["action"]] += 1
    return count.index(min(count))  # Выбирает наименее используемое противником действие

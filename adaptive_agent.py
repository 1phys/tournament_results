#запоминает, что чаще всего выбирает противник, и адаптируется.
def adaptive_agent(observation, configuration):
    if observation.step == 0:
        return 0  # Начинает с "Камня"
    history = observation["steps"]
    count = [0, 0, 0]
    for step in history:
        count[step[1]["action"]] += 1
    most_common = count.index(max(count))
    return (most_common + 1) % 3  # Выбирает действие, которое побеждает самое частое

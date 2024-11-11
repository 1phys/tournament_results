# выбирает действие случайным образом, но чаще выбирает "Камень"
import random
def random_biased_agent(observation, configuration):
    return random.choices([0, 1, 2], weights=[0.5, 0.25, 0.25])[0]

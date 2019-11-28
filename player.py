import random


class MachinePlayer:
    def __init__(self):
        return

    def play(self, avilableCol: list):
        return random.choice(avilableCol)


class HumanPlayer:
    def __init__(self):
        return

    def play(self, avilableCol: list):
        print('select column to insert coin\navailable columns: {0}'.format(*avilableCol))

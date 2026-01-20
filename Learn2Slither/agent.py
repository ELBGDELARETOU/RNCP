from random import choice

class RandomAgent:
    def get_action(self, state):
        return choice([0,1,2])
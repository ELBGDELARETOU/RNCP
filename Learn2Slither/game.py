from random import randrange

class SnakeGame:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.reset()

def reset(self):
    self.snake = [(5,5), (4,5)]
    self.direction = (1,0)
    self.g_apple = (randrange(self.width),randrange(self.height))
    self.r_apple = (randrange(self.width),randrange(self.height))
    self.score = 0
    self.game_over = False

    
from random import randrange

class SnakeGame:
    def __init__(self):
        self.width = 10
        self.height = 10
        self._reset()

    def _place_green_apple(self):
        self.g_apple = (randrange(self.width), randrange(self.height))
        while self.g_apple in self.snake or getattr(self, 'r_apple', None) == self.g_apple:
            self.g_apple = (randrange(self.width), randrange(self.height))

    def _place_red_apple(self):
        self.r_apple = (randrange(self.width), randrange(self.height))
        while self.r_apple in self.snake or getattr(self, 'g_apple', None) == self.r_apple:
            self.r_apple = (randrange(self.width), randrange(self.height))

    def _reset(self):
        self.snake = [(5,5), (4,5)]
        self.direction = (1,0)

        self._place_green_apple()
        self._place_red_apple()

        self.score = 0
        self.game_over = False


    def _update_direction(self, action):
        dx, dy = self.direction

        if(action == 0):
            pass
        elif(action == 1):
            self.direction = (dy, -dx)
        else:
            self.direction = (-dy, dx)

    def _move(self):
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        self.snake.insert(0, new_head)



    def _get_state(self):
        return {
            'snake': self.snake,
            'green_apple': self.g_apple,
            'red_apple': self.r_apple,
            'direction': self.direction
        }

    def _check_collision(self):
        head_x, head_y = self.snake[0]

        if head_x < 0 or head_x >= self.width:
            return True
        if head_y < 0 or head_y >= self.height:
            return True
        if self.snake[0] in self.snake[1:]:
            return True
        return False


    def step(self, action):

        self._update_direction(action)
        self._move()

        if self._check_collision():
            self.game_over = True
            reward = -10
            return self._get_state(), reward, True

        reward = -0.01
        head = self.snake[0]

        if head == self.g_apple:
            self._place_green_apple()
            self.score += 1
            reward = 10

        elif head == self.r_apple:
            self._place_red_apple()
            self.score -= 1
            reward = -10

            self.snake.pop()
            if len(self.snake) > 0:
                self.snake.pop()
            else:
                self.game_over = True
                return self._get_state(), reward, self.game_over
        else:
            self.snake.pop()

        return self._get_state(), reward, self.game_over



game = SnakeGame()
print("Etat initial:", game._get_state())

for i in range(5):
    state, reward, done = game.step(0)
    print(f"Step {i}: Score={game.score}, Reward={reward}, Done={done}")
    if done:
        break
print("Etat initial:", game._get_state())

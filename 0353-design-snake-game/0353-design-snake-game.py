from collections import deque

class SnakeGame:

    def __init__(self, width: int, height: int, food: list[list[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.food_index = 0

        self.snake = deque([(0, 0)])  # initial position
        self.snake_set = set([(0, 0)])  # for O(1) collision check

        self.directions = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1)
        }

    def move(self, direction: str) -> int:
        head_row, head_col = self.snake[-1]
        delta_row, delta_col = self.directions[direction]
        new_head = (head_row + delta_row, head_col + delta_col)

        # Check wall collision
        if not (0 <= new_head[0] < self.height and 0 <= new_head[1] < self.width):
            return -1

        # Check if eating food
        if (self.food_index < len(self.food) and 
            [new_head[0], new_head[1]] == self.food[self.food_index]):
            self.food_index += 1
        else:
            tail = self.snake.popleft()
            self.snake_set.remove(tail)

        # Check self collision
        if new_head in self.snake_set:
            return -1

        self.snake.append(new_head)
        self.snake_set.add(new_head)

        return self.food_index
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
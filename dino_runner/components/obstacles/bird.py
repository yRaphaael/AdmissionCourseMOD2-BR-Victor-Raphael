import random

from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacles import Obstacle

class Bird(Obstacle):
    def __init__(self):
        self.step_index = 0
        super().__init__(BIRD, 0)
        self.rect.y = random.randint(200, 325)

    def draw(self, screen):
        if self.step_index >= 8: self.step_index = 0
        screen.blit(self.image[self.step_index//5], self.rect)
        self.step_index += 1
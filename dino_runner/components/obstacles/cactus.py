import random

from dino_runner.components.obstacles.obstacles import Obstacle


class Cactus(Obstacle):

    def __init__(self, image):
        self.size = random.randint(0, 1)
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325

        super().__init__(image[self.size], random.randint(0, 2))
        self.rect.y = self.verify()

    def verify(self):
        if self.size == 0:
            return 325
        else:
            return 300


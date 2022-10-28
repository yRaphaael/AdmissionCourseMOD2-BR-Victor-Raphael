from dino_runner.utils.constants import AKUMA, AKUMA_TYPE
from dino_runner.components.power_ups.power_up import PowerUp



class Akuma(PowerUp):
    def __init__(self):
        self.image = AKUMA
        self.type = AKUMA_TYPE
        super().__init__(self.image, self.type)
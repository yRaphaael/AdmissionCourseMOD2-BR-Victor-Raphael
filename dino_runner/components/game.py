from sys import implementation
import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS

from dino_runner.components.dinosaur import Dinosaur

class Game:
    def __init__(self):
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True

    def events(self):
        self.playing = False

    def update(self):
        pass
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.screen.fill((255, 255, 255)) # "#ffffff"
        self.draw_background()
        self.player.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

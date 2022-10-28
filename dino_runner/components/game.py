import pygame
from pygame import mixer
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.utils.constants import BG, DEFAULT_TYPE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, GAME_OVER, RESET, SNOWFALL
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.text_utils import draw_message_component

FONT_STYLE = "freesansbold.ttf"


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.music.load(SNOWFALL)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0
        self.death_count = 0
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.best_score = 0
    
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
                pygame.mixer.music.stop()
        pygame.display.quit()
        pygame.quit()


    def run(self):
        # Game loop: events - update - draw
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.5)
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        while self.playing:
            self.events()
            self.update()  
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
    
    
    def update(self):
        self.obstacle_manager.update(self)
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 2

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) #Também aceita código hexadecimal "#FFFFFF"
        self.draw_background()
        self.obstacle_manager.draw(self.screen)
        self.player.draw(self.screen)
        self.draw_power_up_time()
        self.draw_score()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render((f"Score: {self.score}"), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        if self.score > self.best_score:
                self.best_score = self.score
        self.screen.blit(text, text_rect)

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_message_component(
                    f"{self.player.type.capitalize()} enabled for {time_to_show} seconds",
                    self.screen,
                    font_size = 18,
                    pos_x_center = 500,
                    pos_y_center = 40
                )
            
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_message_component(
                    f"{self.player.type.capitalize()} enabled for {time_to_show} seconds",
                    self.screen,
                    font_size = 18,
                    pos_x_center = 500,
                    pos_y_center = 40
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE


    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if self.death_count > 0:
                    self.score = 0
                    self.game_speed = 20
                self.run()


    def configure_text_values(self, size, content, widht, height):
        font = pygame.font.Font(FONT_STYLE, size)
        text = font.render(content, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (widht, height)
        self.screen.blit(text, text_rect)

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        font = pygame.font.Font(FONT_STYLE, 22)

        if self.death_count == 0:
            draw_message_component("Press any key to start", self.screen)
        else:
            draw_message_component("Press any key to restart", self.screen)
            draw_message_component(f"Your Score: {self.score}", self.screen , 15, pos_y_center = half_screen_height +50)
            self.configure_text_values(22, f'Your best Score: {self.best_score}', half_screen_width, half_screen_height + 75)
            draw_message_component(f"Life lost: {self.death_count}", self.screen, 15, pos_y_center = half_screen_height +100)
            self.screen.blit(ICON, (half_screen_width -50, half_screen_height -200 ))
            self.screen.blit(GAME_OVER, (half_screen_width -200, half_screen_height -250 ))
            self.screen.blit(RESET, (half_screen_width -35, half_screen_height +200 ))

        pygame.display.flip()
        self.handle_events_on_menu()
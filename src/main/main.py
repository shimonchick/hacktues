import pygame
from time import time

from evdev import InputDevice, categorize, ecodes
from classes import player
from classes import projectile
from helpers.image_getter import get_image
from controller_config import *
from classes.direction import Direction


# set up gamepad
gamepad1 = InputDevice('/dev/input/event2')
# gamepad2 = InputDevice('/dev/input/event4')

# set up players
player1 = player.Player(50, 50, 'player.png')  
player2 = player.Player(45, 50, 'player.png')
projectiles = []

# main class
class App:
    def __init__(self):
        self._running = True
        self.screen = None
        self.size = self.weight, self.height = 640, 400
        self.clock = None

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.SRCALPHA)
        self._running = True
        self.clock = pygame.time.Clock()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.code == c1_down_btn:
            player1.move(Direction.DOWN)
        if event.code == c1_up_btn:
            player1.move(Direction.UP)
        if event.code == c1_left_btn:
            player1.move(Direction.LEFT)
        if event.code == c1_right_btn:
            player1.move(Direction.RIGHT)
        # player 2 buttons :

        if event.code == c2_down_btn:
            player2.move(Direction.DOWN)
        if event.code == c2_up_btn:
            player2.move(Direction.UP)
        if event.code == c2_left_btn:
            player2.move(Direction.LEFT)
        if event.code == c2_right_btn:
            player2.move(Direction.RIGHT)

        if event.code == c1_r1:
            projectile = player1.shoot()
            projectiles.append(projectile)

    def loop(self):
        self.clock.tick(60)

    def render(self):
        self.screen.blit(get_image(player1.image_filepath), (player1.x, player1.y))
        self.screen.blit(get_image(player2.image_filepath), (player2.x, player2.y))

        for prj in projectiles:
            self.screen.blit(get_image(prj.image_filepath), (prj.x, prj.y))

        pygame.display.flip()

    def cleanup(self):
        pygame.quit()

    def execute(self):
        if self.on_init() == False:
            self._running = False

        self.screen.fill((255, 255, 255))
        self.render()
        current = time()
        for event1 in gamepad1.read_loop():
            if not self._running:
                break
            previous_time = current_time
            current_time = time()
            time_delta = current_time - previous_time 

            for prj in projectiles:
                prj.move(time_delta)

            if event1.type == ecodes.EV_KEY:
                self.on_event(event1)
            self.loop()
            self.render()
            self.screen.fill((255, 255, 255))
        self.cleanup()

        """
        self.screen.fill((255, 255, 255))
        self.render()
        for event1, event2 in zip(gamepad1.read_loop(), gamepad2.read_loop()):
            if not self._running:
                break

            if event1.type == ecodes.EV_KEY:
                self.on_event(event1)
            if event2.type == ecodes.EV_KEY:
                print(event2)
                self.on_event(event2)
            self.loop()
            self.render()
            self.screen.fill((255, 255, 255))
        self.cleanup()
        """


if __name__ == "__main__" :
    theApp = App()
    theApp.execute()


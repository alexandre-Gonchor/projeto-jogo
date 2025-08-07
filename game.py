import pygame

from Menu import Menu
from conts import win_width, win_height


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(win_width, win_height))

    def run(self ):
        pygame.mixer.music.load("./assets/sounds/Menu.mp3")
        pygame.mixer.music.play(-1)
        while True:
            menu = Menu(self.window)
            menu.run()
            pass














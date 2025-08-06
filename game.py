import pygame

from Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(576, 324))

    def run(self ):
        pygame.mixer.music.load("./asset/Menu.mp3")
        pygame.mixer.music.play(-1)
        while True:
            menu = Menu(self.window)
            menu.run()
            pass














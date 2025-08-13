import pygame
from Menu import Menu
from conts import win_width, win_height, menu_options
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(win_width, win_height))

    def run(self):
        pygame.mixer.music.load("./assets/sounds/Menu.mp3")
        pygame.mixer.music.play(-1)
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == menu_options[0]:  # New Game
                level = Level(self.window, 'level 1', menu_return)
                level.run()  # <-- chamando o jogo
            elif menu_return == menu_options[4]:  # Exit
                pygame.quit()
                quit()
            else:
                pass

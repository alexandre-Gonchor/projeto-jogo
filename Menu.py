

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from conts import menu_options, c_yellow, c_white


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/7 Levels/Preview/1lvl.jpg')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_op = 0
        pygame.mixer.music.load("./assets/sounds/Menu.mp3")
        pygame.mixer.music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=80,text='Jump', text_color=(255,128,0), text_center_pos=(self.rect.centerx, 70))
            self.menu_text(text_size=80,text='Test', text_color=(255,128,0), text_center_pos=(self.rect.centerx, 120))

            for i in range(len(menu_options)):
                if i == menu_op:
                     self.menu_text(60, menu_options[i], c_yellow, text_center_pos=(self.rect.centerx, 200 + 55 * i))
                else:
                     self.menu_text(60, menu_options[i], c_white, text_center_pos=(self.rect.centerx, 200 + 55 * i))
            pygame.display.flip()

            #checagem de eventos

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_op < len(menu_options) - 1:
                            menu_op += 1
                        else:
                            menu_op = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_op > 0:
                            menu_op -= 1
                        else:
                            menu_option = len(menu_options) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return menu_options[menu_op]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
        pass


import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
import conts


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/7 Levels/Preview/1lvl.jpg')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):

        pygame.mixer.music.load("./assets/sounds/Menu.mp3")
        pygame.mixer.music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=80,text='Jump', text_color=(255,128,0), text_center_pos=(self.rect.centerx, 70))
            self.menu_text(text_size=80,text='Test', text_color=(255,128,0), text_center_pos=(self.rect.centerx, 120))

            for i in range(len(conts.menu_options)):

                 self.menu_text(60, conts.menu_options[i], conts.c_yellow, text_center_pos=(self.rect.centerx, 200 + 55 * i))








            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
        pass

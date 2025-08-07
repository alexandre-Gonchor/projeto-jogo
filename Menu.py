import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from pygame.locals import K_UP, K_DOWN, K_RETURN, K_KP_ENTER, KEYDOWN

from conts import menu_options, c_yellow, c_white


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/7 Levels/Preview/1lvl.jpg')
        self.rect = self.surf.get_rect(left=0, top=0)
        pygame.mixer.music.load("./assets/sounds/Menu.mp3")
        self.selected_index = 0  # ← índice da opção selecionada

    def run(self):
        pygame.mixer.music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            # Títulos fixos
            center_x = self.rect.centerx
            headers = [('Jump', (255,128,0), 70), ('Test', (255,128,0), 120)]
            for text, color, y in headers:
                self.menu_text(80, text, color, (center_x, y))

            # Opções de menu com seleção
            for i, option in enumerate(menu_options):
                color = c_yellow if i == self.selected_index else c_white
                self.menu_text(60, option, color, (center_x, 200 + 55 * i))

            pygame.display.flip()

            # Processa eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                elif event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        self.selected_index = (self.selected_index + 1) % len(menu_options)
                    elif event.key == K_UP:
                        self.selected_index = (self.selected_index - 1) % len(menu_options)
                    elif event.key in (K_RETURN, K_KP_ENTER):
                        # Ação ao selecionar a opção (pode ser implementada)
                        print(f"Selecionado: {menu_options[self.selected_index]}")
                        # Aqui você pode chamar outra função ou trocar de tela

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

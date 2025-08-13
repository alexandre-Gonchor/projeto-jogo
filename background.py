# background.py
import pygame
from entity import Entity

class Background(Entity):
    def __init__(self, name: str, position=(0,0)):
        super().__init__(name, position)

    def move(self):
        pass  # O fundo não se move por enquanto

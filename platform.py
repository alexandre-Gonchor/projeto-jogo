# platform.py
from entity import Entity

class Platform(Entity):
    def __init__(self, name: str, position=(0, 0)):
        super().__init__(name, position)

    def move(self):
        pass

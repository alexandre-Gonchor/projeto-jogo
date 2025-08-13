# gem.py
from entity import Entity

class Gem(Entity):
    def __init__(self, position=(0, 0)):
        super().__init__('gem', position)  # precisa de assets/gem.png

    def move(self):
        pass

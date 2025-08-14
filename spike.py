from entity import Entity

class Spike(Entity):
    def __init__(self, position=(0, 0)):
        super().__init__('spike', position)  # precisa de assets/spike.png

    def move(self):
        pass

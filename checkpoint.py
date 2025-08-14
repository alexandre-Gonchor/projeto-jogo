from entity import Entity

class Checkpoint(Entity):
    def __init__(self, position=(0, 0)):
        super().__init__('checkpoint', position)  # precisa de assets/checkpoint.png

    def move(self):
        pass

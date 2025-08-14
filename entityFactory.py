from background import Background
from platform import Platform
from gem import Gem
from checkpoint import Checkpoint
from spike import Spike

class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'bg1':
                return [Background('bg1', position)]
            case 'platform1':
                return [Platform('platform', position)]
            case 'gem':
                return [Gem(position)]
            case 'checkpoint':
                return [Checkpoint(position)]
            case 'spike':
                return [Spike(position)]
            case _:
                return []

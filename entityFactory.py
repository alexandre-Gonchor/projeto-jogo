#!/usr/bin/python
# -*- coding: utf-8 -*-
from background import Background
from platform import Platform
from gem import Gem

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
            case _:
                return []

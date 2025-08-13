#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from entity import Entity
from entityFactory import EntityFactory
from player import Player

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []

        # Fundo
        self.entity_list.extend(EntityFactory.get_entity('bg1'))

        # Plataformas
        self.platforms = []
        self.platforms.extend(EntityFactory.get_entity('platform1', (100, 450)))
        self.platforms.extend(EntityFactory.get_entity('platform1', (200, 550)))
        self.platforms.extend(EntityFactory.get_entity('platform1', (400, 250)))

        # Gemas
        self.gems = []
        self.gems.extend(EntityFactory.get_entity('gem', (120, 300)))
        self.gems.extend(EntityFactory.get_entity('gem', (320, 200)))
        self.gems.extend(EntityFactory.get_entity('gem', (520, 100)))

        # Player
        self.player = Player(position=(100, 300))

        # Contador de gemas
        self.gem_count = 0
        self.font = pygame.font.SysFont("Lucida Sans Typewriter", 30)

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.player.update(keys, self.platforms)

            # Checar colisão com gemas
            for gem in self.gems[:]:
                if self.player.rect.colliderect(gem.rect):
                    self.gems.remove(gem)
                    self.gem_count += 1

            # Desenhar fundo
            for entity in self.entity_list:
                self.window.blit(entity.surf, entity.rect)

            # Desenhar plataformas
            for platform in self.platforms:
                self.window.blit(platform.surf, platform.rect)

            # Desenhar gemas
            for gem in self.gems:
                self.window.blit(gem.surf, gem.rect)

            # Desenhar player
            self.window.blit(self.player.surf, self.player.rect)

            # Contador de gemas
            gem_text = self.font.render(f"Gemas: {self.gem_count}", True, (255, 255, 0))
            self.window.blit(gem_text, (10, 10))

            pygame.display.flip()
            clock.tick(60)

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

        # Fundo
        self.background = EntityFactory.get_entity('bg1', (0, 0))[0]

        # Plataformas
        self.platforms = []
        ground = EntityFactory.get_entity('platform1', (0, 850))[0]
        ground.surf = pygame.Surface((1600, 50))
        ground.surf.fill((50, 200, 50))
        self.platforms.append(ground)

        # Plataformas elevadas
        self.platforms.extend(EntityFactory.get_entity('platform1', (100, 700)))
        self.platforms.extend(EntityFactory.get_entity('platform1', (250, 600)))
        self.platforms.extend(EntityFactory.get_entity('platform1', (270, 600)))
        self.platforms.extend(EntityFactory.get_entity('platform1', (350, 500)))
        self.platforms.extend(EntityFactory.get_entity('platform1', (370, 500)))

        # Gemas
        self.gems = []
        self.gems.extend(EntityFactory.get_entity('gem', (265, 500)))

        # Espinhos
        self.spikes = []
        self.spikes.extend(EntityFactory.get_entity('spike', (600, 820)))  # no chão
        self.spikes.extend(EntityFactory.get_entity('spike', (900, 820)))

        # Checkpoint
        self.checkpoint = EntityFactory.get_entity('checkpoint', (1450, 750))[0]

        # Player
        self.start_position = (100, 700)
        self.player = Player(position=self.start_position)

        # Contador de gemas
        self.gem_count = 0
        self.font = pygame.font.SysFont("Lucida Sans Typewriter", 30)

    def reset_player(self):
        """Reseta player para o início."""
        self.player.rect.topleft = self.start_position
        self.player.vel_x = 0
        self.player.vel_y = 0

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.player.update(keys, self.platforms)

            # Se sair da tela → reseta
            if (self.player.rect.top > 900 or
                self.player.rect.bottom < 0 or
                self.player.rect.right < 0 or
                self.player.rect.left > 1600):
                self.reset_player()

            # Colisão com espinhos → reseta
            for spike in self.spikes:
                if self.player.rect.colliderect(spike.rect):
                    print("💀 Morreu nos espinhos!")
                    self.reset_player()

            # Coletar gemas
            for gem in self.gems[:]:
                if self.player.rect.colliderect(gem.rect):
                    self.gems.remove(gem)
                    self.gem_count += 1

            # Checar checkpoint
            if self.player.rect.colliderect(self.checkpoint.rect):
                print("Fase concluída! 🎉")
                running = False

            # Desenhar
            self.window.blit(self.background.surf, self.background.rect)

            for platform in self.platforms:
                self.window.blit(platform.surf, platform.rect)

            for spike in self.spikes:
                self.window.blit(spike.surf, spike.rect)

            for gem in self.gems:
                self.window.blit(gem.surf, gem.rect)

            self.window.blit(self.checkpoint.surf, self.checkpoint.rect)
            self.window.blit(self.player.surf, self.player.rect)

            gem_text = self.font.render(f"Gemas: {self.gem_count}", True, (255, 255, 0))
            self.window.blit(gem_text, (10, 10))

            pygame.display.flip()
            clock.tick(60)

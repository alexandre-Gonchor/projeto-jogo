#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from entityFactory import EntityFactory
from player import Player
from terrain import Terrain

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode

        # fundo
        self.background = EntityFactory.get_entity('bg1', (0, 0))[0]

        # player
        self.start_position = (1290, 815)
        self.player = Player(position=self.start_position)

        # terreno geométrico
        self.terrain = Terrain()

        # --- plataformas fixas ---
        self.platforms = []
        self.platforms.extend(EntityFactory.get_entity('platform1', (400, 750)))
        self.platforms.extend(EntityFactory.get_entity('platform1', (200, 550)))
        self.platforms.extend(EntityFactory.get_entity('platform1', (400, 550)))
        self.platforms.extend(EntityFactory.get_entity('platform1', (80, 450)))
        self.platforms.extend(EntityFactory.get_entity('platform1', (20, 350)))
        self.platforms.extend(EntityFactory.get_entity('platform1', (40, 160)))
        self.platforms.extend(EntityFactory.get_entity('platform1', (600, 240)))
        self.platforms.extend(EntityFactory.get_entity('platform1', (1120, 815)))
        self.platforms.extend(EntityFactory.get_entity('platform1', (1290, 815)))
        self.platforms.extend(EntityFactory.get_entity('platform1', (1290, 615)))
        self.platforms.extend(EntityFactory.get_entity('platform1', (1420, 550)))
        self.platforms.extend(EntityFactory.get_entity('platform1', (1550, 450)))
        self.platforms.extend(EntityFactory.get_entity('platform1', (1380, 400)))
        self.platforms.extend(EntityFactory.get_entity('platform1', (1250, 300)))
        self.platforms.extend(EntityFactory.get_entity('platform1', (1290, 180)))

        # gemas
        self.gems = []
        self.gems.extend(EntityFactory.get_entity('gem', (410, 700)))
        self.gems.extend(EntityFactory.get_entity('gem', (210, 500)))
        self.gems.extend(EntityFactory.get_entity('gem', (30, 290)))
        self.gems.extend(EntityFactory.get_entity('gem', (50, 110)))
        self.gems.extend(EntityFactory.get_entity('gem', (758, 120)))
        self.gems.extend(EntityFactory.get_entity('gem', (1115, 115)))
        self.gems.extend(EntityFactory.get_entity('gem', (860, 615)))
        self.gems.extend(EntityFactory.get_entity('gem', (1050, 715)))
        self.gems.extend(EntityFactory.get_entity('gem', (1555, 365)))

        # espinhos
        self.spikes = []
        spike = EntityFactory.get_entity('spike', (15, 335))[0]
        spike.surf = pygame.transform.rotate(spike.surf, -90)  # gira 90° (para a esquerda)
        spike.rect = spike.surf.get_rect(topleft=spike.rect.topleft)
        self.spikes.append(spike)
        self.spikes.extend(EntityFactory.get_entity('spike', (250, 225)))
        self.spikes.extend(EntityFactory.get_entity('spike', (320, 225)))
        self.spikes.extend(EntityFactory.get_entity('spike', (390, 225)))
        self.spikes.extend(EntityFactory.get_entity('spike', (460, 225)))
        self.spikes.extend(EntityFactory.get_entity('spike', (850, 805)))
        self.spikes.extend(EntityFactory.get_entity('spike', (985, 805)))
        spike = EntityFactory.get_entity('spike', (1485, 180))[0]
        spike.surf = pygame.transform.rotate(spike.surf, 90)  # gira para direita
        spike.rect = spike.surf.get_rect(topleft=spike.rect.topleft)
        self.spikes.append(spike)
        self.spikes.extend(EntityFactory.get_entity('spike', (1585, 705)))
        self.spikes.extend(EntityFactory.get_entity('spike', (1565, 705)))
        self.spikes.extend(EntityFactory.get_entity('spike', (1545, 705)))
        self.spikes.extend(EntityFactory.get_entity('spike', (1525, 705)))
        self.spikes.extend(EntityFactory.get_entity('spike', (950, 505)))
        self.spikes.extend(EntityFactory.get_entity('spike', (970, 505)))
        self.spikes.extend(EntityFactory.get_entity('spike', (990, 505)))
        self.spikes.extend(EntityFactory.get_entity('spike', (1010, 505)))
        self.spikes.extend(EntityFactory.get_entity('spike', (1030, 505)))
        self.spikes.extend(EntityFactory.get_entity('spike', (1050, 505)))
        self.spikes.extend(EntityFactory.get_entity('spike', (1070, 505)))

        # checkpoint
        self.checkpoint = EntityFactory.get_entity('checkpoint', (1550, 133))[0]

        # HUD
        self.gem_count = 0
        self.font = pygame.font.SysFont("Lucida Sans Typewriter", 30)

    def reset_player(self):
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

            # reset se sair da tela
            if (self.player.rect.top > 900 or
                self.player.rect.bottom < 0 or
                self.player.rect.right < 0 or
                self.player.rect.left > 1600):
                self.reset_player()

            # colisão com terreno
            self.terrain.collide_and_resolve(self.player)

            # colisão com espinhos
            for spike in self.spikes:
                if self.player.rect.colliderect(spike.rect):
                    self.reset_player()

            # coletar gemas
            for gem in self.gems[:]:
                if self.player.rect.colliderect(gem.rect):
                    self.gems.remove(gem)
                    self.gem_count += 1

            # checkpoint
            if self.player.rect.colliderect(self.checkpoint.rect):
                # tela final de parabéns
                self.window.blit(self.background.surf, self.background.rect)
                congrats_text = self.font.render("Parabéns! Você concluiu a DEMO ", True, (255, 255, 0))
                text_rect = congrats_text.get_rect(center=(800, 450))
                self.window.blit(congrats_text, text_rect)
                pygame.display.flip()
                pygame.time.delay(4000)
                return "menu"   # volta para o menu principal

            # --- desenhar ---
            self.window.blit(self.background.surf, self.background.rect)
            self.terrain.draw(self.window)

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

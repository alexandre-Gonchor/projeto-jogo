#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

class Terrain:
    def __init__(self):
        self.shapes = [
            # --- BASE ESQUERDA COM RAMPA ---
            ([(0, 850), (0, 750), (200, 750), (200, 850)], (50, 200, 50)),

            # --- BLOCO FLUTUANTE ESQUERDA ---
            ([(550, 650), (630, 650), (630, 680), (550, 680)], (100, 100, 220)),

            # --- PLATAFORMA CENTRAL ---
            ([(200, 240), (500, 240), (500, 250), (200, 250)], (100, 200, 100)),

            # --- MURO DE DIVISÃO
            ([(780, 850), (750, 850), (750, 200), (780, 200)], (100, 200, 100)),

            # --- PLATORMA ESPINHO PT 2
            ([(1000, 820), (850, 820), (850, 840), (1000, 840)], (50, 200, 50)),

            # --- PLATAFORMA ANTI PRAGA
            ([(1100, 540), (950, 540), (950, 520), (1100, 520)], (50, 200, 50)),

            # --- MURO DE DIVISÃO 2
            ([(1101, 540), (1140, 540), (1140, 200), (1101, 200)], (100, 200, 100)),

            # --- BASE OPOSTA
            ([(1400, 740), (1600, 740), (1600, 720), (1400, 720)], (50, 200, 50)),

            # --- FINAL FASEL ---
            ([(1500, 200), (1600, 200), (1600, 180), (1500, 180)], (100, 200, 100)),
        ]

        # gerar máscaras para colisão pixel-perfect
        self.masks = []
        for points, color in self.shapes:
            surf = pygame.Surface((1600, 900), pygame.SRCALPHA)
            pygame.draw.polygon(surf, color, points)
            mask = pygame.mask.from_surface(surf)
            rect = surf.get_rect()
            self.masks.append((surf, rect, mask))

    def draw(self, window):
        for surf, rect, _ in self.masks:
            window.blit(surf, rect)

    def collide_and_resolve(self, player):
        player_mask = pygame.mask.from_surface(player.surf)
        for surf, rect_shape, mask in self.masks:
            offset = (player.rect.x - rect_shape.x, player.rect.y - rect_shape.y)
            overlap = mask.overlap(player_mask, offset)
            if overlap:
                if player.vel_y > 0:  # caindo
                    while mask.overlap(player_mask, offset):
                        player.rect.y -= 1
                        offset = (player.rect.x - rect_shape.x, player.rect.y - rect_shape.y)
                    player.vel_y = 0
                    player.on_ground = True
                elif player.vel_y < 0:  # batendo na cabeça
                    while mask.overlap(player_mask, offset):
                        player.rect.y += 1
                        offset = (player.rect.x - rect_shape.x, player.rect.y - rect_shape.y)
                    player.vel_y = 0

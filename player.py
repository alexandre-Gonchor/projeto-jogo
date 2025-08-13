#!/usr/bin/python
# -*- coding: utf-8 -*-

from entity import Entity
import pygame

class Player(Entity):
    def __init__(self, position=(100, 300)):
        super().__init__('player', position)
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        self.gravity = 0.5
        self.jump_strength = -10

    def update(self, keys, platforms):
        # Movimento horizontal
        self.vel_x = 0
        if keys[pygame.K_LEFT]:
            self.vel_x = -5
        if keys[pygame.K_RIGHT]:
            self.vel_x = 5

        # Pulo
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = self.jump_strength
            self.on_ground = False

        # Gravidade
        self.vel_y += self.gravity

        # Movimento horizontal + colisão lateral
        self.rect.x += self.vel_x
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_x > 0:  # indo para a direita
                    self.rect.right = platform.rect.left
                elif self.vel_x < 0:  # indo para a esquerda
                    self.rect.left = platform.rect.right

        # Movimento vertical + colisão vertical
        self.rect.y += self.vel_y
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:  # caindo
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:  # batendo por baixo
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0

    def move(self):
        pass

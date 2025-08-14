from entity import Entity
import pygame

class Player(Entity):
    def __init__(self, position=(100, 700)):
        super().__init__('player', position)
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        self.on_ledge = False  # Novo estado: agarrado na borda
        self.gravity = 0.5
        self.jump_strength = -10

    def update(self, keys, platforms):
        # Se estiver agarrado na borda
        if self.on_ledge:
            self.vel_x = 0
            self.vel_y = 0
            if keys[pygame.K_DOWN]:  # Soltar
                self.on_ledge = False
            if keys[pygame.K_SPACE]:  # Subir
                self.on_ledge = False
                self.rect.y -= 10  # sobe um pouco
                self.vel_y = 0
            return  # não processa física normal

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

        # Movimento lateral + colisão
        self.rect.x += self.vel_x
        for p in platforms:
            if self.rect.colliderect(p.rect):
                if self.vel_x > 0:
                    self.rect.right = p.rect.left
                    # Checar agarrada na borda (pela direita)
                    if not self.on_ground and abs(self.rect.bottom - p.rect.top) < 20:
                        self.on_ledge = True
                        self.rect.bottom = p.rect.top + 5
                        return
                elif self.vel_x < 0:
                    self.rect.left = p.rect.right
                    # Checar agarrada na borda (pela esquerda)
                    if not self.on_ground and abs(self.rect.bottom - p.rect.top) < 20:
                        self.on_ledge = True
                        self.rect.bottom = p.rect.top + 5
                        return

        # Movimento vertical + colisão
        self.rect.y += self.vel_y
        self.on_ground = False
        for p in platforms:
            if self.rect.colliderect(p.rect):
                if self.vel_y > 0:
                    self.rect.bottom = p.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:
                    self.rect.top = p.rect.bottom
                    self.vel_y = 0

    def move(self):
        pass

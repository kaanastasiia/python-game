import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, alien_invasion_game):
        super().__init__()
        self.screen = alien_invasion_game.screen
        self.settings = alien_invasion_game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = alien_invasion_game.ship.rect.midtop
        self.y = float(self.rect.y)
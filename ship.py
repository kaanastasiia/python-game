import pygame

class Ship:
    def __init__(self, alien_invasion_game):
        self.screen = alien_invasion_game.screen
        self.screen_rect = alien_invasion_game.screen.get_rect()
        self.image = pygame.image.load('./images/starship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image,self.rect)

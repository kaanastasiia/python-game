import sys
from settings import Settings
from ship import Ship
import pygame

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()
                self.screen.fill(self.bg_color)
                self.ship.blitme()                
                pygame.display.flip()

if __name__ == "__main__":
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
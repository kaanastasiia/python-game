import sys
from settings import Settings
from ship import Ship
import pygame

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bg_color = self.settings.bg_color

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
   
    def _check_events(self):
        for event in pygame.event.get():
            self._quit_game_on_button(event)
            self._check_keydown_events(event)
            self._check_keyup_events(event)

    def _quit_game_on_button(self, event):
        if event.type == pygame.QUIT:
            pygame.QUIT()
        

    def _check_keydown_events(self, event):
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                pygame.QUIT()


    def _check_keyup_events(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False
    

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.update()
        self.ship.blitme()                
        pygame.display.flip()

if __name__ == "__main__":
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
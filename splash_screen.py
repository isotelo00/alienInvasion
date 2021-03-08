import pygame as pg
import pygame.font

class SplashScreen:

    def __init__(self, settings, screen, play_button, score_button):
        self.screen = screen
        self.play_button = play_button
        self.score_button = score_button

        self.title_font = pygame.font.SysFont(None, 100)
        self.Title = self.title_font.render('ALIEN INVADERS', False, (60,230,60))

        self.font = pygame.font.SysFont(None, 48)

        self.score0 = self.font.render(' = 10 pts', False, (200, 200, 200))
        self.score1 = self.font.render(' = 20 pts', False, (200, 200, 200))
        self.score2 = self.font.render(' = 40 pts', False, (200, 200, 200))
        self.score3 = self.font.render(' = ??? pts', False, (200, 200, 200))

    def draw(self):
        self.play_button.draw()
        self.score_button.draw()
        self.alien_info()
        self.title()

    def title(self):
        self.screen.blit(self.Title, [325, 50])

    def alien_info(self):
        alien0 = pg.image.load('images/alien00.png')
        alien1 = pg.image.load('images/alien10.png')
        alien2 = pg.image.load('images/alien20.png')
        alien3 = pg.image.load('images/alien30.png')

        self.screen.blit(alien0, [100, 200])
        self.screen.blit(self.score0, [164, 200])
        self.screen.blit(alien1, [100, 275])
        self.screen.blit(self.score1, [164, 275])
        self.screen.blit(alien2, [100, 350])
        self.screen.blit(self.score2, [164, 350])
        self.screen.blit(alien3, [100, 425])
        self.screen.blit(self.score3, [164, 425])







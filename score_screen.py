import pygame as pg
import pygame.font

class ScoreScreen:

    def __init__(self, settings, screen, button):
        self.screen = screen
        self.button = button

        self.title_font = pygame.font.SysFont(None, 100)
        self.Title = self.title_font.render('HIGH SCORES', False, (60,230,60))

        self.font = pygame.font.SysFont(None, 72)

        high_score_file = open("highscores.txt", "r")
        temphigh = []
        num_lines = self.file_len("highscores.txt")
        for x in range(num_lines):
            temphigh.append(int(high_score_file.readline()))
        temphigh.sort()
        high_score_file.close()

        self.score0 = self.font.render(str(temphigh[0]), False, (200, 200, 200))
        self.score1 = self.font.render(str(temphigh[1]), False, (200, 200, 200))
        self.score2 = self.font.render(str(temphigh[2]), False, (200, 200, 200))
        self.score3 = self.font.render(str(temphigh[3]), False, (200, 200, 200))
        self.score4 = self.font.render(str(temphigh[4]), False, (200, 200, 200))

    def draw(self):
        self.button.draw()
        self.scores()
        self.title()

    def title(self):
        self.screen.blit(self.Title, [325, 50])

    def scores(self):
        self.screen.blit(self.score0, [500, 500])
        self.screen.blit(self.score1, [500, 550])
        self.screen.blit(self.score2, [500, 600])
        self.screen.blit(self.score3, [500, 650])
        self.screen.blit(self.score4, [500, 700])

    def file_len(self, fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1
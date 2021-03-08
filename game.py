from io import open

import pygame as pg
from settings import Settings
import game_functions as gf

from ship import Ship
from alien import Aliens
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from sound import Sound
from barrier import Barriers
from splash_screen import SplashScreen
from score_screen import ScoreScreen

import time
import atexit

class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode(size=(self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption("Alien Invasion")
        ship_image = pg.image.load('images/ship.bmp')
        self.ship_height = ship_image.get_rect().height

        self.sound = Sound(bg_music="sounds/startrektheme.wav")
        self.sound.play()
        self.sound.pause_bg()
        self.splash_screen = self.score_button = self.play_button = self.aliens = self.stats = self.sb = self.ship = None
        self.restart()

    def restart(self):
        self.play_button = Button(settings=self.settings, screen=self.screen, msg="Play", type='play')
        self.score_button = Button(settings=self.settings, screen=self.screen, msg="SCORES", type='score')
        self.stats = GameStats(settings=self.settings)
        self.sb = Scoreboard(game=self, sound=self.sound)
        self.settings.init_dynamic_settings()

        self.barriers = Barriers(game=self)
        self.aliens = Aliens(ship_height=self.ship_height, game=self, barriers=self.barriers)
        self.ship = Ship(aliens=self.aliens, sound=self.sound, game=self, barriers=self.barriers)
        self.splash_screen = SplashScreen(settings=self.settings,screen=self.screen,play_button=self.play_button,score_button=self.score_button)
        self.score_screen = ScoreScreen(settings=self.settings,screen=self.screen,button=self.play_button)
        self.aliens.add_ship(ship=self.ship)
        self.sb.prep_high_score()

    def play(self):
        atexit.register(self.exit_handler)
        while True:
            gf.check_events(stats=self.stats, play_button=self.play_button, score_button=self.score_button, ship=self.ship, sound=self.sound)
            if self.stats.game_active:
                self.ship.update()
                self.aliens.update()
                self.barriers.update()

            self.screen.fill(self.settings.bg_color)
            self.ship.draw()
            self.aliens.draw()
            self.barriers.draw()
            self.sb.show_score()
            if not self.stats.game_active:
                if self.stats.score_active:
                    self.screen.fill(self.settings.bg_color)
                    self.score_screen.draw()
                else:
                    self.screen.fill(self.settings.bg_color)
                    self.splash_screen.draw()
                self.sound.pause_bg()
            else:
                if not self.sound.playing_bg: self.sound.unpause_bg()
            pg.display.flip()

    def reset(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.aliens.empty()
            self.aliens.create_fleet()
            self.ship.center_ship()
            time.sleep(0.5)
            self.ship.timer = Ship.timer
        else:
            self.stats.game_active = False
            self.sound.pause_bg()
            self.hs = self.stats.high_score
            self.restart()

    def exit_handler(self):
        high_score_file = open("highscores.txt", "r")
        temphigh = []
        num_lines = self.file_len("highscores.txt")
        for x in range(num_lines):
            temphigh.append(int(high_score_file.readline()))
        temphigh.sort()
        high_score_file.close()
        if temphigh[0] < self.stats.high_score & temphigh[4] != self.stats.high_score:
            temphigh[0] = self.stats.high_score
            with open('highscores.txt', 'w') as f:
                for item in temphigh:
                    f.write("%s\n" % item)









    def file_len(self, fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1

def main():
    g = Game()
    g.play()
    # Vector.run_tests()
    # Quaternion.run_tests()
    # Matrix.run_tests()
    # Alien.run_tests()


if __name__ == '__main__':
    main()

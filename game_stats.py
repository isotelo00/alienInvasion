class GameStats():
    def __init__(self, settings):
        self.settings = settings
        self.game_active = False
        self.score_active = False
        self.reset_stats()
        high_score_file = open("highscores.txt")
        score_list = high_score_file.readlines()
        for i in range(0, len(score_list)):
            score_list[i] = int(score_list[i])
        score_list.sort()
        score_list.reverse()
        self.high_score = score_list[0]
        self.level = 1

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0

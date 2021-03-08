import pygame as pg
import pygame.font

class Button:
    def __init__(self, settings, screen, msg, type):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (50, 50, 50)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pg.Rect(0, 0, self.width, self.height)

        if type == 'play':
            self.rect.center = self.screen_rect.center
        elif type == 'score':
            self.rect.bottomright = self.screen_rect.bottomright
        elif type == 'menu':
            self.rect.bottomleft = self.screen_rect.bottomleft
        self.prep_msg(msg)


    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

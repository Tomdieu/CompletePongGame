import pygame
from ball import Ball
pygame.init()
class Paddle(pygame.sprite.Sprite):
    def __init__(self,surface,game_type):
        super().__init__()
        self.surface = surface
        self.rect=pygame.Rect(400,450,10,120)
        self.velocity=4
        self.color=pygame.Color('grey')
        self.rect.x=self.surface.get_width()-32
        self.rect.y=self.surface.get_height()//2-self.rect.h//2
        self.score=0
        self.ai=''
        #957 37 965 30
    """    def move_right(self):
        if self.rect.x+10>=self.surface.get_width():
            self.rect.x=self.surface.get_width()-10
        else:
            self.rect.x+=self.velocity
    def move_left(self):
        if self.rect.x<=0:
            self.rect.x=0
        else:
            self.rect.x-=self.velocity"""
    def draw(self,surface):
        pygame.draw.rect(surface,self.color,self.rect)
    def move_up(self):
        if self.rect.top<=20:
            self.rect.y=20
        else:
            self.rect.y-=self.velocity
    def move_down(self):
        if self.rect.bottom>=self.surface.get_height()-20:
            self.rect.bottom=self.surface.get_height()-20
        else:
            self.rect.y+=self.velocity

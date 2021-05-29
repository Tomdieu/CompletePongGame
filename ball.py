import pygame,random
pygame.init()
class Ball(pygame.sprite.Sprite):
    def __init__(self,surface,opponent,game_type):
        self.surface=surface
        self.opponent=opponent
        self.color=pygame.Color('grey')
        self.rect=pygame.Rect(250,250,30,30)
        """self.velocity_x=3*random.choice((-1,1))
        self.velocity_y=3*random.choice((-1,1))"""
        self.rect.x=surface.get_width()//2-self.rect.width//2
        self.rect.y=surface.get_height()//2-self.rect.height//2
        self.game_type=game_type
        if self.game_type=="easy":
            self.velocity_x = 2 * random.choice((-1, 1))
            self.velocity_y = 2 * random.choice((-1, 1))
        elif self.game_type=="medium":
            self.velocity_x = 3 * random.choice((-1, 1))
            self.velocity_y = 3 * random.choice((-1, 1))
        elif self.game_type=="dificult":
            self.velocity_x = 4 * random.choice((-1, 1))
            self.velocity_y = 4 * random.choice((-1, 1))
    def draw(self):
        pygame.draw.ellipse(self.surface,self.color,self.rect)
    def move(self):
        self.rect.x+=self.velocity_x
        self.rect.y+=self.velocity_y
        #980
        if self.rect.right>=self.surface.get_width()-15 or self.rect.left<=12:
            self.velocity_x*=-1
        elif self.rect.top<=20 or self.rect.bottom>=680:
            self.velocity_y*=-1

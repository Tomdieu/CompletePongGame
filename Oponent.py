import pygame,random
pygame.init()

class Oponnent(pygame.sprite.Sprite):
    def __init__(self,surface,ball,game_type):
        super().__init__()
        self.surface = surface
        self.rect = pygame.Rect(400, 450, 10, 120)
        self.velocity_y = 9
        self.color = pygame.Color('grey')
        self.rect.x = 22
        self.rect.y = self.surface.get_height()//2-self.rect.h//2
        self.score = 0
        self.ball=ball
        self.game_type=game_type
    def up(self):
        if self.rect.top<self.ball.rect.y :#and self.ball.rect.left<self.surface.get_width()//2:
            if self.game_type=='dificult':
                self.rect.y+=self.velocity_y+5
            elif self.game_type=='medium':
                self.rect.y+=self.velocity_y+2
            else:
                self.rect.y += self.velocity_y
    def down(self):
        if self.rect.bottom>self.ball.rect.y:# and self.ball.rect.left<self.surface.get_width()//2:
            self.rect.y-=self.velocity_y
    def move(self):
        if self.game_type=="easy":
            self.velocity_y = 6
            self.up()
            self.down()
            """c=random.choice((-1,1))
            if c==-1:
                self.up()
            else:
                self.down()"""
        elif self.game_type=="medium":
            self.velocity_y = 8
            self.up()
            self.down()
        elif self.game_type=='dificult':
            self.velocity_y = 13
            self.up()
            self.down()
        if self.rect.top<=20:
            self.rect.top=20
        if self.rect.bottom>=680:
            self.rect.bottom=680
        print(self.velocity_y)
    def draw(self):
        pygame.draw.rect(self.surface,self.color,self.rect)


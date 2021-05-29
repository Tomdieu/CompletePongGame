import pygame,random,winsound,sys
from Oponent import Oponnent
font=pygame.font.SysFont('arial',20)
pygame.init()

class Game1(pygame.sprite.Sprite):
    def __init__(self,surface,ball,paddle,opponent,game_type):
        super().__init__()
        self.surface=surface
        self.ball=ball
        self.paddle=paddle
        self.opponent=opponent
        self.all_rec=pygame.sprite.Group()
        self.color_box=pygame.Color('red')
        self.grid_rect=pygame.Rect(0,0,50,50)
        self.op_scr=0
        self.pdl_scr=0
        self.play=True
        self.count=3
        self.stop=True
        self.increase_ball_speed=False
        self.increase_ball_speed_x=0
        self.increase_ball_speed_y=0
        self.clock=pygame.time.Clock()
        self.game_type=game_type
        self.tim_con = font.render(str(self.count), True, (255, 0, 0))
        self.tim_con_re = self.tim_con.get_rect(center=(self.surface.get_width() // 2, self.surface.get_height() // 2 + 50))
        self.surface.blit(self.tim_con, self.tim_con_re)
    def draw_grid(self):
        pass
    def reset(self):
        #self.delay()

        self.paddle.rect.y = self.surface.get_height() // 2 - self.paddle.rect.h // 2
        self.opponent.rect.y = self.surface.get_height() // 2 - self.paddle.rect.h // 2
        self.ball.rect.center = (self.surface.get_width()// 2 - 12, self.surface.get_height() // 2 - 15)
        """"        self.ball.velocity_x = random.choice((-3-self.increase_ball_speed_x, 3+self.increase_ball_speed_y))
        self.ball.velocity_y = random.choice((-3-self.increase_ball_speed_x, 3+self.increase_ball_speed_y))"""
        if self.game_type=="easy":
            self.ball.velocity_x = 2 * random.choice((-1, 1))
            self.ball.velocity_y = 2 * random.choice((-1, 1))
        elif self.game_type=="medium":
            self.ball.velocity_x = 3 * random.choice((-1, 1))
            self.ball.velocity_y = 3 * random.choice((-1, 1))
        elif self.game_type=="dificult":
            self.ball.velocity_x = random.choice((-4-self.increase_ball_speed_x, 4+self.increase_ball_speed_y))
            self.ball.velocity_y = random.choice((-4-self.increase_ball_speed_x, 4+self.increase_ball_speed_y))
    def update_scr(self,surface):
        self.surface.fill((255,255,255))
        self.ball.draw()
        self.paddle.draw(self.surface)
        self.ball.move()
        self.draw_grid()
        pygame.draw.line(self.surface, (0, 0, 0), (self.surface.get_width() // 2, 20),(self.surface.get_width() // 2, 680))
        if self.paddle.rect.colliderect(self.ball.rect) and self.paddle.velocity > 0:
            if abs(self.ball.rect.right - self.paddle.rect.left) < 10:
                self.ball.velocity_x *= -1
            elif abs(self.ball.rect.top - self.paddle.rect.bottom) < 10 and self.ball.velocity_y > 0:
                self.ball.velocity_y *= -1
            elif abs(self.ball.rect.top - self.paddle.rect.bottom) < 10 and self.ball.velocity_y < 0:
                self.ball.velocity_y *= -1

        if self.ball.rect.colliderect(self.opponent.rect) :
            if abs(self.ball.rect.right - self.opponent.rect.left) < 10:
                self.ball.velocity_x *= -1
            elif abs(self.ball.rect.top - self.opponent.rect.bottom) < 10 and self.ball.velocity_y > 0:
                self.ball.velocity_y *= -1
            elif abs(self.ball.rect.top - self.opponent.rect.bottom) < 10 and self.ball.velocity_y < 0:
                self.ball.velocity_y *= -1
            self.ball.velocity_x *= -1
        if (self.ball.rect.right) >= (self.paddle.rect.x + 10):
            self.op_scr += 1
            winsound.Beep(2937, 300)
            self.reset()
            self.play = False
        if (self.ball.rect.left )<= (self.opponent.rect.x-7 ):
            self.pdl_scr += 1
            winsound.Beep(2937, 300)
            self.reset()
            self.play = False
        if ((self.paddle.score>=10) or (self.opponent.score>=10)) and self.increase_ball_speed==False:
            self.increase_ball_speed=True

        if self.increase_ball_speed==True and self.stop==False:
            self.ball.velocity_x+=3
            self.ball.velocity_y+=3
        if self.game_type=='dificult' and self.ball.velocity_x>7:
            self.stop=True
def welcome(scr):
    font=pygame.font.Font("always forever.ttf",90)
    text="welcome"
    move_text="Pong Game"
    n=10
    b,c=0,0
    con=True
    f=True
    time=0
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
                sys.exit()

        scr.fill(pygame.Color('white'))
        pygame.time.delay(1000)
        time+=1
        wel=font.render(str(text),True,pygame.Color('orange'))
        wel_rec=wel.get_rect(center=(scr.get_width()//2-wel.get_width()//2+57,scr.get_height()//2-wel.get_height()//2))
        scr.blit(wel,wel_rec)

        fonty = pygame.font.Font('BaltimoreTypewriterBold Beveled.otf', n)
        load=fonty.render(str('Loading'),True,pygame.Color('blue'))
        #load_rect=load.get_rect(center=(scr.get_width()//2-load.get_width()//2+(scr.get_width()//2-load.get_width()//2),scr.get_height()//2-load.get_height()//2+300))
        load_rect = load.get_rect(center=(scr.get_width() // 2 , scr.get_height() // 2 + 300))
        load_rect.x-=1
        if con==True:
            n+=30
        if n>=70:
            n=30
        if time>=random.randint(6,9):
            n=70
            con=False
            run=False
        scr.blit(load,load_rect)
        pygame.display.update()
def reset_time(scr):
    TT = pygame.font.Font("BaltimoreTypewriterBold Beveled.otf", 300)
    j = True
    white = pygame.Color("white")
    count = 4
    while j:
        scr.fill(white)
        pygame.time.delay(1000)
        count -= 1
        count_text = TT.render(str(count), True, (0, 0, 0))
        count_text_r=count_text.get_rect(center=(scr.get_width()// 2 ,scr.get_height()//2))
        scr.blit(count_text, count_text_r)
        pygame.display.update()
        if count == 0:
            j = False

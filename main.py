import pygame,sys

from pygame.locals import *
from Paddle import Paddle
from ball import Ball
from game import Game1,welcome,reset_time
from Oponent import Oponnent
import random
import winsound

#2937
pygame.init()
pygame.display.init()
pygame.display.get_init()
font=pygame.font.SysFont('arial',20)
scr=pygame.display.set_mode((1000,700))
pygame.display.set_caption('Pong Game')
ico=pygame.image.load('logo.png')
pygame.display.set_icon(ico)
game_type="easy"
but=pygame.image.load('button.png').convert_alpha()
#but=pygame.transform.scale(but,(166*2,66*2))
but_rect=but.get_rect(center=(scr.get_width()//2-40,scr.get_height()//2))
p=pygame.image.load('p.png').convert_alpha()
p_rect=p.get_rect(center=(scr.get_width()//2-190,scr.get_height()//2))

n=pygame.image.load('n.png').convert_alpha()
n_rect=n.get_rect(center=(scr.get_width()//2+90,scr.get_height()//2))

g=pygame.image.load('g.png').convert_alpha()
g_rect=g.get_rect(center=(scr.get_width()//2+240,scr.get_height()//2))
#create a variable paddle to contain the class
code_play=""
name=""
check="stop"
ok=pygame.image.load('cor.png').convert_alpha()
code_play.lower()
paddle=Paddle(scr,game_type)
ball=Ball(scr,paddle,game_type)
oponnent=Oponnent(scr,ball,game_type)
gam=Game1(scr,ball,paddle,oponnent,game_type)
clk=pygame.time.Clock()
def move_ai():
    if paddle.rect.top < ball.rect.y:  # and self.ball.rect.left<self.surface.get_width()//2:
        paddle.rect.y += 7+5#paddle.velocity
    if paddle.rect.bottom > ball.rect.y:  # and self.ball.rect.left<self.surface.get_width()//2:
        paddle.rect.y -= 7#paddle.velocity
    if paddle.rect.bottom >= paddle.surface.get_height() - 20:
        paddle.rect.bottom = scr.get_height() - 20
    if paddle.rect.top <= 20:
        paddle.rect.y=20
run=True
def good_bye():
    font = pygame.font.Font("always forever.ttf", 90)
    text = "Good Bye"
    move_text = "Pong Game"
    n = 10
    b, c = 0, 0
    con = True
    f = True
    time = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pass
        scr.fill(pygame.Color('white'))
        pygame.time.delay(1000)
        time += 1
        wel = font.render(str(text), True, pygame.Color('orange'))
        wel_rec = wel.get_rect(
            center=(scr.get_width() // 2 - wel.get_width() // 2 + 57, scr.get_height() // 2 - wel.get_height() // 2))
        scr.blit(wel, wel_rec)
        fonty = pygame.font.Font('BaltimoreTypewriterBold Beveled.otf', n)
        load = fonty.render(str('Thanks!'), True, pygame.Color('blue'))
        # load_rect=load.get_rect(center=(scr.get_width()//2-load.get_width()//2+(scr.get_width()//2-load.get_width()//2),scr.get_height()//2-load.get_height()//2+300))
        load_rect = load.get_rect(center=(scr.get_width() // 2, scr.get_height() // 2 + 300))
        load_rect.x -= 1
        if con == True:
            n += 30
        if n >= 70:
            n = 30
        if time >= random.randint(7, 11):
            n = 70
            con = False
            run = False
            pygame.quit()
            sys.exit()
        scr.blit(load, load_rect)
        pygame.display.update()
def menu():
    pass
def play():
    global code_play,check,name
    run = True
    fonty_1=pygame.font.SysFont('Arial',20)
    if name == '':
        name = 'player'
    while run:
        ft = pygame.font.SysFont('arial', 20)
        look = ft.render(str("Difficulty : "+game_type), True, (0, 0, 0))
        look_rect = look.get_rect(center=(scr.get_width() // 2-10, 40))

        score_1 = font.render(str(gam.op_scr), True, pygame.Color('black'))
        score_2 = font.render(str(gam.pdl_scr), True, pygame.Color('black'))
        gam.update_scr(scr)
        oponnent.draw()
        oponnent.move()
        scr.blit(score_1, (465, 335))
        scr.blit(score_2, (525, 335))
        scr.blit(look, look_rect)

        op=fonty_1.render(str('opponent'),True,(0,0,0))
        op_rect=op.get_rect(center=(scr.get_width()//2-60,10))
        pygame.draw.rect(scr, (0, 0, 0), (20, 20, 960, 660), 1)
        pygame.draw.rect(scr, pygame.Color('orange'), (0, 0, 1000, 700), 40)
        o=fonty_1.render(str(code_play),True,pygame.Color('black'))
        scr.blit(o,(20,680))
        scr.blit(op,op_rect)
        aff = fonty_1.render(str(name), True, (0, 0, 0))
        aff_rect = aff.get_rect(center=(scr.get_width() // 2 + 40, 10))
        scr.blit(aff, aff_rect)
        #pygame.draw.rect(scr,(0,0,0),(20,680,60,20))
        keys = pygame.key.get_pressed()
        if check=='stop':
            if keys[pygame.K_UP]:
                paddle.move_up()
            if keys[pygame.K_DOWN]:
                paddle.move_down()
        elif check=='ivan':
            move_ai()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                start()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:
                    code_play=code_play[:-1]
                else:
                    code_play+=event.unicode
        if code_play.lower()=='ivan':
            check= code_play.lower()
            code_play=''
        if code_play.lower()=='stop':
            check = code_play.lower()
            code_play=''
        print(code_play)
        if len(code_play)>4:
            code_play=''
        pygame.display.flip()
        pygame.display.update()
welcome(scr)
def start():
    global game_type,name
    navy=pygame.font.SysFont('consolas',50)
    run=True
    pos1, pos2 = 100, 100
    clock=pygame.time.Clock()
    count=30
    rect=pygame.Rect(scr.get_width()//2-150,scr.get_height()//2-150,300,50)
    text="Program by Ivan copyright (c) 2021 "
    easy_rect=pygame.Rect(100,100,50,50)
    meduim_rect=pygame.Rect(320,100,50,50)
    dificult_rect=pygame.Rect(590,100,50,50)
    text1='Easy'
    text2='Medium'
    text3='Dificult'
    text4="DIFICUTY"
    prit=True
    dif=navy.render(str(text4),True,pygame.Color('orange'))
    dif_rect=dif.get_rect(center=(scr.get_width()//2,scr.get_height()//2-300))
    name_background='Enter your name'
    #name=""
    help_font=pygame.font.Font('BaltimoreTypewriterBold Beveled.otf',30)
    show=True
    ft_name=pygame.font.SysFont('arial',40)
    ft_name_1 = pygame.font.SysFont('arial', 35)
    show_help=False
    woo=[]
    n_count=214
    text_ = 'Whe playing,no need\nof of pause just quit the \ngame and go back \nto the menu when you\nwhant to continue just click play \nand your score will not change \nbut if you whant to reset the score \nclick reset'
    woo.append("When playing,no need")
    woo.append("of pause just quit the ")
    woo.append("game and go back ")
    woo.append("to the menu.When you")
    woo.append("whant to continue  ")
    woo.append("just click play")
    woo.append("and your score will not  ")
    woo.append("change but if you ")
    woo.append("whant to reset the score ")
    woo.append("click reset.")

    while run:
        reset=(pygame.font.Font('BaltimoreTypewriterBold Beveled.otf', 30)).render(str('Reset Score'),True,(0,0,0))
        reset_rect=reset.get_rect(center=(170,175))

        scr.fill(pygame.Color('white'))
        scr.blit(but,but_rect)
        scr.blit(p,p_rect)
        scr.blit(n, n_rect)
        scr.blit(g, g_rect)
        scr.blit(dif,dif_rect)
        scr.blit(ok,(pos1,pos2))
        ea=navy.render(str(text1),True,(0,0,0))
        scr.blit(ea,(170,100))
        me=navy.render(str(text2),True,(0,0,0))
        scr.blit(me,(390,100))
        di = navy.render(str(text3), True, (0, 0, 0))
        scr.blit(di, (680, 100))
        scr.blit(reset, reset_rect)
        if name == '':
            put = ft_name.render(str(name_background), True, pygame.Color('grey'))
            put_rect = put.get_rect(center=(scr.get_width() // 2 , scr.get_height() // 2 - 123))
            scr.blit(put, (put_rect))
        if name != '':
            put = ft_name_1.render(str(name), True, pygame.Color('black'))
            put_rect = put.get_rect(center=(scr.get_width() // 2 , scr.get_height() // 2 - 123))
            scr.blit(put, (put_rect))
        help=help_font.render(str('Help'),True,(0,0,0))
        help_rect=help.get_rect(center=(871,165))
        scr.blit(help,help_rect)
        pygame.draw.rect(scr,(255,0,0),rect,5)
        #important point 819,214
        if show_help==True:
            pygame.draw.rect(scr,pygame.Color('grey'),(805,214,180,210))
            for i in woo:
                help_tect = (pygame.font.SysFont('arial', 20)).render(str(i), True, (0, 0, 0))
                scr.blit(help_tect, (806, n_count))
                #pygame.time.delay(1000)
                if prit == True:
                    n_count += 20
                if i=="click reset.":
                    n_count=216


        pygame.draw.rect(scr,pygame.Color('brown'),easy_rect,1)
        pygame.draw.rect(scr, pygame.Color('brown'),meduim_rect, 1)
        pygame.draw.rect(scr, pygame.Color('brown'),dificult_rect, 1)
        font = pygame.font.Font('SimplySquare.ttf',count)
        iv=font.render(str(text),True,pygame.Color('black'))
        iv_rect=iv.get_rect(center=(scr.get_width()//2,scr.get_height()//2+200))
        scr.blit(iv,iv_rect)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                good_bye()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    pos=pygame.mouse.get_pos()
                    if easy_rect.collidepoint(pos):
                        pos1,pos2=100,100
                        game_type='easy'
                    elif meduim_rect.collidepoint(pos):
                        pos1, pos2 = 320,100
                        game_type="medium"
                    elif dificult_rect.collidepoint(pos):
                        pos1, pos2 = 590,100
                        game_type="dificult"
                    elif but_rect.collidepoint(pos):
                        gam.game_type=game_type
                        ball.game_type=game_type
                        oponnent.game_type=game_type
                        reset_time(scr)
                        winsound.Beep(4000, 1000)
                        play()
                    elif rect.collidepoint(pos):
                        show=False
                    elif help_rect.collidepoint(pos):
                        show_help=True
                    elif reset_rect.collidepoint(pos):
                        gam.op_scr=0
                        gam.pdl_scr=0
                    else:
                        show=True
                        show_help=False
            if event.type==pygame.KEYDOWN:
                if show==False:
                    if event.key==pygame.K_BACKSPACE:
                        name=name[:-1]
                    else:
                        name+=event.unicode
            if len(name)>15:
                show=True
        if game_type=='easy':
            pos1, pos2 = 100, 100
        if game_type=="medium":
            pos1, pos2 = 320,100
        if game_type=="dificult":
            pos1, pos2 = 590,100
        count+=1
        if count>=60:
            count=30
        clock.tick(30)
        pygame.display.update()
start()

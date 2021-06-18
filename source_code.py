import pygame as pg
from pygame import mixer
import random
import math


#initializing game variables
pg.init()
rocket_x=250
rocket_y=400
rocket_x_change = 0
astroid=[]
moveSpeed=0.5
score=0.0


#loading requirments

rocketimg=pg.image.load('rocket.png')
astroidimg=pg.image.load('astroid.png')
bgimg=pg.image.load('background.png')
icon=pg.image.load('icon.png')

font=pg.font.Font('font.ttf',32)
gameOver_font=pg.font.Font('font.ttf',50)

bgmusic=mixer.music.load('bgm.mp3')
explosionsound=mixer.Sound('explosion.wav')

#initializing window 
screen=pg.display.set_mode((700,600))
pg.display.set_caption("Space Traveller")
pg.display.set_icon(icon)
mixer.music.play(-1)


#generating new astroids
def newAstroids():
    astroid.append([])
    end=150
    start=0
    for i in range(random.randint(2,4)):
        astroid[-1].append([random.randint(start,end),0])
        start+=180
        end+= 170
    global moveSpeed    #increasing astroid's speed
    moveSpeed+=0.01

# displaying astroids
def astroid_display():
    for ls in astroid:
        i=0
        if ls[0][1]>600:
            del astroid[0]
        for x,y in ls:
            screen.blit(astroidimg,(x,y))
            if (ls[i][0]<=rocket_x+50 and ls[i][0]>=rocket_x-43 ) and (ls[i][1]>=rocket_y-75 and ls[i][1] < rocket_y+100):      #collision checking
                global running
                running = False
                
            ls[i][1]+=moveSpeed
            i+=1



#score printing
def score_display():
    score_text=font.render("SCORE : "+str(int(score)),True,(0,255,255))
    screen.blit(score_text,(450,0))

#gameover text display
def gameOver_display():
    gameOver_text = gameOver_font.render("GAME OVER",True,(100,200,255))
    screen.blit(gameOver_text,(180,250))

running=True
close = False
loop = 0

while running:

    screen.blit(bgimg,(0,0))
    screen.blit(rocketimg,(rocket_x,rocket_y))
    astroid_display()
    score_display()
     # checking for gameover
    if not running :
        explosionsound.play()
        gameOver_display()
        
    if loop == 600:          #Creating new row of astroids
        newAstroids()
        loop =-1


        
    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            running=False
            close=True
            pg.display.quit()

        #KEY PRESS 
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                rocket_x_change= -2
            if event.key == pg.K_RIGHT:
                rocket_x_change= 2

        #KEY RELEASED
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                rocket_x_change=0

    #moving rocket
    rocket_x +=  rocket_x_change

    #boundaries for rocket
    if rocket_x>=635:
        rocket_x=635
    if  rocket_x <= 0 :
        rocket_x= 0
    score+=0.02

    pg.display.update()
    loop+=1

pg.mixer.music.stop()

while not close:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            close= True
            pg.display.quit()
            pg.quit()





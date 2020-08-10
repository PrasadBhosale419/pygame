import random
import math

import pygame
from pygame import mixer

#initialize the pygame
pygame.init()

#diplaying the screen
screen=pygame.display.set_mode((800,600))

#backgroud
background=pygame.image.load('C:/Users/user/Documents/bckg.png')

#background music
mixer.music.load('C:/Users/user/Desktop/Space-Invaders-Pygame-master/Space-Invaders-Pygame-master/background.wav')
mixer.music.play(-1)

#title and icon
pygame.display.set_caption("Prasad's Py-project")
#loading an image in a specific variable
icon=pygame.image.load('C:/Users/user/Pictures/ufo.png')
#setting a particular image as an icon
pygame.display.set_icon(icon)

#player
player_img=pygame.image.load('C:/Users/user/Pictures/player.png')
playerX=370
playerY=480
playerX_change=0

#invader
invader_img=[]
invaderX=[]
invaderX=[]
invaderY=[]
invaderX_change=[]
invaderY_change=[]
num_of_enemies=6

for i in range(num_of_enemies):
    invader_img.append(pygame.image.load('C:/Users/user/Pictures/invader.png'))
    invaderX.append(random.randint(0,735))
    invaderY.append(random.randint(50,150))
    invaderX_change.append(1)
    invaderY_change.append(40)

#bullet
#ready-the bullet is currently not visible on the screen
#Fire-the bullet starts moving on the screen
bullet_img=pygame.image.load('C:/Users/user/Pictures/bullet.png')
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=10
bullet_state = "ready"

#score

score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

testX = 10
testY = 10

#game over text
game_over = pygame.font.Font('freesansbold.ttf',64)


def show_score(x,y):
    score = font.render("Score:"+str(score_value),True, (225,255,0))
    screen.blit(score,(x,y))

def game_over_text():
    over_text=font.render("GAME OVER"+str(score_value), True,(255,225,225))
    screen.blit(over_text,(200,250))

def player(x,y):
    screen.blit(player_img,(x,y))

def invader(x,y,i):
    screen.blit(invader_img[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet_img,(x + 16,y + 10))

def iscollision(invaderX,invaderY,bulletX,bulletY):
    distance = math.sqrt((math.pow(invaderX-bulletX,2)) + (math.pow(invaderY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

#game loop
while True:
    
    #RGB= red,green,blue
    screen.fill((255,255,0))
    
    #background image
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #check whether the keyword pressed is left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                    playerX_change= -4
            if event.key == pygame.K_RIGHT:
                    playerX_change= 4
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound=mixer.Sound('C:/Users/user/Desktop/Space-Invaders-Pygame-master/Space-Invaders-Pygame-master/laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
      
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                  playerX_change= 0
    
    playerX +=playerX_change

    #checking boundary for spaceship
    if playerX >= 736:
        playerX = 736
    elif playerX <= 0:
        playerX = 0

    #for invaderX in range(70,660,70):

    invaderX +=invaderX_change

    #enemy movement
    for i in range(num_of_enemies):

        #game over
            if invaderY[i] >450:
                for j in range(num_of_enemies):
                    invaderY[j] = 2000
                game_over_text()
                break
            invaderX[i] += invaderX_change[i]
            if invaderX[i] <= 0:
                invaderX_change[i] = 1
                invaderY[i] += invaderY_change[i]
            elif invaderX[i] >= 736:
                invaderX_change[i] = -1
                invaderY[i] += invaderY_change[i]

            #collision
            collision = iscollision(invaderX[i],invaderY[i],bulletX,bulletY)
            if collision:
                explosion_sound=mixer.Sound('C:/Users/user/Desktop/Space-Invaders-Pygame-master/Space-Invaders-Pygame-master/explosion.wav')
                explosion_sound.play()
                bulletY=480
                bullet_state = "ready"
                score_value += 1
                invaderX[i] = random.randint(0,735)
                invaderY[i] = random.randint(50,150)

            invader(invaderX[i],invaderY[i],i)    

    if bulletY <=0:
        bullet_state="ready"
        bulletY=480

        #bullet_movement
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    
    player(playerX,playerY)
    show_score(testX,testY)
    pygame.display.update()

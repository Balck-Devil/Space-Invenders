import pygame
import random
import math

pygame.init()

screen=pygame.display.set_mode((800,600))

background=pygame.image.load(r"D:\PFP\SahilPatel\Python App And Program\Space Invaders\space_photo.jpg")

# Title and Icons
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load(r"D:\PFP\SahilPatel\Python App And Program\Space Invaders\alien.png")
pygame.display.set_icon(icon)

#Player
playerimg=pygame.image.load(r"D:\PFP\SahilPatel\Python App And Program\Space Invaders\space.png")
playerX=370
playerY=480
playerX_change=0

enemyimg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load(r"D:\PFP\SahilPatel\Python App And Program\Space Invaders\alien1.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(1)
    enemyY_change.append(40)

bulletimg=pygame.image.load(r"D:\PFP\SahilPatel\Python App And Program\Space Invaders\bullet.png")
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=4
bullet_state="ready"

score_value=0
font=pygame.font.Font("freesansbold.ttf",32)
textX=10
textY=10

over_text=pygame.font.Font("freesansbold.ttf",65)
def game_over_text():
    score=over_text.render("GAME OVER",True,(255,255,255))
    screen.blit(score,(200,250))

def show_score(x,y):
    score=font.render("Score :-"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def player(x,y):
    screen.blit(playerimg,(int(x),int(y)))

def enemy(x,y,i):
    screen.blit(enemyimg[i],(int(x),int(y)))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletimg,(int(x)+16,int(y)+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance < 30:
        return  True
    else:
        return False

running =True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change = -2
            if event.key==pygame.K_RIGHT:
                playerX_change = 2
            if event.key==pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0
                
                   
    playerX=playerX+playerX_change
    
    if playerX <= 0:
        playerX=0
    elif playerX >= 736:
        playerX=736

    for i in range(num_of_enemies):

        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j]=2000

            game_over_text()
            break

        enemyX[i]+=enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i]=1.5
            enemyY[i]=enemyY[i]+enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i]=-1.5
            enemyY[i]=enemyY[i]+enemyY_change[i] 

        collision=isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY=480
            bullet_state="ready"
            score_value += 1
            enemyX[i]=random.randint(0,735)
            enemyY[i]=random.randint(50,150)
        enemy(enemyX[i],enemyY[i],i)


    if bulletY <= 0 :
        bulletY=480
        bullet_state="ready" 

    if bullet_state in "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()
import math
# from re import T
import pygame
import random
pygame.init()
screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Space Indevars")
Game_icon = pygame.image.load("001-ufo.png")
pygame.display.set_icon(Game_icon)
# Player Image and others
PlayerImg = pygame.image.load("player.png")
PlayerX = 445
PlayerY = 620
PlayerX_Move = 0
PlayerY_Move = 0

# Enemy Image and others
enemyImg = []
enemyX = []
enemyY = []
enemyX_Move = []
enemyY_Move = []
number_of_enemies = 7
for i in range(number_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, 930))
    enemyY.append(random.randint(50, 450))
    enemyX_Move.append(0.6)
    enemyY_Move.append(40)

# space image
spaceImg = pygame.image.load("space.png")

# bullet image
bulletimg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 3
bullet_state = "Ready"
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
font_x = 10
font_y = 10

# Game over
game_over_text = pygame.font.Font("freesansbold.ttf", 64)

def game_over():
    over_text = font.render("GAME OVER :(", True, (255,255,255))
    screen.blit(over_text, (450,350))

#score
def score_title(x,y):
    score_value = font.render("Score : "+str(score),True, (255,255,255))
    screen.blit(score_value,(x,y))
# collision
def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

#Player function
def player():
    screen.blit(PlayerImg, (PlayerX, PlayerY))

#Enemy
def enemy(x,y,i):
    screen.blit(enemyImg[i], (x, y))

#Fire bullet
def fire_bullet(X, Y):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bulletimg, (X+16, Y+10))


Game_On = True
while Game_On:
    screen.fill((0, 0, 0))
    screen.blit(spaceImg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_On = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PlayerX_Move = -0.7
            if event.key == pygame.K_RIGHT:
                PlayerX_Move = 0.7
            if event.key == pygame.K_SPACE:
                bulletX = PlayerX
                fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PlayerX_Move = 0

    PlayerX += PlayerX_Move
    if PlayerX <= 0:
        PlayerX = 0
    if PlayerX >= 835:
        PlayerX = 835
    for i in range(number_of_enemies):
        # game over
        if enemyY[i] > 590:
            for j in range(number_of_enemies):
                enemyY[j] = 2000
            game_over()
            break
        enemyX[i] += enemyX_Move[i]
        if enemyX[i] <= 0:
            enemyX_Move[i] = 0.6
            enemyY[i] += enemyY_Move[i]
        elif enemyX[i] >= 830:
            enemyX_Move[i] = -0.6
            enemyY[i] += enemyY_Move[i]
        
        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 620
            bullet_state = "Ready"
            score += 1
            
            enemyX[i] = random.randint(5, 830)
            enemyY[i] = random.randint(50, 450)
        enemy(enemyX[i],enemyY[i],i)
        
    if bullet_state is "Fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    if bulletY <= 0:
        bulletY = 610
        bullet_state = "Ready"
    score_title(font_x,font_y)
    player()
    # enemy(i)
    pygame.display.update()


# import pygame
# import random
# pygame.init()
# screen = pygame.display.set_mode((900,700))
# # set caption and image
# pygame.display.set_caption("Space Indevers")
# captionIMG = pygame.image.load("001-ufo.png")
# pygame.display.set_icon(captionIMG)

# # set background
# backgroundIMG = pygame.image.load("space.png")

# #set player
# playerIMG = pygame.image.load("player.png")
# playerX = 455
# playerY = 610
# playerX_change = 0
# def player():
#     screen.blit(playerIMG, (playerX,playerY))

# #set enemy
# enemyIMG = pygame.image.load("enemy.png")
# enemyX = random.randint(0,830)
# enemyY = random.randint(40,800)
# enemyX_change = 0.6
# enemyY_change = 40
# def enemy():
#     screen.blit(enemyIMG,(enemyX,enemyY))
# # set bullet
# bullet_img = pygame.image.load("bullet.png")
# bulletX = 0
# bulletY = 610
# bulletX_change = 0
# bulletY_change = 2

# bullet_state = "ready"
# def fire_bullet(x,y):
#     global bullet_state
#     bullet_state = "fire"
#     # bulletX = playerX
#     screen.blit(bullet_img,(x+16,y+10))
# start = True
# while start :
#     screen.fill((0,0,0))
#     screen.blit(backgroundIMG,(0,0))
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             start = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 playerX_change = -0.8
#             if event.key == pygame.K_RIGHT:
#                 playerX_change = 0.8
#             if event.key == pygame.K_SPACE:
#                 bulletX = playerX
#                 fire_bullet(bulletX,bulletY)
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                 playerX_change = 0

#     playerX += playerX_change
#     if playerX <= 0:
#         playerX = 0
#     if playerX >= 830:
#         playerX = 830
#     enemyX += enemyX_change
#     if enemyX <= 0 :
#         enemyX_change = 0.6
#         enemyX += enemyX_change
#         enemyY +=enemyY_change
#     elif enemyX >= 830 :
#         enemyX_change = -0.6
#         enemyX += enemyX_change
#         enemyY +=enemyY_change
#     if bullet_state == "fire":
#         fire_bullet(bulletX,bulletY)
#         bulletY -=bulletY_change
#     if bulletY <=0:
#         bulletY = 610
#         bullet_state = "ready"
#     player()
#     enemy()
#     pygame.display.update()

import pygame
import time
from random import randint
import objects

from sqlalchemy import true

#Initialize pygame
pygame.init()

screen = pygame.display.set_mode((800,800))

#Set Screen Title
pygame.display.set_caption("PyPong")

#App Icon
icon = pygame.image.load("media/ico.png")
pygame.display.set_icon(icon)

#Starting logo
logo = pygame.image.load("media/PyPong.png")
logoX = 209
logoY = 150

#Game Over image
end = pygame.image.load("media/game_over.png")
endX = 259
endY = 175

anykey = "Press Any Key"
font = pygame.font.SysFont('arial', 20)

anykeyX = 320
anykeyY = 500

def drawLogo():
    screen.blit(logo, (logoX,logoY))

def drawAnyKey():
    textAnyKey = font.render(anykey,True,(255,255,255))
    screen.blit(textAnyKey, (anykeyX,anykeyY))

def gameOver():
    screen.blit(end, (endX,endY))
    pygame.display.update()


def bouncingBall():
    ball = objects.Ball(400,400,5,2)
    paddle1 = objects.Paddle()
    white = (255,255,255)

    w,h = pygame.display.get_surface().get_size()

    clock = 0

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        move_ticker = 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if move_ticker == 0:
                move_ticker = 30
                paddle1.moveUp()

        if keys[pygame.K_DOWN]:
            if move_ticker == 0:
                move_ticker = 30
                paddle1.moveDown()

        move_ticker -=1
                
        clock += 1
        if clock == 10:
            ball.move()
            clock = 0
        
        running = ball.checkCollisions(w,h)

        if paddle1.checkBallCollision(ball):
            wall = paddle1.posX + paddle1.width + 1
            ball.bounceX(wall)

        screen.fill((50, 50, 50))
        
        pygame.draw.rect(screen,white,pygame.Rect(ball.posX,ball.posY,ball.width,ball.height))
        pygame.draw.rect(screen,white,pygame.Rect(paddle1.posX,paddle1.posY,paddle1.width,paddle1.height))
        pygame.display.update()

    screen.fill((50,50,50))
    pygame.display.update

running = True
startScreen = True
clock = 0
while running:

    screen.fill((50, 50, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            startScreen = False

    if startScreen:
        drawLogo()
        if clock < 150:
            drawAnyKey()
        
        clock += 1

        if clock == 300:
            clock = 0
    else:
        bouncingBall()

        gameOver()

        time.sleep(2)
        running = False
    
    pygame.display.update()

pygame.quit()
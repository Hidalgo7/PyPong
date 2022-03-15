import pygame
from random import randint

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

anykey = "Press Any Key"
font = pygame.font.SysFont('arial', 20)

anykeyX = 320
anykeyY = 500

def drawLogo():
    screen.blit(logo, (logoX,logoY))

def drawAnyKey():
    textAnyKey = font.render(anykey,True,(255,255,255))
    screen.blit(textAnyKey, (anykeyX,anykeyY))


def bouncingBall():
    white = (255,255,255)
    ballX = 400
    ballY = 400
    ballSpeed = pygame.Vector2((randint(-5,5),randint(-5,5)))

    w,h = pygame.display.get_surface().get_size()

    time = 0

    while True:
        time += 1
        if time == 10:
            ballX += ballSpeed.x
            ballY += ballSpeed.y
            time = 0
        
        if ballX > w - 20:
            ballSpeed.x = -ballSpeed.x
            ballX = w-21
        elif ballX < 0:
            ballSpeed.x = -ballSpeed.x
            ballX = 1

        if ballY > h - 20:
            ballSpeed.y = -ballSpeed.y
            ballY = h-21
        elif ballY < 0:
            ballSpeed.y = -ballSpeed.y
            ballY = 1
        
        

        screen.fill((50, 50, 50))
        
        pygame.draw.rect(screen,white,pygame.Rect(ballX,ballY,20,20))
        pygame.display.update()


running = True
startScreen = True
time = 0
while running:

    screen.fill((50, 50, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            startScreen = False

    if startScreen:
        drawLogo()
        if time < 250:
            drawAnyKey()
        
        time += 1

        if time == 500:
            time = 0
    else:
        bouncingBall()
    
    pygame.display.update()
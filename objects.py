import pygame

class Ball():
    def __init__(self,posX,posY,speedX,speedY):
        self.width = 20
        self.height = 20
        self.posX = posX
        self.posY = posY
        self.speed = pygame.Vector2(speedX,speedY)

    def checkCollisions(self,width,height):
        if self.posX > width - 20:
            self.bounceX(width)
        elif self.posX < 0:
            self.bounceX(0)
            return False

        if self.posY > height - 20:
            self.bounceY(height)
        elif self.posY < 0:
            self.bounceY(0)
        
        return True
    def move(self):
        self.posX += self.speed.x
        self.posY += self.speed.y
    
    def bounceX(self,wall):
        self.speed.x = -self.speed.x

        if self.speed.x < 0:
            self.posX = wall - self.width - 2
        else:
            self.posX = wall + 1
        # if wall > 0:
        #     self.posX = wall - self.width - 1
        # else:
        #     self.posX = 1

    def bounceY(self,wall):
        self.speed.y = -self.speed.y
        if wall > 0:
            self.posY = wall - self.width - 1
        else:
            self.posY = 1

class Paddle():
    def __init__(self):
        self.width = 20
        self.height = 120
        self.posX = 30
        self.posY = 30

    def moveUp(self):
        self.posY -= 1

    def moveDown(self):
        self.posY += 1

    def checkBallCollision(self,ball):
        lowerY = self.posY
        upperY = self.posY + self.height

        lowerX = self.posX
        upperX = self.posX + self.width   

        if ball.posY <= upperY and ball.posY >= lowerY:
            if ball.posX <= upperX and ball.posX >= lowerX:
                return True

        return False

import sys, pygame, math
from Ball import Ball

class PlayerPaddle(Ball):
    def __init__(self, image, maxSpeed, pos = [0,0]):
        Ball.__init__(self, image, [0,0], pos)
        
        self.maxSpeedx = maxSpeed[0]
        self.maxSpeedy = maxSpeed[1]
        
        self.didBounceX = False
        self.didBounceY = False

    def collideScreen(self, size):
        width = size[0]
        height = size[1]
        
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = -self.speedy
                selfdidBounceY = True
                self.move()
                self.speedy = 0
        
    def go(self, direction):
        if direction == "up":
            self.speedy = -self.maxSpeedy
        elif direction == "down":
            self.speedy = self.maxSpeedy
        
        if direction == "stop up":
            self.speedy = 0
        elif direction == "stop down":
            self.speedy = 0

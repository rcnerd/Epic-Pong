import sys, pygame, math
from Ball import Ball

class PlayerPaddle():
    def __init__(self, image, maxSpeed, pos = [0,0]):
        Ball.__init__(self, image, [0,0], pos)
        
        self.maxSpeedx = maxSpeed[0]
        self.maxSpeedy = maxSpeed[1]

    def collideScreen(self, size):
        width = size[0]
        height = size[1]
        
    def go(self, direction):
        if direction == "up":
            self.speedy = -self.maxSpeedy
        elif direction == "down":
            self.speedy = self.maxSpeedy
        
        if direction == "stop up":
            self.speedy = 0
        elif direction == "stop down":
            self.speedy = 0

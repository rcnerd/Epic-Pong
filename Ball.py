import sys, pygame, math, image
from Ball import *
pygame.init()

class Ball():
    def __init__(self, images, speed, pos=[0,0]):
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        
        self.images = []
        for image in images:
            self.images += [pygame.image.load(image)]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.radius = self.rect.width/2 - 2

    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        self.didBounceX = False
        self.didBounceY = False

    def collideScreen(self, size):
        width = size[0]
        height = size[1]
        
        self.frame = 0
        self.maxFrame = len(self.images)-1
        self.timer = 0
        self.timerMax = .05* 60
        
        self.didBounceX = False
        self.didBounceY = False

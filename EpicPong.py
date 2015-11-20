import sys, pygame, math
from PlayerPaddle import*
from Ball import*
pygame.init()

clock = pygame.time.Clock()

width = 900
height = 900
size = width, height

bgColor = r,b,g = 120,0,56

screen = pygame.display.set_mode(size)

player = PlayerPaddle( [width/2, height/2], "prainbow.png")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        
        
        bgColor = r,b,g
    screen.fill(bgColor)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(60)

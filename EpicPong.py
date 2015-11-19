import sys, pygame, math
pygame.init()

clock = pygame.time.Clock()

width = 900
height = 900
size = width, height

bgColor = r,b,g = 120,0,56

screen = pygame.display.set_mode(size)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        
        
        bgColor = r,b,g
    screen.fill(bgColor)
    pygame.display.flip()
    clock.tick(60)

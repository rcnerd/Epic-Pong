import sys, pygame, math, random
from PlayerPaddle import *
from Ball import *
pygame.init()

clock = pygame.time.Clock()

width = 900
height = 700
size = width, height

bgColor = r,b,g = 120,0,56

screen = pygame.display.set_mode(size)

player = PlayerPaddle( ["pRainbow.png"], [10,10], [width/2, height/2])
player2 = PlayerPaddle( ["player2.png"], [10,10], [width/2, height/2])

ball = Ball(["BlackBall.png"], [6,6], [300,400])

balls = []
ballSpawnTimer = 0
ballSpawnTimerMax = .1 * 60


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.go("up")
            elif event.key == pygame.K_DOWN:
                player.go("down")

            elif event.key == pygame.K_w:
                player2.go("up")
            elif event.key == pygame.K_s:
                player2.go("down")
           
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.go("stop up")
            elif event.key == pygame.K_DOWN:
                player.go("stop down")
            
            elif event.key == pygame.K_w:
                player2.go("stop up")
            elif event.key == pygame.K_s:
                player2.go("stop down")
        
        ballSpawnTimer += 1
    if ballSpawnTimer >= ballSpawnTimerMax:
        ballSpawnTimer = 0
        ballSpeed = [random.randint(-5, 5),
                     random.randint(-5, 5)]
        ballPos = [random.randint(100, width-100),
                     random.randint(100, height-100)]
        
    player.update(size)
    player2.update(size)
        
    for ball in balls:
        ball.update(size)
        
    bgColor = r,b,g
    screen.fill(bgColor)
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    screen.blit(player.image, player.rect)
    screen.blit(player2.image, player2.rect)

    pygame.display.flip()
    clock.tick(60)
    #print clock.get_fps()

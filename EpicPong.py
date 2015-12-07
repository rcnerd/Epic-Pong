import sys, pygame, math, random
from PlayerPaddle import *
from Ball import *
pygame.init()

clock = pygame.time.Clock()

width = 900
height = 700
size = width, height

bgColor = r,b,g = 255,0,255

screen = pygame.display.set_mode(size)

balls = []
ballTimer = 0
ballTimerMax = .1 * 60

player = PlayerPaddle( ["pRainbow.png"], [10,10], [850, 600])
player2 = PlayerPaddle( ["player2.png"], [10,10], [0, 0])

ball = Ball(["BlackBall.png"], [6,6], [300,400])

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
        
    ballTimer += 1
    if ballTimer >= ballTimerMax:
        ballTimer = 0
        if len(balls) < 2:
            #ballSpeed = random.randint(-5, 5)
            #ballPos = random.randint(100, width-100)
            balls += [Ball(["BlackBall.png",
                            "BlackBall1.png",
                            "BlackBall2.png",
                            "BlackBall3.png"],
                           [5,5],
                           [425, 350])]
            #print len(balls), clock.get_fps()
        
    player.update(size)
    player2.update(size)
        
    for ball in balls:
        ball.update(size)
        
    for first in balls:
        player.collideBall(first)
        if first.collideBall(player):
            first.collidePaddle(player)
        else:
            for second in balls:
                if first != second:
                    first.collideBall(second)
                elif second != first:
                    second.collideBall(first)
    
    for ball in balls:
        if not ball.living:
            balls.remove(ball)
        
    bgColor = r,b,g
    screen.fill(bgColor)
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    screen.blit(player.image, player.rect)
    screen.blit(player2.image, player2.rect)

    pygame.display.flip()
    clock.tick(60)
    #print clock.get_fps()

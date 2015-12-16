import sys, pygame, math, random
from PlayerPaddle import *
from Ball import *
from Score import*
pygame.init()

clock = pygame.time.Clock()

width = 900
height = 700
size = width, height

bgColor = r,b,g = 255,255,255

screen = pygame.display.set_mode(size)

balls = []
ballTimer = 0
ballTimerMax = .1 * 60

player = PlayerPaddle( ["Pics/Player/player.png"], [10,10], [880, 300])
player2 = PlayerPaddle( ["Pics/Player/player2.png"], [10,10], [10, 300])

scoreP1 = Score([15,15])
scoreP2 = Score([width - 15, height - 15])
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
        if len(balls) < 1:
            #ballSpeed = random.randint(-5, 5)
            #ballPos = random.randint(100, width-100)
            balls += [Ball(["Pics/Ball/BlackBall.png",
                            "Pics/Ball/BlackBall1.png",
                            "Pics/Ball/BlackBall2.png",
                            "Pics/Ball/BlackBall3.png"],
                           [9,9],
                           [450, 350])]
            #print len(balls), clock.get_fps()
        
    player.update(size)
    player2.update(size)
        
    for ball in balls:
        ball.update(size)
        
    for first in balls:
        first.collidePaddle(player)
        first.collidePaddle(player2)
        if first.collidePaddle:
            scoreP1.increase(1)
            scoreP2.increase(1)
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
    screen.blit(scoreP1.image, scoreP1.rect)
    screen.blit(scoreP2.image, scoreP2.rect)
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    screen.blit(player.image, player.rect)
    screen.blit(player2.image, player2.rect)
    pygame.display.flip()
    clock.tick(60)
    #print clock.get_fps()

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
ballTimerMax = 2 * 60

player = PlayerPaddle( ["Pics/Player/player.png"], [10,10], [10, 300])
player2 = PlayerPaddle( ["Pics/Player/player2.png"], [10,10], [880, 300])

scoreP1 = Score([300, 350])
scoreP2 = Score([600, 350])

endScore = 3

while True:
    while scoreP1.score < endScore and scoreP2.score < endScore:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.go("up")
                elif event.key == pygame.K_s:
                    player.go("down")

                elif event.key == pygame.K_UP:
                    player2.go("up")
                elif event.key == pygame.K_DOWN:
                    player2.go("down")
               
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.go("stop up")
                elif event.key == pygame.K_s:
                    player.go("stop down")
                
                elif event.key == pygame.K_UP:
                    player2.go("stop up")
                elif event.key == pygame.K_DOWN:
                    player2.go("stop down")
                    
        ballTimer += 1
        if ballTimer >= ballTimerMax:
            ballTimer = 0
            if len(balls) < 1:
                d = random.randint(1,4)
                if d == 1:
                    ballSpeed = [random.randint(7,8), random.randint(7,8)]
                elif d == 2:
                    ballSpeed = [random.randint(-8,-7), random.randint(7,8)]
                elif d == 3:
                    ballSpeed = [random.randint(-8,-7), random.randint(-8,-7)]
                elif d == 4:
                    ballSpeed = [random.randint(7,8), random.randint(-8,-7)]
                balls += [Ball(["Pics/Ball/BlackBall.png",
                                "Pics/Ball/BlackBall1.png",
                                "Pics/Ball/BlackBall2.png",
                                "Pics/Ball/BlackBall3.png"],
                                ballSpeed,
                               [435,338])]
                    #print len(balls), clock.get_fps()
            
        player.update(size)
        player2.update(size)
        scoreP1.update()
        scoreP2.update()
            
        for ball in balls:
            ball.update(size)
            if ball.collideScreen(size) == "right":
                scoreP1.increase(1)
            elif ball.collideScreen(size) == "left":
                scoreP2.increase(1)
            #elif ballcollideScreen(size) == "left" or "right":
                
            
        for first in balls:
            first.collidePaddle(player)
            first.collidePaddle(player2)
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
        
        
        
    while scoreP1.score >= endScore and scoreP2.score <= endScore:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if scoreP1.score == endScore and scoreP2.score < endScore:
                print "Player 1 wins"
                
        bg = pygame.image.load("Pics/Player/player1wins.png")
        bgrect = bg.get_rect(center = [width/2,height/2])
        
        screen.fill(bgColor)
        screen.blit(bg, bgrect)
        pygame.display.flip()
        clock.tick(60)
        
    while scoreP2.score >= endScore and scoreP1.score <= endScore:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

            if scoreP2.score == endScore and scoreP1.score < endScore:
                print "Player 2 wins"

            
            print "Player 2 Wins!!!"
        
        bg = pygame.image.load("Pics/Player/player2wins.png")
        bgrect = bg.get_rect(center = [width/2,height/2])
        
        screen.fill(bgColor)
        screen.blit(bg, bgrect)
        pygame.display.flip()
        clock.tick(60)

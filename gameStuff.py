import pygame
import robot
import cards

pygame.init()


maxX = 1000
maxY = 1000

gridRows = 11
gridCols = 11
gridXsize = maxX/gridCols
gridYzize = maxY/gridRows   # ******** not int
windowSize = [maxX, maxY]
screen = pygame.display.set_mode(windowSize)
gameBoard = pygame.image.load('graphics/2016doodle.jpg')
gameBoard = pygame.transform.scale(gameBoard, (1000, 1000))
robot1 = robot.Robot('Lloyd', 0, 0)
robot1.setMoveMult(gridXsize)  # int is not callable
robot1.img = pygame.image.load('graphics/UR1.png')
robot1.img = pygame.transform.scale(robot1.img, (84, 84))
screen.blit(gameBoard, (0, 0))
screen.blit(robot1.img, (robot1.x, robot1.y))
d = cards.Deck()

done = False
keyPressed = False

while not done:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_i] and robot1.dir == 0 and not keyPressed:
        keyPressed = True
        if robot1.y > 0:
            robot1.moveUp()
            screen.blit(gameBoard, (0, 0))
            screen.blit(robot1.img, (robot1.x, robot1.y))
        print(robot1.x, robot1.y, robot1.dir)  # get rid of this

    if keys[pygame.K_j] and robot1.dir == 3 and not keyPressed:
        keyPressed = True
        if robot1.x > 0:
            robot1.moveLeft()
            screen.blit(gameBoard, (0, 0))
            screen.blit(robot1.img, (robot1.x, robot1.y))
        print(robot1.x, robot1.y, robot1.dir)  # get rid of this

    if keys[pygame.K_k] and robot1.dir == 2 and not keyPressed:
        keyPressed = True
        if robot1.y < maxY - 40:
            robot1.moveDown()
            screen.blit(gameBoard, (0, 0))
            screen.blit(robot1.img, (robot1.x, robot1.y))
        print(robot1.x, robot1.y, robot1.dir)  # get rid of this

    if keys[pygame.K_l] and robot1.dir == 1 and not keyPressed:
        keyPressed = True
        if robot1.x < maxX - 40:
            robot1.moveRight()
            screen.blit(gameBoard, (0, 0))
            screen.blit(robot1.img, (robot1.x, robot1.y))
        print(robot1.x, robot1.y, robot1.dir)  # get rid of this

    if keys[pygame.K_u] and not keyPressed:
        keyPressed = True
        robot1.turnLeft()
        robot1.img = pygame.image.load(f"graphics/UR{str(robot1.dir)}.png")
        robot1.img = pygame.transform.scale(robot1.img, (84, 84))
        screen.blit(gameBoard, (0, 0))
        screen.blit(robot1.img, (robot1.x, robot1.y))
        print(robot1.x, robot1.y, robot1.dir)  # get rid of this

    if keys[pygame.K_o] and not keyPressed:
        keyPressed = True
        robot1.turnRight()
        robot1.img = pygame.image.load(f"graphics/UR{str(robot1.dir)}.png")
        robot1.img = pygame.transform.scale(robot1.img, (84, 84))
        screen.blit(gameBoard, (0, 0))
        screen.blit(robot1.img, (robot1.x, robot1.y))
        print(robot1.x, robot1.y, robot1.dir)  # get rid of this

# check for off the board 460
    c = d.getCard()
    c.applyCard(robot1)



    if keyPressed and event.type == pygame.KEYUP:
        keyPressed = False

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


pygame.quit()

import pygame

def rot_center(image, angle): # not sure if this works
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    return rot_image


pygame.init()

windowSize = [500, 500]
screen = pygame.display.set_mode(windowSize)
gameBoard = pygame.image.load('graphics/2016doodle.jpg')
robot1 = pygame.image.load('graphics/UglyBot 2000.png')
screen.blit(gameBoard, (0, 0))
screen.blit(robot1, (0, 0))



done = False

while not done:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_u]: # does go into code when u is pushed
        rot_center(robot1, 90)
        screen.blit(robot1, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()


pygame.quit()

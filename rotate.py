import pygame

pygame.init()

clock = pygame.time.Clock()
windowSize = (500, 500)
screen = pygame.display.set_mode(windowSize)
white = pygame.color.Color("#FFFFFF")

robot1 = pygame.image.load('graphics/UglyBot 2000.png')
robot1Dir = 0
r1DirFile = f"UR{str(robot1Dir)}.png"
#robot1.set_colorkey((0, 0, 0))
angle = 0
rotatedImage = pygame.transform.rotate(robot1, angle)


done = False

while not done:
    screen.fill(white)
    screen.blit(rotatedImage, (0, 0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_u]:
        angle += 0.001
        rotatedImage = pygame.transform.rotate(rotatedImage, angle)
        screen.blit(rotatedImage, (0, 0))
    if keys[pygame.K_o]:
        angle -= 0.001
        rotatedImage = pygame.transform.rotate(rotatedImage, angle)
        screen.blit(rotatedImage, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
    clock.tick()

pygame.quit()

import pygame


fileName = 'graphics/2016doodle.jpg'
picture = pygame.image.load(fileName)
picture = pygame.transform.scale(picture, (1000, 1000))

windowSize = [1000, 1000]
screen = pygame.display.set_mode(windowSize)

fileName = 'graphics/2016doodle.jpg'
picture = pygame.image.load(fileName)
picture = pygame.transform.scale(picture, (1000, 1000))


screen.blit(picture, (0, 0))

pygame.display.flip()

done = False

while not done:
    pass


pygame.quit()

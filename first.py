import pygame
pygame.init()
scr = pygame.display.set_mode((600,500))
pygame.display.set_caption('Pygame Window')
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.display.flip()
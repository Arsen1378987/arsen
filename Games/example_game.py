import pygame
pygame.init()
screen = pygame.display.set_mode((2000,1000))
pygame.display.set_caption('game 1')
running = True
x = 100
y = 210
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                x = 100
                y = 210
    screen.fill((18,180,250))
    pygame.draw.rect(screen, (64, 128, 255), (100, 100, 1000, 700), 8)
    pygame.draw.lines(screen, (230, 4, 100), True, [[200, 200], [500, 500], [700, 200]], 20)
    pygame.draw.polygon(screen, (255, 255, 255), [[450, 450], [810, 300], [900, 60], [80, 700]], 8)
    pygame.draw.circle(screen, (47, 250, 1), (x,y), 100)
    pygame.display.flip()
    x += 5
    y += 5
    clock.tick(27)
pygame.display.flip()
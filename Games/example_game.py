import pygame
import random
pygame.init()
screen = pygame.display.set_mode((2000,1000))
pygame.display.set_caption('game 1')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
running = True
clock = pygame.time.Clock()
font = pygame.font.Font(None,50)
color = GREEN
Colors = [YELLOW,GREEN,GRAY,BLACK,LIGHT_BLUE,PINK,WHITE]
def text(messege,color):
    words = font.render(messege,True,color)
    place = words.get_rect(center = (1000,500))
    screen.blit(words,place)
x = 0
v = 5
LEVEL = 1
gate = -1
win = 0
heights = [200,500,800]
y = random.choice(heights)
def draw():
    screen.fill(WHITE)
    gate_colors = [GRAY,GRAY,GRAY]
    if gate != -1:
        gate_colors[gate] = GREEN
    pygame.draw.rect(screen,gate_colors[0],(1950,heights[0]-50,50,100))
    pygame.draw.rect(screen, gate_colors[1], (1950, heights[1] - 50, 50, 100))
    pygame.draw.rect(screen, gate_colors[2], (1950, heights[2] - 50, 50, 100))
    pygame.draw.circle(screen, color, (x,y),25)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                color = random.choice(Colors)
            if event.key == pygame.K_1:
                gate = 0
            if event.key == pygame.K_2:
                gate = 1
            if event.key == pygame.K_3:
                gate = 2
    text("Сергио Агуеро 33 года легенда футбола",color)
    draw()
    pygame.display.flip()
    clock.tick(30)
pygame.display.flip()
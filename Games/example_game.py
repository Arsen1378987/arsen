import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1900,1000))
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
v = 9
LEVEL = 5
gate = -1
win = 0
heights = [200,500,800]
y = random.choice(heights)
def draw():
    screen.fill(WHITE)
    gate_colors = [GRAY,GRAY,GRAY]
    if gate != -1:
        gate_colors[gate] = GREEN
    pygame.draw.rect(screen,gate_colors[0],(1850,heights[0]-50,50,100))
    pygame.draw.rect(screen, gate_colors[1], (1850, heights[1] - 50, 50, 100))
    pygame.draw.rect(screen, gate_colors[2], (1850, heights[2] - 50, 50, 100))
    pygame.draw.circle(screen, color, (x,y),50)
def VICTORY():
    screen.fill(GREEN)
    text("ПОБЕДА!!", YELLOW)
    pygame.display.flip()
    run = True
    while run:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                run = False
    pygame.quit()
    exit()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                color = random.choice(Colors)
            if event.key == pygame.K_1 and x < 1800:
                gate = 0
            if event.key == pygame.K_2 and x < 1800:
                gate = 1
            if event.key == pygame.K_3 and x < 1800:
                gate = 2
            if win and event.key == pygame.K_RETURN:
                LEVEL += 1
                win = 0
                x = 0
                y = random.choice(heights)
                v = LEVEL * 5
                gate = -1
    if LEVEL > 24:
        VICTORY()
    if x >= 1800:
        v = 0
        if gate == -1 or heights[gate] != y:
            text("Ты проиграл!", BLACK)
        else:
            text("Уровень пройден", GREEN)
            win = 1

    text("Сергио Агуеро 33 года легенда футбола",color)
    draw()
    x += v
    pygame.display.flip()
    clock.tick(30)
pygame.display.flip()
import pygame, sys

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load("beach_ball.png")

# Starting coordinates
x = 50
y = 50
x_speed = 10

screen.blit(my_ball, [x, y])
pygame.display.flip()

# Moving the ball
for looper in range (1, 100):
    pygame.time.delay(10)
    pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
    x = x + 5
    screen.blit(my_ball, [x, y])
    pygame.display.flip()

# Program control
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
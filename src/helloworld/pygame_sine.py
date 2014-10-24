import pygame, sys
import math

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
plotPoints = []
for x in range(0, 640):
    y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240)
    plotPoints.append([x, y])
    
# lines() takes five params:
# 1. the surface to draw on
# 2. the color of the line (a list of rgb values)
# 3. whether a line should be drawn from endpoint back to beginning
# 4. the list of points to connect
# 5. the width of the line
pygame.draw.lines(screen, [0,0,0], False, plotPoints, 2)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
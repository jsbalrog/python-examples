import pygame
import sys
import random

class MyBallClass(pygame.sprite.Sprite):
    
    def __init__(self, image_file, location, speed):
        # Initialize the sprite
        pygame.sprite.Sprite.__init__(self)
        
        #Load an image file into it
        self.image = pygame.image.load(image_file)
        
        # Get the rectangle that defines the boundaries of the image
        self.rect = self.image.get_rect()
        
        # Set the initial location of the ball
        self.rect.left, self.rect.top = location
        
        # Set the speed attribute for the ball
        self.speed = speed
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
            
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]
        
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
image_file = "beach_ball.png"
balls = []

for row in range(0, 3):
    for column in range (0, 3):
        # Make the location different each time through the loop
        location = [column * 180 + random.randint(0, 10), row * 180 + random.randint(0, 10)]
        
        speed = [random.randint(-10, 10), random.randint(-10, 10)]

        # Create a ball at a specific location
        ball = MyBallClass(image_file, location, speed)

        # Add the ball to the list
        balls.append(ball)
        
for ball in balls:
    screen.blit(ball.image, ball.rect)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    pygame.time.delay(20)
    screen.fill([255, 255, 255])
    for ball in balls:
        ball.move()
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()

from pygame.locals import *
import pygame
import sys
from pygame import key
import time



class Snake:

    length = 2
    position = []
    speed = [1, 0]
    def __init__(self, length):
        self.length = length
        for i in range(0, length):
            self.position.append([100 + 30 * i, 300])
        print("len is :",len(self.position))


    def move_right(self):
        if self.speed[0] == 0:
            self.speed[0] = 1
            self.speed[1] = 0

    def move_left(self):
        if self.speed[0] == 0:
            self.speed[0] = -1
            self.speed[1] = 0

    def move_up(self):
        if self.speed[1] == 0:
            self.speed[1] = -1
            self.speed[0] = 0

    def move_down(self):
        if self.speed[1] == 0:
            self.speed[1] = 1
            self.speed[0] = 0

    def update(self):
        
        for i in range(self.length - 1, 0, -1):
            self.position[i] = self.position[i-1]
        self.position[0][0] += self.speed[0]
        self.position[0][1] += self.speed[1]

    def draw(self, surface, image):
        for i in range(0, self.length):
            surface.blit(image, tuple(self.position[i]))



class Game:
    
    size = w, h = 500, 600
    black = 0, 0, 0

    # def __init__(self):


    screen = pygame.display.set_mode(size)
    pygame.init()
    snake = Snake(2)

    snake_body = pygame.image.load("ball.png").convert()


    while 1:
        time.sleep(0.01)
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        if (keys[K_UP]):
            snake.move_up()
        if (keys[K_DOWN]):
            snake.move_down()
        if (keys[K_RIGHT]):
            snake.move_right()
        if (keys[K_LEFT]):
            snake.move_left()


        # if ballrect.left < 0 or ballrect.right > w:
        #     speed[0] = -speed[0]
        # if ballrect.top < 0 or ballrect.bottom > h:
        #     speed[1] = -speed[1]

        
        snake.update()
        screen.fill(black)
        snake.draw(screen, snake_body)
        pygame.display.flip()
